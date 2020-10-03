from item_dump_parser.utils import load_json

FED76_MAPPING_URL = "https://fed76.info/pricing/mapping"

AMMO_MAPPING = load_json("resources/ammo.types.json")
ARMOR_MAPPING = load_json("resources/armor.config.json")
ITEM_TYPE_MAPPING = load_json("resources/itemTypes.config.json")
LEGENDARY_MAPPING = load_json("resources/legendaryMods.config.json")
NAME_MODS_MAPPING = load_json("resources/name.modifiers.json")

ARMOR_LIMB_IDENTIFIER_STRINGS = {"arm", "leg", "chest", "left", "right", "mask"}

UNUSED_KEYWORDS = ["Rifle"]

KEYWORD_REMAPPING = {
    "50 Cal": ".50 Cal",
    "Wood": "Wooden",
    "Lever Action": "Lever-Action",
    "Experimental MIRV": "Fat Man",
}

MY_STUPID_NAMES_FOR_ITEMS_I_OWN = {
    "(DNS) Sledge No Hammer": {
        "type": "WEAPON_MELEE",
        "text": "Sledge No Hammer",
        "abbreviation": "sledgehammer",
    },
    "(.DNS) CONFETTI 4 ALL": {
        "type": "WEAPON_RANGED",
        "text": "DEVROOM PISTOL",
        "abbreviation": "10mm",
    },
    "(DNS) Combat No Knife": {
        "type": "WEAPON_MELEE",
        "text": "Combat No Knife",
        "abbreviation": "combatknife",
    },
    "(.DNS) Radiator": {
        "type": "WEAPON_RANGED",
        "text": "Radium Rifle",
        "abbreviation": "radium",
    },
    "(Armor) SS Chest": {
        "type": "ARMOR",
        "text": "Secret Service Armor",
        "abbreviation": "secretservice",
    },
    "(Armor) SS L Arm": {
        "type": "ARMOR",
        "text": "Secret Service Armor",
        "abbreviation": "secretservice",
    },
    "(Armor) SS R Arm": {
        "type": "ARMOR",
        "text": "Secret Service Armor",
        "abbreviation": "secretservice",
    },
    "(Armor) SS L Leg": {
        "type": "ARMOR",
        "text": "Secret Service Armor",
        "abbreviation": "secretservice",
    },
    "(Armor) SS R Leg": {
        "type": "ARMOR",
        "text": "Secret Service Armor",
        "abbreviation": "secretservice",
    },
    "(DNS) LA Rifle": {
        "type": "WEAPON_RANGED",
        "text": "Lever-Action Rifle",
        "abbreviation": "lever",
    },
    "(DNS) Shotgun": {
        "type": "WEAPON_RANGED",
        "text": "Pump Action Shotgun",
        "abbreviation": "pump",
    },
    "The V.A.T.S. Unknown": {
        "type": "WEAPON_RANGED",
        "text": "Alien Blaster",
        "abbreviation": "alienblaster",
    },
    "Slug Buster": {
        "type": "WEAPON_RANGED",
        "text": "Plasma Gun",
        "abbreviation": "plasma",
    },
    "[GOD] DB Shotgun": {
        "type": "WEAPON_RANGED",
        "text": "Double-barrel shotgun",
        "abbreviation": "doublebarrel",
    },
}

HACKED_BULLSHIT = [
    "The Captain's Hat",
    "Lucky Rabbit's Foot",
    "Orbital Strike",
    "(DNS) Beth Fix Cripple;_;",
    "(DNS) Handmade",
    "(DNS) Minigun-gun",
    "Bloodied Animatronic Alien Blaster",
]

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
    "Gain +5% accuracy with guns",
}

OUTPUT_STRING_FORMAT = "{0.plain_name}\t{0.item_level}\t{0.one_star_effect}\t{0.two_star_effect}\t{0.three_star_effect}\t\t\t\t\t\t{0.character}"

OUPUT_ONLY_NEW = True
