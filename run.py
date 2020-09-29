import os
from item_dump_parser import ItemProcessor
from item_dump_parser.utils import write_file

item_processor = ItemProcessor()

item_processor.run()

write_file("item_dump.txt", item_processor.dump())
