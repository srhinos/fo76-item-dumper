from item_dump_parser.utils import load_json

FED76_MAPPING_URL = "https://fed76.info/pricing/mapping"

FED76_PRICING_URL = "https://fed76.info/pricing-api/"

ALERT_ON_WEB_REQUESTS = True

AMMO_MAPPING = load_json("resources/ammo.types.json")
ARMOR_MAPPING = load_json("resources/armor.config.json")
ITEM_TYPE_MAPPING = load_json("resources/itemTypes.config.json")
LEGENDARY_MAPPING = load_json("resources/legendaryMods.config.json")
NAME_MODS_MAPPING = load_json("resources/name.modifiers.json")

ARMOR_LIMB_IDENTIFIER_STRINGS = {"arm", "leg", "chest", "left", "right", "mask"}

ARMOR_META_IDENTIFIER_STRINGS = {"urban", "forest"}

UNUSED_KEYWORDS = ["Rifle"]

FILTERED_STRINGS = ["Armor"]

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
    "(DNS) Combat No Knife": {
        "type": "WEAPON_MELEE",
        "text": "Combat Knife",
        "abbreviation": "combatknife",
    },
    "(.DNS) CONFETTI 4 ALL": {
        "type": "WEAPON_RANGED",
        "text": "DEVROOM PISTOL",
        "abbreviation": "10mm",
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
    "[GOD] Gauntlet": {
        "type": "WEAPON_MELEE",
        "text": "Bullion Gauntlet",
        "abbreviation": "bullgauntlet",
    },
}

HACKED_BULLSHIT = {
    "The Captain's Hat": "ARMOR",
    "Lucky Rabbit's Foot": "WEAPON",
    "Orbital Strike": "WEAPON",
    "(DNS) Beth Fix Cripple;_;": "WEAPON",
    "(DNS) Handmade": "WEAPON",
    "(DNS) Minigun-gun": "WEAPON",
    "Bloodied Animatronic Alien Blaster": "WEAPON",
}

LEGENDARY_REMAPPING = {
    "Bullets explode on impact doing 15 points area effect damage.": "Bullets explode for area damage."
}

OUTPUT_STRING_FORMAT = "{0.plain_name}\t{0.item_level}\t{0.one_star_effect_str}\t{0.two_star_effect_str}\t{0.three_star_effect_str}\t\t\t\t\t\t{0.character}\t{0.fed76_value}"

OUPUT_ONLY_NEW = True
