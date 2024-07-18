import random


# Player
class Character:
    def __init__(self, name: str, health: int, strength: int, intelligence: int, magie: int, weakness: str = None):
        self.name = name
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.magie = magie
        self.weakness = weakness

    def is_alive(self):
        return self.health > 0

    def take_damage_health(self, damage: int):
        self.health += damage

    def take_damage_strength(self, damage: int):
        self.strength += damage

    def take_damage_intelligence(self, damage: int):
        self.intelligence += damage

    def take_damage_magie(self, damage: int):
        self.magie += damage

    def physical_attack(self, other, weapon=None):
        if weapon == "sword" or "club" or "bow":
            damage = random.randint(0, self.strength)
        elif weapon == "fire" or "lightning" or "conjuring":
            damage = random.randint(0, self.magie)

        if other and other.weakness:
            if weapon in other.weakness:
                damage += 5
        other.take_damage_health(-damage)
        print(f"{self.name} blesse {other.name} pour {damage} dégat(s)!")

    def __str__(self):
        tableau = "| Nom      | Vie | Force | Intelligence | Magie |\n"
        tableau += "| -------- | --- | ----- | ------------ | ----- |\n"
        tableau += f"| {self.name} | {self.health} |   {self.strength}  |      {self.intelligence}      | {self.magie} |\n"
        return tableau


# Event
class Event:
    def __init__(self, message: str, attribut: str, malus: int):
        self.message = message
        self.attribut = attribut
        self.malus = malus


class Game:
    def __init__(self):
        self.monster = None
        characters = [
            {"name": "Guerrier", "health": 100, "strength": 15, "intelligence": 5, "magie": 0},
            {"name": "Magicien", "health": 80, "strength": 10, "intelligence": 18, "magie": 30},
            {"name": "Voleur  ", "health": 70, "strength": 8, "intelligence": 12, "magie": 10},
            {"name": "Clérical", "health": 90, "strength": 12, "intelligence": 16, "magie": 30}
        ]

        self.monsters = [
            {"name": "Goblin        ", "health": 20, "strength": 6, "intelligence": 3, "magie": 0,
             "weakness": ["conjuring", "sword"]},
            {"name": "Orc           ", "health": 30, "strength": 8, "intelligence": 4, "magie": 0,
             "weakness": ["conjuring", "club"]},
            {"name": "Troll         ", "health": 50, "strength": 12, "intelligence": 6, "magie": 0,
             "weakness": ["fire", "sword"]},
            {"name": "Dragonette    ", "health": 80, "strength": 18, "intelligence": 10, "magie": 0,
             "weakness": ["fire", "lightning"]},
            {"name": "Warlock       ", "health": 60, "strength": 15, "intelligence": 12, "magie": 0,
             "weakness": ["conjuring", "fire"]},
            {"name": "Giant Spider  ", "health": 40, "strength": 10, "intelligence": 8, "magie": 0,
             "weakness": ["fire", "club"]},
            {"name": "Zombie        ", "health": 25, "strength": 5, "intelligence": 1, "magie": 0,
             "weakness": ["fire", "club"]},
            {"name": "Vampire       ", "health": 70, "strength": 20, "intelligence": 15, "magie": 0,
             "weakness": ["fire", "lightning"]},
            {"name": "Werewolf      ", "health": 60, "strength": 25, "intelligence": 8, "magie": 0,
             "weakness": ["fire", "sword"]},
            {"name": "Witch         ", "health": 45, "strength": 10, "intelligence": 20, "magie": 15,
             "weakness": ["conjuring", "fire"]},
            {"name": "Skeleton      ", "health": 15, "strength": 5, "intelligence": 2, "magie": 0,
             "weakness": ["club", "fire"]},
            {"name": "Hydra         ", "health": 100, "strength": 30, "intelligence": 10, "magie": 0,
             "weakness": ["fire", "lightning"]},
            {"name": "Minotaur      ", "health": 80, "strength": 28, "intelligence": 8, "magie": 0,
             "weakness": ["sword", "fire"]},
            {"name": "Harpy         ", "health": 35, "strength": 12, "intelligence": 7, "magie": 0,
             "weakness": ["sword", "bow"]},
            {"name": "Banshee       ", "health": 40, "strength": 10, "intelligence": 18, "magie": 10,
             "weakness": ["conjuring", "lightning"]},
            {"name": "Lich          ", "health": 75, "strength": 15, "intelligence": 25, "magie": 20,
             "weakness": ["fire", "lightning"]},
            {"name": "Manticore     ", "health": 85, "strength": 20, "intelligence": 12, "magie": 0,
             "weakness": ["sword", "bow"]},
            {"name": "Cyclops       ", "health": 90, "strength": 35, "intelligence": 5, "magie": 0,
             "weakness": ["fire", "lightning"]},
            {"name": "Phoenix       ", "health": 60, "strength": 15, "intelligence": 18, "magie": 20,
             "weakness": ["lightning", "bow"]},
            {"name": "Griffin       ", "health": 70, "strength": 22, "intelligence": 10, "magie": 0,
             "weakness": ["sword", "bow"]}
        ]

        self.event = [
            {"message": "Des pierres tombent du plafond", "attribut": "health", "malus": -5},
            {"message": "Vous trouvez un bâton magique", "attribut": "intelligence", "malus": 2},
            {"message": "Vous trouvez une potion qui renforce votre magie", "attribut": "intelligence", "malus": 3},
            {"message": "Vous trouvez un objet de protection", "attribut": "health", "malus": 5},
            {"message": "Un piège se déclenche et vous blesse", "attribut": "health", "malus": -10},
            {"message": "Vous trouvez une épée légendaire", "attribut": "strength", "malus": 5},
            {"message": "Une tempête magique vous affaiblit", "attribut": "magie", "malus": -4},
            {"message": "Vous trouvez un grimoire ancien", "attribut": "intelligence", "malus": 4},
            {"message": "Un enchantement vous guérit", "attribut": "health", "malus": 8},
            {"message": "Vous trouvez un anneau de puissance", "attribut": "strength", "malus": 3},
            {"message": "Un ennemi invisible vous attaque", "attribut": "health", "malus": -7},
            {"message": "Vous trouvez une potion de force", "attribut": "strength", "malus": 4},
            {"message": "Une malédiction diminue votre intelligence", "attribut": "intelligence", "malus": -5},
            {"message": "Vous trouvez un talisman de sagesse", "attribut": "intelligence", "malus": 3},
            {"message": "Vous êtes frappé par un éclair magique", "attribut": "magie", "malus": -6},
            {"message": "Une bénédiction augmente votre magie", "attribut": "magie", "malus": 5},
            {"message": "Un éboulement vous blesse gravement", "attribut": "health", "malus": -15},
            {"message": "Vous trouvez une amulette de vigueur", "attribut": "health", "malus": 6},
            {"message": "Vous mangez un fruit magique", "attribut": "strength", "malus": 2},
            {"message": "Un esprit maléfique vous affaiblit", "attribut": "magie", "malus": -5},
            {"message": "Vous trouvez une rune de force", "attribut": "strength", "malus": 3},
            {"message": "Une flèche empoisonnée vous atteint", "attribut": "health", "malus": -8},
            {"message": "Un artefact augmente votre magie", "attribut": "magie", "malus": 4},
            {"message": "Vous trouvez une potion de guérison", "attribut": "health", "malus": 10}
        ]

        self.player_character = None

        tableau = "| Nom      | Vie | Force | Intelligence | Magie |\n"
        tableau += "| -------- | --- | ----- | ------------ | ----- |\n"
        for character in characters:
            tableau += f"| {character['name']} | {character['health']} |   {character['strength']}  |      {character['intelligence']}      | {character['magie']} |\n"

        print(tableau)

        player_choose = input(
            "Choisisez votre personnage : (g) guerrier, (m) magicien, (v) voleur, (c) clèrical").lower()

        while True:
            if player_choose == 'g':
                self.player_character = Character(characters[0]["name"], characters[0]["health"],
                                                  characters[0]["strength"], characters[0]["intelligence"],
                                                  characters[0]["magie"])
                break
            elif player_choose == 'm':
                self.player_character = Character(characters[1]["name"], characters[1]["health"],
                                                  characters[1]["strength"], characters[1]["intelligence"],
                                                  characters[1]["magie"])
                break
            elif player_choose == 'v':
                self.player_character = Character(characters[2]["name"], characters[2]["health"],
                                                  characters[2]["strength"], characters[2]["intelligence"],
                                                  characters[2]["magie"])
                break
            elif player_choose == 'c':
                self.player_character = Character(characters[3]["name"], characters[3]["health"],
                                                  characters[3]["strength"], characters[3]["intelligence"],
                                                  characters[3]["magie"])
                break
            else:
                print("Erreur dans la selection")
                exit(0)

        print("##################################")
        print(f"# Vous avez choissi un {self.player_character.name}. #")
        print("##################################")
        print("\n")

        self.start_game()

    def start_game(self):
        print("Bienvenu dans le défi fantastique : La montagne de feu")
        print("Vous pouvez explorer le labyrinthe : (e), regarder vos states : (s)")

        exit_score = 50
        current_score = 0

        while current_score < exit_score:
            command = input("> ").lower()

            if command == "e":
                current_score += 5
                random_event = random.choice(self.event)
                random_monster = random.randint(1, 9)

                if random_monster in [1, 2, 3]:
                    print(f"{random_event['message']}")

                    if random_event["attribut"] == "health":
                        self.player_character.take_damage_health(random_event["malus"])
                    elif random_event["attribut"] == "strength":
                        self.player_character.take_damage_strength(random_event["malus"])
                    elif random_event["attribut"] == "intelligence":
                        self.player_character.take_damage_intelligence(random_event["malus"])
                    elif random_event["attribut"] == "magie":
                        self.player_character.take_damage_magie(random_event["malus"])

                    print(
                        f"Votre {random_event['attribut']} est maintenant de {self.player_character.__getattribute__(random_event['attribut'])}")

                elif random_monster in [4, 5, 6]:
                    monster_index = random.randint(0, len(self.monsters) - 1)
                    self.monster = Character(self.monsters[monster_index]["name"],
                                             self.monsters[monster_index]["health"],
                                             self.monsters[monster_index]["strength"],
                                             self.monsters[monster_index]["intelligence"],
                                             self.monsters[monster_index]["magie"],
                                             self.monsters[monster_index]["weakness"])
                    print(f"Vous rencontrez un {self.monster.name.strip()}. Un combat s'engage !")

                    while True:
                        if self.player_character.is_alive():
                            if self.player_character.name == 'Guerrier':
                                attack = input(
                                    "Choisissez votre arme pour attaquer : Epée (e), Massue (m) ou Arc (a)").lower()
                                weapon_map = {'e': "sword", 'm': "club", 'a': "bow"}
                                if attack in weapon_map:
                                    weapon = weapon_map[attack]
                                    self.player_character.physical_attack(self.monster, weapon)
                                else:
                                    print("Erreur dans la selection de l'arme.")

                                self.monster.physical_attack(self.player_character)

                            elif self.player_character.name == 'Voleur  ':
                                attack = input(
                                    "Choisissez votre arme pour attaquer : Epée (e), Arc (a) ou Boule de feu (f)").lower()
                                weapon_map = {'e': "sword", 'f': "fire", 'a': "bow"}
                                if attack in weapon_map:
                                    weapon = weapon_map[attack]
                                    self.player_character.physical_attack(self.monster, weapon)
                                else:
                                    print("Erreur dans la selection de l'arme.")

                                self.monster.physical_attack(self.player_character)

                            elif self.player_character.name == 'Magicien':
                                attack = input(
                                    "Choisissez votre arme pour attaquer : Boule de feu (f), Foudre (l) ou Conjuration (c)").lower()
                                weapon_map = {'f': "fire", 'l': "lightning", 'c': "conjuring"}
                                if attack in weapon_map:
                                    weapon = weapon_map[attack]
                                    self.player_character.physical_attack(self.monster, weapon)
                                else:
                                    print("Erreur dans la selection de l'arme.")

                                self.monster.physical_attack(self.player_character)

                            elif self.player_character.name == 'Clérical':
                                attack = input(
                                    "Choisissez votre arme pour attaquer : Massue (m), Foudre (l) ou Conjuration (c)").lower()
                                weapon_map = {'m': "club", 'l': "lightning", 'c': "conjuring"}
                                if attack in weapon_map:
                                    weapon = weapon_map[attack]
                                    self.player_character.physical_attack(self.monster, weapon)
                                else:
                                    print("Erreur dans la selection de l'arme.")

                                self.monster.physical_attack(self.player_character)

                            if not self.monster.is_alive():
                                print(f"Le {self.monster.name} est mort.")
                                break
                        else:
                            print(f"Le {self.player_character.name} est mort.")
                            break

                elif random_monster in [7, 8, 9]:
                    print("Vous avancez prudement")

            elif command == "s":
                print(str(self.player_character))
            else:
                print("Erreur, essayez encore")
            print("Vous pouvez explorer le labyrinthe : (e), regarder vos states : (s)")

        print("\n")
        print("##################################")
        print("Vous voyez enfin la sortie !!!")
        print("Bravo !!! Vous avez survécu à la montagne de feu !")
        print("##################################")
        print(str(self.player_character))


###############
game = Game()
