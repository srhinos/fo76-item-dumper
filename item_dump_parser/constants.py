from item_dump_parser.utils import load_json

FED76_MAPPING_URL = "https://fed76.info/pricing/mapping"

AMMO_MAPPING = load_json("resources/ammo.types.json")
ARMOR_MAPPING = load_json("resources/armor.config.json")
ITEM_TYPE_MAPPING = load_json("resources/itemTypes.config.json")
LEGENDARY_MAPPING = load_json("resources/legendaryMods.config.json")
NAME_MODS_MAPPING = load_json("resources/name.modifiers.json")

ARMOR_LIMB_IDENTIFIER_STRINGS = {"arm", "leg", "chest", "left", "right", "mask"}

UNUSED_ARMOR_KEYWORDS = ["armor"]

LEGENDARY_REMAPPING = {
    "Bullets explode on impact doing 15 points area effect damage.": "Bullets explode for area damage."
}

SKIPPED_LEGENDARY_EFFECTS = {
    "SET BONUS (1/5): Melee targets and melee attackers bleed. Harder to detect while sneaking.",
    "SET BONUS (2/5): Melee targets and melee attackers bleed. Harder to detect while sneaking.",
    "SET BONUS (3/5): Melee targets and melee attackers bleed. Harder to detect while sneaking.",
    "SET BONUS (4/5): Melee targets and melee attackers bleed. Harder to detect while sneaking.",
    "SET BONUS (5/5): Melee targets and melee attackers bleed. Harder to detect while sneaking.",
    "Target is poisoned for 50 damage over 10 seconds",
}

OUTPUT_STRING_FORMAT = "{0.plain_name}\t{0.item_level}\t{0.one_star_effect}\t{0.two_star_effect}\t{0.three_star_effect}\t\t\t\t\t\t{0.character}"
