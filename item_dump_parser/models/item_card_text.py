__all__ = ["ItemCardTexts"]


class ItemCardText:
    def __init__(self, card_display_text, card_input_text):
        self.text = card_input_text
        self.pretty_text = card_display_text

    def __iter__(self):
        yield "Text", self.text,
        yield "Pretty Text", self.pretty_text,

    def __str__(self):
        return f"{dict(self)}"

    def __repr__(self):
        return f"ICT({self.text}"


class ItemCardTexts:
    DR = ItemCardText("Damage reduction", "$dr")
    WEIGHT = ItemCardText("Weight", "$wt")
    VAL = ItemCardText("Value", "$val")
    DESC = ItemCardText("Description", "DESC")
    LEG_MODS = ItemCardText("Legendary Mods", "legendaryMods")
    PERCEPTION = ItemCardText("Perception", "PER")
    INT = ItemCardText("Intelligence", "INT")
    STR = ItemCardText("Strength", "STR")
    END = ItemCardText("Endurance", "END")
    AGI = ItemCardText("Agility", "AGI")
    CHR = ItemCardText("Charisma", "CHR")
    LCK = ItemCardText("Luck", "LCK")
    ROF = ItemCardText("Rate of fire", "$ROF")
    RNG = ItemCardText("Range", "$rng")
    ACC = ItemCardText("Accuracy", "$acc")
    DMG = ItemCardText("Damage", "$dmg")
    FOOD = ItemCardText("Food", "$Food")
    WATER = ItemCardText("Water", "$Water")
    RADS = ItemCardText("Rads", "Rads")
    HP = ItemCardText("HP", "HP")
    RAD_RESIST = ItemCardText("Rad Resist", "Rad Resist")
    MOVE_SPEED = ItemCardText("Move Speed", "Move Speed")
    DISEASE_CHANCE = ItemCardText("Disease Chance", "Disease Chance")
    AP = ItemCardText("Action point", "AP")
    MELEE_CRIT_DMG = ItemCardText("Melee Crit Dmg", "Melee Crit Dmg")
    BAT_CHARGE = ItemCardText("Battery charge", "$charge")
    POISON_RESIST = ItemCardText("Poison resist", "Poison Resist")
    DMG_RESIST = ItemCardText("Damage resist", "DMG Resist")
    RAD_INGESTION = ItemCardText("Rad Ingestion", "Rad Ingestion")
    MELEE_SPEED = ItemCardText("Melee speed", "$speed")
    BONUS_XP = ItemCardText("Bonus XP", "Bonus XP")
    DURABILITY = ItemCardText("Health/Durability", "$health")
    HP_REGEN = ItemCardText("Health Regen", "Health Regen")
    AP_REGEN = ItemCardText("AP Regen", "AP Regen")
    DMG_VS_YAO = ItemCardText("Dmg Vs Yao Guai", "Dmg Vs Yao Guai")
    MAX_HP = ItemCardText("Max HP", "Max HP")
    MAX_AP = ItemCardText("Max AP", "Max AP")
    DIS_RES = ItemCardText("Disease Resist", "Disease Resist")
    CARRY_WEIGHT = ItemCardText("Carry Weight", "Carry Weight")
    UNKNOWN = ItemCardText("", "")

    ALL = [
        DR,
        WEIGHT,
        VAL,
        DESC,
        LEG_MODS,
        PERCEPTION,
        INT,
        STR,
        END,
        AGI,
        CHR,
        LCK,
        ROF,
        RNG,
        ACC,
        DMG,
        FOOD,
        WATER,
        RADS,
        HP,
        RAD_RESIST,
        MOVE_SPEED,
        DISEASE_CHANCE,
        AP,
        MELEE_CRIT_DMG,
        BAT_CHARGE,
        POISON_RESIST,
        DMG_RESIST,
        RAD_INGESTION,
        MELEE_SPEED,
        BONUS_XP,
        DURABILITY,
        HP_REGEN,
        AP_REGEN,
        DMG_VS_YAO,
        MAX_HP,
        MAX_AP,
        DIS_RES,
        CARRY_WEIGHT,
        UNKNOWN,
    ]
