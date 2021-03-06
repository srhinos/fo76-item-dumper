import asyncio
import json
import logging
import os
import traceback
from datetime import datetime
from inspect import trace
from pprint import pprint

import aiohttp

from item_dump_parser.constants import (
    FED76_MAPPING_URL,
    OUTPUT_STRING_FORMAT,
    OUPUT_ONLY_NEW,
    ALERT_ON_WEB_REQUESTS,
)
from item_dump_parser.models.item import Item
from item_dump_parser.utils import load_json, write_json, write_file

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class ItemProcessor:
    def __init__(self):
        self.item_dump_json = self.load_character_data()

        self.item_list = []

    # noinspection PyMethodOverriding
    def run(self):
        """
        Used for initializing the asynchronous event loop.
        This was only cool when I made webrequests lol
        """
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.get_fed76_mapping_data())
            loop.run_until_complete(self.build())
        except Exception:
            for task in asyncio.Task.all_tasks():
                task.cancel()
        finally:
            loop.close()

    async def get_fed76_mapping_data(self):
        try:
            if ALERT_ON_WEB_REQUESTS:
                logging.warning(f"[GET] -> FED76 (Reason: Fetching Mappings)")
            async with aiohttp.ClientSession() as sess:
                async with sess.get(FED76_MAPPING_URL) as r:
                    fed76_mapping = await r.json()

            write_json("fed76_mapping.json", fed76_mapping)
        except Exception:
            traceback.print_exc()

    async def build(self, **filter_kwargs):
        """
        Applies any filters that were passed in to the raw item dump json, then
        Iterates over the item dump and parses each json into an Item class.
        Finally, appends each parsed item to the item_list.
        """
        try:
            await self.filter_player_data(**filter_kwargs)
            fed76_resp_cache = load_json("fed76_resp_cache.json")

            for json_item in self.item_dump_json:
                item = Item(**json_item)
                if item:
                    item_hash = item.gen_hash()
                    if item_hash not in fed76_resp_cache:
                        resp = await item.get_fed76_value()
                        fed76_resp_cache[item_hash] = resp
                    else:
                        await item.get_fed76_value(fed76_resp_cache[item_hash])

                    self.item_list.append(item)
            write_json("fed76_resp_cache.json", fed76_resp_cache)
        except Exception as e:
            traceback.print_exc()
            raise e

    def dump(self):
        """
        Takes processed item data and does some transformation to it.
        As of my writing this, it apply the output string format to each item and writes it to a file
        """
        output = []
        previous_output = None
        try:

            if OUPUT_ONLY_NEW:
                if os.path.exists("previous_output.json"):
                    previous_output = set(load_json("previous_output.json"))
                else:
                    previous_output = set([])

            for item in self.item_list:
                if (
                    item.item_type.startswith("WEAPON")
                    and item.fed76_value
                    and int(item.fed76_value) > 10000
                ):
                    if previous_output is not None:
                        if item.gen_hash() not in previous_output:
                            output.append(OUTPUT_STRING_FORMAT.format(item))
                            previous_output.add(item.gen_hash())
                    else:
                        output.append(OUTPUT_STRING_FORMAT.format(item))

            write_file("item_dump.txt", output)
            if previous_output:
                write_json("previous_output.json", list(previous_output))

        except Exception:
            traceback.print_exc()

    def load_character_data(self):
        """
        Attempts to walk the directory for all item dumps to parse all separate user dumps into a single mapping.
        Data is not deduplicated and exists with all unwanted fields.
        """
        item_data = []
        for root, _, files in os.walk("ItemExtractorMod", topdown=False):
            files = [file for file in files if ".json" in file]
            characters = set([file.split("_")[0] for file in files])
            important_files = [
                max([file for file in files if file.startswith(character)])
                for character in characters
            ]

            for file in important_files:
                character_data = []
                fileroute = os.path.join(root, file)
                json_file = load_json(fileroute)
                character_data.extend(
                    json_file["characterInventories"][file.split("_")[0]][
                        "stashInventory"
                    ]
                )
                character_data.extend(
                    json_file["characterInventories"][file.split("_")[0]][
                        "playerInventory"
                    ]
                )
                item_data.extend(
                    [
                        {"character": file.split("_")[0], **item}
                        for item in character_data
                    ]
                )

        return item_data

    async def filter_player_data(self, **kwargs):
        """
        Attempts to dynamically filter out items based on kwargs passed in.

        kwargs should be written exactly like how they're listed on each item.

        EX: filter_player_data(isLegendary=False) will check each item's data dump to
            see if the value "isLegendary" is False.
        """
        return [item for item in self.item_dump_json if kwargs.items() <= item.items()]
