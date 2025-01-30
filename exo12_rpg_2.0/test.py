import random
from enum import Enum, auto
from dataclasses import dataclass


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


# ===================================================================================================================
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


# ===================================================================================================================
@dataclass
class Stats:
    health: int
    strength: int
    intelligence: int
    magic: int

    def modify_stat(self, attribute: str, value: int) -> None:
        current = getattr(self, attribute)
        setattr(self, attribute, current + value)


@dataclass
class Character:
    name: str
    stats: Stats
    weaknesses: list[WeaponType] | None = None
    potions: int = 5

    def is_alive(self) -> bool:
        return self.stats.health > 0

    def take_damage(self, damage: int) -> None:
        self.stats.health -= damage

    def use_potion(self) -> bool:
        if self.potions > 0:
            healing = random.randint(15, 50)
            self.stats.health += healing
            self.potions -= 1
            print(f"{self.name} utilise une potion et récupère {healing} points de vie!")
            print(f"Il reste {self.potions} potion(s)")
            return True
        print("Plus de potions disponibles!")
        return False

    def attack(self, target: 'Character', weapon: WeaponType) -> None:
        match weapon:
            case WeaponType.SWORD | WeaponType.CLUB | WeaponType.BOW:
                damage = random.randint(0, self.stats.strength)
            case WeaponType.FIRE | WeaponType.LIGHTNING | WeaponType.CONJURING:
                damage = random.randint(0, self.stats.magic)

        if target.weaknesses and weapon in target.weaknesses:
            damage += 5

        target.take_damage(damage)
        print(f"{self.name} blesse {target.name} pour {damage} dégât(s)!")

    def __str__(self) -> str:
        return (
            "| Nom      | Vie | Force | Intelligence | Magie | Potions |\n"
            "| -------- | --- | ----- | ------------ | ----- | ------- |\n"
            f"| {self.name:<8} | {self.stats.health:>3} | {self.stats.strength:>5} | "
            f"{self.stats.intelligence:>12} | {self.stats.magic:>5} | {self.potions:>7} |"
        )


@dataclass
class Event:
    message: str
    attribute: str
    effect: int


# ===================================================================================================================
class Game:
    def __init__(self) -> None:
        self.player: Character | None = None
        self.current_monster: Character | None = None
        self.setup_game()

    def setup_game(self) -> None:
        self._display_character_selection()
        self._select_character()
        print(f"\n{'#' * 34}")
        print(f"# Vous avez choisi un {self.player.name}. #")
        print(f"{'#' * 34}\n")
        self.start_game()

    @staticmethod
    def _display_character_selection() -> None:
        print("| Nom      | Vie | Force | Intelligence | Magie |")
        print("| -------- | --- | ----- | ------------ | ----- |")
        for char_data in INITIAL_CHARACTERS.values():
            print(f"| {char_data['name']:<8} | {char_data['health']:>3} | "
                  f"{char_data['strength']:>5} | {char_data['intelligence']:>12} | "
                  f"{char_data['magic']:>5} |")

    def _select_character(self) -> None:
        char_map = {
            'g': CharacterClass.WARRIOR,
            'm': CharacterClass.MAGE,
            'v': CharacterClass.THIEF,
            'c': CharacterClass.CLERIC
        }

        while True:
            choice = input("Choisissez votre personnage : (g) guerrier, (m) magicien, "
                           "(v) voleur, (c) clérical\n").lower()

            if choice in char_map:
                char_class = char_map[choice]
                char_data = INITIAL_CHARACTERS[char_class]
                self.player = Character(
                    # Obligé de passer la fonction str(), sinon PyCharm léve une erreur.
                    name=str(char_data['name']),
                    stats=Stats(
                        health=char_data['health'],
                        strength=char_data['strength'],
                        intelligence=char_data['intelligence'],
                        magic=char_data['magic']
                    )
                )
                break
            print("Erreur dans la sélection")

    def handle_combat(self) -> None:
        if not (self.player and self.current_monster):
            return

        while True:
            if not self.player.is_alive():
                print(f"Le {self.player.name} est mort.")
                break

            # Options de combat
            print("\nQue souhaitez-vous faire ?")
            print("(1) Attaquer")
            print("(2) Prendre une potion")
            action = input("> ")

            match action:
                case "1":
                    # Gestion de l'attaque du joueur
                    weapons = WEAPONS_BY_CLASS[self._get_player_class()]
                    weapon_choices = {str(i): weapon for i, weapon in enumerate(weapons, 1)}

                    print("\nChoisissez votre arme:")
                    for key, weapon in weapon_choices.items():
                        print(f"({key}) {weapon.value}")

                    choice = input("> ")
                    if choice in weapon_choices:
                        self.player.attack(self.current_monster, weapon_choices[choice])
                    else:
                        print("Erreur dans la sélection de l'arme.")
                        continue

                case "2":
                    if self.player.use_potion():
                        print(f"Points de vie actuels : {self.player.stats.health}")
                    else:
                        continue  # Si pas de potion disponible, on recommence le tour

                case _:
                    print("Action non valide")
                    continue

            if not self.current_monster.is_alive():
                print(f"Le {self.current_monster.name} est mort.")
                # Chance de trouver une potion après un combat
                if random.random() < 0.05:  # 5% de chance
                    self.player.potions += 1
                    print("Vous avez trouvé une potion sur le corps du monstre!")
                break

            # Attaque du monstre
            monster_weapon = random.choice(list(WeaponType))
            self.current_monster.attack(self.player, monster_weapon)

    def _get_player_class(self) -> CharacterClass:
        for char_class, data in INITIAL_CHARACTERS.items():
            if data['name'] == self.player.name:
                return char_class
        raise ValueError("Invalid player class")

    def start_game(self) -> None:
        print("Bienvenue dans le défi fantastique : La montagne de feu")
        print("Vous pouvez explorer le labyrinthe : (e), regarder vos stats : (s), prendre une potion : (p)")

        current_score = 0
        exit_score = 50

        while current_score < exit_score and self.player.is_alive():
            command = input("> ").lower()

            match command:
                case CommandType.EXPLORE.value:
                    current_score += 5
                    self._handle_exploration()
                case CommandType.STATS.value:
                    print(str(self.player))
                case CommandType.POTION.value:
                    if self.player.use_potion():
                        print(f"Points de vie actuels : {self.player.stats.health}")
                case _:
                    print("Erreur, essayez encore")
                    continue

            if self.player.is_alive():
                print("\nVous pouvez explorer le labyrinthe : (e), regarder vos stats : (s), prendre une potion : (p)")
        if self.player.is_alive():
            self._display_victory_message()

    def _handle_exploration(self) -> None:
        event_type = random.randint(1, 100)
        if event_type <= 2:
            # 2% de chance de trouver une potion pendant l'exploration
            self.player.potions += 1
            print("Vous avez trouvé une potion!")
        else:
            event_type = random.randint(1, 9)
            match event_type:
                case n if n <= 3:
                    self._handle_random_event()
                case n if n <= 6:
                    self._handle_monster_encounter()
                case n if n <= 9:
                    print("Vous avancez prudemment")

    def _handle_random_event(self) -> None:
        event = random.choice(EVENTS)
        print(event["message"])
        self.player.stats.modify_stat(event["attribute"], event["effect"])
        print(f"Votre {event['attribute']} est maintenant de "
              f"{getattr(self.player.stats, event['attribute'])}")

    def _handle_monster_encounter(self) -> None:
        monster_data = random.choice(MONSTERS)
        self.current_monster = Character(
            name=monster_data["name"],
            stats=Stats(**monster_data["stats"]),
            weaknesses=monster_data["weaknesses"]
        )
        print(f"Vous rencontrez un {self.current_monster.name}. Un combat s'engage !")
        self.handle_combat()

    def _display_victory_message(self) -> None:
        print("\n" + "#" * 34)
        print("Vous voyez enfin la sortie !!!")
        print("Bravo !!! Vous avez survécu à la montagne de feu !")
        print("#" * 34)
        print(str(self.player))

# ===================================================================================================================


if __name__ == "__main__":
    game = Game()
