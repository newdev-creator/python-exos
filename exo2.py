import random

def roll():
  min_value = 1
  max_value = 6
  roll = random.randint(min_value, max_value)
  
  return roll
  
while True:
  players = input("Entrez un nombre de joueurs (2 - 4): ")
  if players.isdigit():
    players = int(players)
    if 2 <= players <= 4:
      break
    else:
      print("Vous devez choisir entre 2 et 4 joueurs.")
  else:
    print("Erreur, essayez encore.")
    
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
  for player_i in range(players):
    print("Joueur numéro", player_i + 1, "votre tour demarre !")
    print("Votre score est de : ", player_scores[player_i])
    current_score = 0
    
    while True:
      should_roll = input("Voulez vous jeter les dés ? (y) ")
      if should_roll.lower() != "y":
        break
      
      value = roll()
      if value == 1:
        print("Vos obtenez 1 ! Fin du tour !")
        current_score = 0
        break
      else:
        current_score += value
        print("Vous obtenez : ", value)
        
      print("Votre score est de : ", current_score)
      
    player_scores[player_i] += current_score
    print("Votre score total est de : ", player_scores[player_i])
    
max_score = max(player_scores)
winning_i = player_scores.index(max_score)
print("Joueur numéro : ", winning_i + 1, "est le gagnant avec un score de : ", max_score)