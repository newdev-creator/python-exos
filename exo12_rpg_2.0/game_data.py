from constants import WeaponType, CharacterClass

INITIAL_CHARACTERS: dict[CharacterClass, dict[str, int]] = {
    CharacterClass.WARRIOR: {"name": "Guerrier", "health": 100, "strength": 15, "intelligence": 5, "magic": 0},
    CharacterClass.MAGE: {"name": "Magicien", "health": 80, "strength": 10, "intelligence": 18, "magic": 30},
    CharacterClass.THIEF: {"name": "Voleur", "health": 70, "strength": 8, "intelligence": 12, "magic": 10},
    CharacterClass.CLERIC: {"name": "Clérical", "health": 90, "strength": 12, "intelligence": 16, "magic": 30}
}

MONSTERS: list[dict] = [
    {
        "name": "Dragon de Glace",
        "stats": {"health": 85, "strength": 18, "intelligence": 14, "magic": 25},
        "weaknesses": [WeaponType.FIRE, WeaponType.LIGHTNING]
    },
    {
        "name": "Nécromancien",
        "stats": {"health": 60, "strength": 8, "intelligence": 20, "magic": 35},
        "weaknesses": [WeaponType.LIGHTNING, WeaponType.SWORD]
    },
    {
        "name": "Golem de Pierre",
        "stats": {"health": 120, "strength": 25, "intelligence": 5, "magic": 0},
        "weaknesses": [WeaponType.CLUB, WeaponType.CONJURING]
    },
    {
        "name": "Assassin des Ombres",
        "stats": {"health": 55, "strength": 22, "intelligence": 16, "magic": 10},
        "weaknesses": [WeaponType.FIRE, WeaponType.BOW]
    },
    {
        "name": "Esprit Vengeur",
        "stats": {"health": 45, "strength": 12, "intelligence": 18, "magic": 30},
        "weaknesses": [WeaponType.CONJURING, WeaponType.LIGHTNING]
    },
    {
        "name": "Berserker Orc",
        "stats": {"health": 95, "strength": 30, "intelligence": 6, "magic": 0},
        "weaknesses": [WeaponType.BOW, WeaponType.FIRE]
    },
    {
        "name": "Sorcier Corrompu",
        "stats": {"health": 70, "strength": 10, "intelligence": 22, "magic": 28},
        "weaknesses": [WeaponType.SWORD, WeaponType.CONJURING]
    },
    {
        "name": "Chimère",
        "stats": {"health": 100, "strength": 20, "intelligence": 12, "magic": 15},
        "weaknesses": [WeaponType.LIGHTNING, WeaponType.CLUB]
    },
    {
        "name": "Démon Mineur",
        "stats": {"health": 75, "strength": 16, "intelligence": 15, "magic": 20},
        "weaknesses": [WeaponType.CONJURING, WeaponType.SWORD]
    },
    {
        "name": "Titan de Givre",
        "stats": {"health": 110, "strength": 28, "intelligence": 8, "magic": 18},
        "weaknesses": [WeaponType.FIRE, WeaponType.CLUB]
    }
]

EVENTS: list[dict] = [
    {
        "message": "Une aura mystique vous enveloppe, amplifiant vos pouvoirs magiques",
        "attribute": "magic",
        "effect": 5
    },
    {
        "message": "L'air vicié de la caverne affaiblit votre corps",
        "attribute": "health",
        "effect": -8
    },
    {
        "message": "Un ancien grimoire vous révèle ses secrets",
        "attribute": "intelligence",
        "effect": 4
    },
    {
        "message": "Une bénédiction divine renforce votre vigueur",
        "attribute": "strength",
        "effect": 3
    },
    {
        "message": "Un piège magique explose, drainant votre énergie",
        "attribute": "magic",
        "effect": -6
    },
    {
        "message": "Une fontaine enchantée restaure vos forces",
        "attribute": "health",
        "effect": 12
    },
    {
        "message": "Un esprit maléfique tente de posséder votre esprit",
        "attribute": "intelligence",
        "effect": -5
    },
    {
        "message": "Un ancien autel renforce votre connexion avec la magie",
        "attribute": "magic",
        "effect": 8
    },
    {
        "message": "La fatigue commence à vous gagner",
        "attribute": "strength",
        "effect": -4
    },
    {
        "message": "Une vision prophétique aiguise votre esprit",
        "attribute": "intelligence",
        "effect": 6
    }
]
