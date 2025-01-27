import re


def calcul(a, operator, b):
    try:
        a = float(a) if '.' in a else int(a)
        b = float(b) if '.' in b else int(b)
        if operator == "+":
            return a + b
        elif operator == '-':
            return a - b
        elif operator == 'x' or operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Division par zéro impossible !")
            return a / b
        else:
            raise ValueError("Opération non supportée.")

    except ValueError:
        return "Erreur : Entrée invalide."


def calculatrice():
    print("Calculatrice en Python")
    print("Entrze votre opération normalement")
    print("Exemple: 5+5")

    while True:
        s = (input("Veuillez poser votre opération (ou 'q' pour quitter): ")
             .strip()
             .replace(" ", ""))
        if s.lower() == 'q':
            break
        if not s:
            print("Vous n'avez rien renseigné.")
            continue

        try:
            match = re.match(r'(-?\d+\.?\d*)([-+x*/])(-?\d+\.?\d*)', s)
            a, operator, b = match.groups()
            result = calcul(a, operator, b)
        except (AttributeError, ValueError):
            print("Erreur : Vous avez oubliez un opérateut ou un nombre.")
            continue

        print(f"Résultat : {result}")


if __name__ == "__main__":
    calculatrice()
