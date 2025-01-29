import random

from constants import CharacterClass, WeaponType, WEAPONS_BY_CLASS, CommandType
from game_data import INITIAL_CHARACTERS, MONSTERS, EVENTS
from models import Character, Stats


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

