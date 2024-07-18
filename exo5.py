import random


# Player
class Character:
    def __init__(self, name: str, health: int, strength: int, intelligence: int, magie: int):
        self.name = name
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.magie = magie

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

    def physical_attack(self, other):
        damage = random.randint(0, self.strength)
        other.take_damage(damage)
        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def magic_attack(self, other):
        damage = random.randint(0, self.magie)
        other.take_damage(damage)
        print(f"{self.name} attacks {other.name} for {damage} damage!")

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
        characters = [
            {"name": "Guerrier", "health": 100, "strength": 15, "intelligence": 5, "magie": 0},
            {"name": "Magicien", "health": 80, "strength": 10, "intelligence": 18, "magie": 30},
            {"name": "Voleur  ", "health": 70, "strength": 8, "intelligence": 12, "magie": 10},
            {"name": "Clérical", "health": 90, "strength": 12, "intelligence": 16, "magie": 30}
        ]

        self.monsters = [
            {"name": "Goblin      ", "health": 20, "strength": 6, "intelligence": 3, "magie": 0},
            {"name": "Orc         ", "health": 30, "strength": 8, "intelligence": 4, "magie": 0},
            {"name": "Troll       ", "health": 50, "strength": 12, "intelligence": 6, "magie": 0},
            {"name": "Dragonette  ", "health": 80, "strength": 18, "intelligence": 10, "magie": 0},
            {"name": "Warlock     ", "health": 60, "strength": 15, "intelligence": 12, "magie": 0},
            {"name": "Giant Spider", "health": 40, "strength": 10, "intelligence": 8, "magie": 0}
        ]

        self.event = [
            {"message": "Des pierres tombent du plafond", "attribut": "health", "malus": -5},
            {"message": "Vous trouver un bâton magique", "attribut": "intelligence", "malus": 2},
            {"message": "Vous trouver une potion qui renforce votre magie", "attribut": "intelligence", "malus": 3},
            {"message": "Vous trouver un objet de protection", "attribut": "health", "malus": 5},
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

        print(f"Vous avez choissi un {self.player_character.name}.")

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

                    monster_index = random.randint(0, len(self.monsters))
                    monster = self.monsters[monster_index]

                    print(monster)




                elif random_monster in [7, 8, 9]:
                    print("Vous avancez prudement")

            elif command == "s":
                print(str(self.player_character))
            else:
                print("Erreur, essayez encore")


###############
game = Game()
