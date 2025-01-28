# constants.py
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Dict, Optional

class WeaponType(Enum):
    SWORD = "sword"
    CLUB = "club"
    BOW = "bow"
    FIRE = "fire"
    LIGHTNING = "lightning"
    CONJURING = "conjuring"

class CharacterClass(Enum):
    WARRIOR = auto()
    MAGE = auto()
    THIEF = auto()
    CLERIC = auto()

WEAPONS_BY_CLASS = {
    CharacterClass.WARRIOR: [WeaponType.SWORD, WeaponType.CLUB, WeaponType.BOW],
    CharacterClass.MAGE: [WeaponType.FIRE, WeaponType.LIGHTNING, WeaponType.CONJURING],
    CharacterClass.THIEF: [WeaponType.SWORD, WeaponType.BOW, WeaponType.FIRE],
    CharacterClass.CLERIC: [WeaponType.CLUB, WeaponType.LIGHTNING, WeaponType.CONJURING]
}

# models.py
from dataclasses import dataclass
from typing import Optional, List, ClassVar
import random
from constants import WeaponType

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
    weaknesses: Optional[List[WeaponType]] = None
    
    def is_alive(self) -> bool:
        return self.stats.health > 0

    def take_damage(self, damage: int) -> None:
        self.stats.health -= damage

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
            "| Nom      | Vie | Force | Intelligence | Magie |\n"
            "| -------- | --- | ----- | ------------ | ----- |\n"
            f"| {self.name:<8} | {self.stats.health:>3} | {self.stats.strength:>5} | "
            f"{self.stats.intelligence:>12} | {self.stats.magic:>5} |"
        )

@dataclass
class Event:
    message: str
    attribute: str
    effect: int

# game_data.py
from typing import Dict, List
from constants import WeaponType, CharacterClass

INITIAL_CHARACTERS: Dict[CharacterClass, Dict[str, int]] = {
    CharacterClass.WARRIOR: {"name": "Guerrier", "health": 100, "strength": 15, "intelligence": 5, "magic": 0},
    CharacterClass.MAGE: {"name": "Magicien", "health": 80, "strength": 10, "intelligence": 18, "magic": 30},
    CharacterClass.THIEF: {"name": "Voleur", "health": 70, "strength": 8, "intelligence": 12, "magic": 10},
    CharacterClass.CLERIC: {"name": "Clérical", "health": 90, "strength": 12, "intelligence": 16, "magic": 30}
}

MONSTERS: List[Dict] = [
    {
        "name": "Goblin",
        "stats": {"health": 20, "strength": 6, "intelligence": 3, "magic": 0},
        "weaknesses": [WeaponType.CONJURING, WeaponType.SWORD]
    },
    # ... (autres monstres)
]

EVENTS: List[Dict] = [
    {
        "message": "Des pierres tombent du plafond",
        "attribute": "health",
        "effect": -5
    },
    # ... (autres événements)
]

# game.py
from typing import Optional
import random
from models import Character, Stats, Event
from constants import CharacterClass, WeaponType, WEAPONS_BY_CLASS
from game_data import INITIAL_CHARACTERS, MONSTERS, EVENTS

class Game:
    def __init__(self) -> None:
        self.player: Optional[Character] = None
        self.current_monster: Optional[Character] = None
        self.setup_game()

    def setup_game(self) -> None:
        self._display_character_selection()
        self._select_character()
        print(f"\n{'#' * 34}")
        print(f"# Vous avez choisi un {self.player.name}. #")
        print(f"{'#' * 34}\n")
        self.start_game()

    def _display_character_selection(self) -> None:
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
                    name=char_data['name'],
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

            if not self.current_monster.is_alive():
                print(f"Le {self.current_monster.name} est mort.")
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
        print("Vous pouvez explorer le labyrinthe : (e), regarder vos stats : (s)")

        current_score = 0
        exit_score = 50

        while current_score < exit_score and self.player.is_alive():
            command = input("> ").lower()

            match command:
                case "e":
                    current_score += 5
                    self._handle_exploration()
                case "s":
                    print(str(self.player))
                case _:
                    print("Erreur, essayez encore")
                    continue

            if self.player.is_alive():
                print("\nVous pouvez explorer le labyrinthe : (e), regarder vos stats : (s)")

        if self.player.is_alive():
            self._display_victory_message()

    def _handle_exploration(self) -> None:
        event_type = random.randint(1, 9)
        match event_type:
            case n if n <= 3:
                self._handle_random_event()
            case n if n <= 6:
                self._handle_monster_encounter()
            case _:
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

# main.py
if __name__ == "__main__":
    game = Game()