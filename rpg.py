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
    potions: int = 3  # Chaque personnage commence avec 3 potions
    
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

# game.py class (modifications principales)
class Game:
    def __init__(self) -> None:
        self.player: Optional[Character] = None
        self.current_monster: Optional[Character] = None
        self.setup_game()

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
                if random.random() < 0.3:  # 30% de chance
                    self.player.potions += 1
                    print("Vous avez trouvé une potion sur le corps du monstre!")
                break

            # Attaque du monstre
            monster_weapon = random.choice(list(WeaponType))
            self.current_monster.attack(self.player, monster_weapon)

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

    def _handle_exploration(self) -> None:
        event_type = random.randint(1, 9)
        match event_type:
            case n if n <= 3:
                self._handle_random_event()
            case n if n <= 6:
                self._handle_monster_encounter()
            case n if n <= 8:
                print("Vous avancez prudemment")
            case _:
                # 10% de chance de trouver une potion pendant l'exploration
                self.player.potions += 1
                print("Vous avez trouvé une potion!")