import logging

log = logging.getLogger(__name__)


__all__ = ["FilterFlags"]


class FilterFlag:
    def __init__(self, flag_name, has_stars=False, subtypes=[], *flags):
        self.name = flag_name
        self.has_stars = has_stars
        self.subtypes = subtypes
        try:
            self.flags = [int(flag) for flag in flags]
        except ValueError:
            log.error(
                f"Value Error: {self.name} cannot be initialized with flags: {flags}"
            )

    def __iter__(self):
        yield "Name", self.name,
        yield "HasStars", self.has_stars,
        yield "Subtypes", self.subtypes,
        yield "Flags", self.flags,

    def __str__(self):
        return f"{dict(self)}"

    def __repr__(self):
        return f"FF({self.name} {self.has_stars}{' ' if self.flags else ''}{'-'.join([str(v) for v in self.flags])}"


class FilterFlags:
    POWER_ARMOR = FilterFlag("Power Armor", 0)
    WEAPON_MELEE = FilterFlag("Weapon - Melee", True)
    WEAPON_RANGED = FilterFlag("Weapon - Ranged", True)
    WEAPON_THROWN = FilterFlag("Weapon - Thrown")
    WEAPON = FilterFlag(
        "Weapon", True, [WEAPON_MELEE, WEAPON_RANGED, WEAPON_THROWN], 2, 3,
    )
    ARMOR_OUTFIT = FilterFlag("Armor - Outfit")
    ARMOR = FilterFlag("Armor", True, [ARMOR_OUTFIT], 4)
    AID = FilterFlag("Aid", 8, 9)
    HOLO = FilterFlag("Holo", 512)
    AMMO = FilterFlag("Ammo", 4096)
    NOTES = FilterFlag("Notes", 128, 8192)
    MISC = FilterFlag("Misc", 33280)
    MODS = FilterFlag("Mods", 2048)
    JUNK = FilterFlag("Junk", 33792, 1024)
    UNKNOWN = FilterFlag("Unknown")

    ALL = [
        POWER_ARMOR,
        WEAPON_MELEE,
        WEAPON_RANGED,
        WEAPON_THROWN,
        WEAPON,
        ARMOR_OUTFIT,
        ARMOR,
        AID,
        HOLO,
        AMMO,
        NOTES,
        MISC,
        MODS,
        JUNK,
        UNKNOWN,
    ]
