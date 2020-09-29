from logging import Filter
from item_dump_parser.models.damage_type import DamageTypes
from item_dump_parser.models.filter_flag import FilterFlags
from item_dump_parser.models.item_card_text import ItemCardTexts
from item_dump_parser.constants import (
    LEGENDARY_MAPPING,
    ARMOR_MAPPING,
    ITEM_TYPE_MAPPING,
    NAME_MODS_MAPPING,
    ARMOR_LIMB_IDENTIFIER_STRINGS,
    UNUSED_ARMOR_KEYWORDS,
    LEGENDARY_REMAPPING,
    SKIPPED_LEGENDARY_EFFECTS,
)
from item_dump_parser.utils import find as find_in_iter, load_json

__all__ = ["Item"]


class Item:
    """
    Takes in a bunch of data to form a model for an individual item

    Params:
    text (str) - The Text Name Of The Item
    serverHandleID (int) - A Character + Item Specific ID
    count (int) - number of items the character has
    itemValue (int) - cap value assigned to the item
    filterFlag (int) - used when filtering items by the UI
    currentHealth (int) - the current durability of an item
    damage (int) - the amount of damage an item does
    durability (int) - the stat that determines a weapons propensity to break down during use
    maximumHealth (int) - the max amount of durability the item can be repaired to
    weight (float) - how heavy an item is to a person
    weaponDisplayAccuracy (double) - the current accuracy the weapon has stat wise
    weaponDisplayRateOfFire (double) - the current rate of fire the weapon has stat wise
    weaponDisplayRange (double) - the current range the weapon has stat wise
    numLegendaryStars (int) - the number of legendary stars it has (duh)
    itemLevel (int) - the minimum level an item can be used by
    rarity (int) - this is never not -1 for me, no clue what its for
    isTradable (boolean) - whether this item can be traded between players or not
    isSpoiled (boolean) - whether this food item is spoiled or not
    isSetItem (boolean) - whether this item is part of an item set (like strangler heart armor) or not
    isQuestItem (boolean) - whether this item is for a quest or not
    isLegendary (boolean) - whether this item is a legendary or not
    vendingData (dict) - some garbage about vending I'll never use
    #TODO: Finish This
    """

    def __init__(self, **kwargs):
        self.text = (
            (kwargs.get("text")).replace("¢", "").replace("$$ZEUSGLYPH", "").strip()
        )
        self.server_handle_id = kwargs.get("serverHandleId")
        self.count = kwargs.get("count")
        self.item_value = kwargs.get("itemValue")
        self.filter_flag = kwargs.get("filterFlag")
        self.current_health = kwargs.get("currentHealth")
        self.damage = kwargs.get("damage")
        self.durability = kwargs.get("durability")
        self.maximum_health = kwargs.get("maximumHealth")
        self.weight = kwargs.get("weight")
        self.weapon_display_accuracy = kwargs.get("weaponDisplayAccuracy")
        self.weapon_display_rate_of_fire = kwargs.get("weaponDisplayRateOfFire")
        self.weapon_display_range = kwargs.get("weaponDisplayRange")
        self.num_legendary_stars = kwargs.get("numLegendaryStars")
        self.item_level = kwargs.get("itemLevel")
        self.rarity = kwargs.get("rarity")
        self.is_tradable = kwargs.get("isTradable")
        self.is_spoiled = kwargs.get("isSpoiled")
        self.is_set_item = kwargs.get("isSetItem")
        self.is_quest_item = kwargs.get("isQuestItem")
        self.is_legendary = kwargs.get("isLegendary")
        self.vending_data = kwargs.get("vendingData")
        self.item_card_entries = kwargs.get("ItemCardEntries")
        self.mod_card_entries = kwargs.get("ModCardEntries")
        self.character = kwargs.get("character")

        self.legendary_effects = []
        self.one_star_effect = None
        self.two_star_effect = None
        self.three_star_effect = None

        self.item_type = None
        self.description = None

        self.armor_grade = None
        self.damage_resistance = None
        self.energy_resistance = None
        self.radiation_resistance = None

        self.filter_flag_text = self.process_filter_flag_text()

        self.plain_name = None
        self.process_item_name_and_type()
        self.process_item_card_entries()
        self.process_armor_grade()

    def process_filter_flag_text(self):
        """
        finds the specific filter flag for the item.
        """
        filter_flag_text = next(
            (fflag for fflag in FilterFlags.ALL if self.filter_flag in fflag.flags),
            FilterFlags.UNKNOWN,
        )
        if filter_flag_text == FilterFlags.WEAPON:
            for item_card in self.item_card_entries:
                if item_card.get("damage_type_text") == DamageTypes.AMMO.name:
                    return FilterFlags.WEAPON_RANGED.name

                item_card_text = next(
                    (
                        ic_text
                        for ic_text in ItemCardTexts.ALL
                        if item_card["text"] == ic_text.text
                    ),
                    ItemCardTexts.UNKNOWN,
                )
                if item_card_text.text == ItemCardTexts.MELEE_SPEED.text:
                    return FilterFlags.WEAPON_MELEE.name

                if float(item_card["value"]):
                    if item_card_text.text == ItemCardTexts.ROF.text:
                        return FilterFlags.WEAPON_RANGED.name
                    if item_card_text.text == ItemCardTexts.RNG.text:
                        return FilterFlags.WEAPON_THROWN.name

        elif filter_flag_text == FilterFlags.ARMOR and self.current_health == -1:
            return FilterFlags.ARMOR_OUTFIT.name

        if filter_flag_text:
            return filter_flag_text.name

        return FilterFlags.UNKNOWN.name

    def process_item_name_and_type(self):
        if not self.filter_flag < 5:
            self.item_type = self.filter_flag_text
            self.plain_name = self.text
            return

        item_found = find_in_iter(
            lambda m: all(
                elem.lower() in self.text.lower().split()
                for elem in self.drop_unused_keywords(m["text"]).split()
            ),
            ITEM_TYPE_MAPPING,
        )

        if self.filter_flag_text == FilterFlags.ARMOR_OUTFIT.name:
            self.item_type = "ARMOR_OUTFIT"

        if item_found:
            if not self.item_type:
                self.item_type = item_found["type"]
            text = item_found["text"]
            text = text + " ".join(
                [
                    item
                    for item in self.text.split()
                    if item in ARMOR_LIMB_IDENTIFIER_STRINGS
                ]
            )
            self.plain_name = text

        if not self.item_type:
            self.item_type = "UNKNOWN"

    def drop_unused_keywords(self, str_text):
        return " ".join(
            [item for item in str_text.split(" ") if item not in UNUSED_ARMOR_KEYWORDS]
        )

    def process_armor_grade(self):
        armor_grade = find_in_iter(
            lambda m: m["helper"]
            == f"{self.damage_resistance}-{self.energy_resistance}-{self.radiation_resistance}",
            ARMOR_MAPPING,
        )
        if not armor_grade:
            return None
        self.armor_grade = armor_grade["armorGrade"]

    def process_item_card_entries(self):
        for item_card in self.item_card_entries:
            item_card = self.append_damage_on_item_card_entries(item_card)
            if item_card["text"] == ItemCardTexts.DESC.text:
                if self.is_legendary:
                    effects = self.process_legendary_effects(item_card)
                    for effect in effects:
                        if effect:
                            self.legendary_effects.append(effect)
                            if effect["star"] == 1:
                                self.one_star_effect = effect["texts"]["en"]
                            elif effect["star"] == 2:
                                self.two_star_effect = effect["texts"]["en"]
                            elif effect["star"] == 3:
                                self.three_star_effect = effect["texts"]["en"]
                else:
                    self.description = item_card["value"]

    def process_legendary_effects(self, item_card):
        effect_strings = item_card["value"].split("\n")
        effect_strings = [
            string.strip() for string in effect_strings if len(string.strip()) > 0
        ]
        effects = []
        for effect_string in effect_strings:

            if effect_string in SKIPPED_LEGENDARY_EFFECTS:
                continue

            if effect_string in LEGENDARY_REMAPPING:
                effect_string = LEGENDARY_REMAPPING[effect_string]

            effect = find_in_iter(
                lambda m: m["translations"]["en"] == effect_string, LEGENDARY_MAPPING
            )
            if not effect:
                print(item_card)
                print(effect_string)
                raise Exception
            effects.append(effect)
        if effects:
            return effects
        print(item_card)
        raise Exception

    def append_damage_on_item_card_entries(self, item_card):
        """
        Appends the field "damage_type_text" onto the item card
        """
        damage_type = next(
            (
                dmg_type
                for dmg_type in DamageTypes.ALL
                if item_card["damageType"] == dmg_type.type
            ),
            DamageTypes.UNKNOWN,
        )
        item_card["damage_type_text"] = damage_type.name

        if damage_type == DamageTypes.BALLISTIC:
            self.damage_resistance = item_card["value"]
        if damage_type == DamageTypes.ENERGY:
            self.energy_resistance = item_card["value"]
        if damage_type == DamageTypes.RADIATION:
            self.radiation_resistance = item_card["value"]

        return item_card

    def __iter__(self):
        yield "text", self.text,
        yield "server_handle_id", self.server_handle_id,
        yield "count", self.count,
        yield "item_value", self.item_value,
        yield "filter_flag", self.filter_flag,
        yield "current_health", self.current_health,
        yield "damage", self.damage,
        yield "durability", self.durability,
        yield "maximum_health", self.maximum_health,
        yield "weight", self.weight,
        yield "weapon_display_accuracy", self.weapon_display_accuracy,
        yield "weapon_display_rate_of_fire", self.weapon_display_rate_of_fire,
        yield "weapon_display_range", self.weapon_display_range,
        yield "num_legendary_stars", self.num_legendary_stars,
        yield "item_level", self.item_level,
        yield "rarity", self.rarity,
        yield "is_tradable", self.is_tradable,
        yield "is_spoiled", self.is_spoiled,
        yield "is_set_item", self.is_set_item,
        yield "is_quest_item", self.is_quest_item,
        yield "is_legendary", self.is_legendary,
        yield "vending_data", self.vending_data,
        yield "item_card_entries", self.item_card_entries,
        yield "mod_card_entries", self.mod_card_entries,
        yield "character", self.character,

        yield "legendary_effects", self.legendary_effects,
        yield "one_star_effect", self.one_star_effect,
        yield "two_star_effect", self.two_star_effect,
        yield "three_star_effect", self.three_star_effect,

        yield "item_type", self.item_type,
        yield "description", self.description,

        yield "armor_grade", self.armor_grade,
        yield "damage_resistance", self.damage_resistance,
        yield "energy_resistance", self.energy_resistance,
        yield "radiation_resistance", self.radiation_resistance,

        yield "filter_flag_text", self.filter_flag_text,

        yield "plain_name", self.plain_name,

    def __str__(self):
        return f"{dict(self)}"

    def __repr__(self):
        return f"{dict(self)}"
