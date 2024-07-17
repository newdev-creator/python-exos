import re


def create_produit():
    panier = []

    while True:
        produit = {
            "qt": None,
            "nom": None,
            "prix": None
        }

        produit_nom = input("quel produit vous mettez dans votre panier ? : ")
        if produit_nom.isdigit():
            print("Erreur : le nom du produit ne peut pas être un nombre.")
        else:
            produit["nom"] = produit_nom

        produit_qt = input("combien en prenez-vous ? : ")
        if produit_qt.isdigit():
            # on convertit en entier
            produit["qt"] = int(produit_qt)
        else:
            print("Erreur : le nombre de quantité doit être un entier.")

        while True:
            produit_prix = input("quel est son prix ? : ")
            # on vérifit si le nombre contient une virgule
            if re.match(r'^\d+(?:\.\d+)?$', produit_prix):
                # on type la donnée en "float" si on a un nombre à virgule
                produit["prix"] = float(produit_prix)
                break
            else:
                print("Erreur : le prix doit être un nombre avec ou sans virgule.")

        panier.append(produit)

        end = input("ajouter un autre produit ? : (y) / (n)")
        if end.lower() == "y":
            continue
        elif end.lower() == "n":
            break

    total = sum(produit["prix"] * produit["qt"] for produit in panier)

    return panier, total


panier_total, total = create_produit()
print(panier_total)
print("Total : ", total)
