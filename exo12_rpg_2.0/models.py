import random
from dataclasses import dataclass

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
