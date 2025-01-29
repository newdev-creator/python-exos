from enum import Enum, auto


class WeaponType(Enum):
    SWORD = "épée"
    CLUB = "massue"
    BOW = "arc"
    FIRE = "boule de feu"
    LIGHTNING = "éclair"
    CONJURING = "conjuration"


class CharacterClass(Enum):
    WARRIOR = auto()
    MAGE = auto()
    THIEF = auto()
    CLERIC = auto()


class CommandType(Enum):
    EXPLORE = "e"
    STATS = "s"
    POTION = "p"


WEAPONS_BY_CLASS = {
    CharacterClass.WARRIOR: [WeaponType.SWORD, WeaponType.CLUB, WeaponType.BOW],
    CharacterClass.MAGE: [WeaponType.FIRE, WeaponType.LIGHTNING, WeaponType.CONJURING],
    CharacterClass.THIEF: [WeaponType.SWORD, WeaponType.BOW, WeaponType.FIRE],
    CharacterClass.CLERIC: [WeaponType.CLUB, WeaponType.LIGHTNING, WeaponType.CONJURING]
}
