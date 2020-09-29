__all__ = ["DamageTypes"]


class DamageType:
    def __init__(self, dmg_type, dmg_name):
        self.type = dmg_type
        self.name = dmg_name

    def __iter__(self):
        yield "Name", self.name,
        yield "Type", self.type,

    def __str__(self):
        return f"{dict(self)}"

    def __repr__(self):
        return f"DMG({self.name} {self.type}"

    def __eq__(self, o: object):
        if isinstance(object, DamageType):
            return self.text == object.text
        elif isinstance(object, str):
            return self.text == object


class DamageTypes:
    NOTHING = DamageType(0, "Nothing")
    BALLISTIC = DamageType(1, "Ballistic")
    WATER = DamageType(2, "Water")
    FLAG_3 = DamageType(3, "")
    ENERGY = DamageType(4, "Energy")
    FLAG_5 = DamageType(5, "")
    RADIATION = DamageType(6, "Radiation")
    AMMO = DamageType(10, "Ammo")
    UNKNOWN = DamageType(0, "Unknown")

    ALL = [
        NOTHING,
        BALLISTIC,
        WATER,
        FLAG_3,
        ENERGY,
        FLAG_5,
        RADIATION,
        AMMO,
        UNKNOWN,
    ]
