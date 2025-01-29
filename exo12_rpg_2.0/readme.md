# La Montagne de Feu - Jeu de Rôle Textuel 🗡️🔥

## Description
La Montagne de Feu est un jeu de rôle textuel en Python où vous incarnez un héros dans un donjon fantastique. Explorez des salles mystérieuses, affrontez des créatures dangereuses et tentez de survivre aux pièges mortels.

## Caractéristiques
- 4 classes de personnages jouables : Guerrier, Magicien, Voleur et Clérical
- 10 types de monstres uniques avec leurs propres forces et faiblesses
- Système de combat stratégique avec différentes armes
- Système de potions pour la guérison
- Événements aléatoires qui influencent vos statistiques
- Interface en ligne de commande intuitive

## Prérequis
- Python 3.10 ou supérieur
- Aucune dépendance externe requise


## Comment jouer

### Classes disponibles
- **Guerrier** : Fort et résistant (Armes : Épée, Massue, Arc)
- **Magicien** : Puissant en magie (Armes : Boule de feu, Éclair, Conjuration)
- **Voleur** : Agile et polyvalent (Armes : Épée, Arc, Boule de feu)
- **Clérical** : Équilibré (Armes : Massue, Éclair, Conjuration)

### Commandes
- `e` : Explorer le donjon
- `s` : Afficher vos statistiques
- `p` : Utiliser une potion de soin

### Combat
Pendant les combats, vous pouvez :
1. Attaquer avec votre arme
2. Utiliser une potion de soin

### Points clés
- Chaque personnage commence avec 3 potions
- Les potions restaurent entre 15 et 50 points de vie
- Possibilité de trouver des potions en explorant ou en battant des monstres
- Différents événements peuvent affecter vos statistiques
- Les monstres ont des faiblesses spécifiques à exploiter

## Structure du Projet
```
montagne-de-feu/
├── main.py
├── constants.py
├── models.py
├── game.py
└── game_data.py
```

## Objectif
Atteignez la sortie du donjon en accumulant suffisamment de points d'exploration (50 points) tout en restant en vie !
