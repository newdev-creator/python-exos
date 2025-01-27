def create_element(elm: str) -> str:
    # Ajoute un élément à la liste


def display_menu() -> str:
    # Menu des actions possible.
    print("\n=== Gestion de la liste de course ===")
    print("1. Ajouter un élément à la liste")
    print("2. Retirer un élément de la liste")
    print("3. Afficher la liste")
    print("4. Vider la liste")
    print("5. Quitter")
    choice = input("Choississez parmi les 5 options suivantes : ")
    return choice


def read_integer(prompt: str) -> int:
    # Lecture de l'option choissie.
    return int(input(prompt))

def main():
    shopping_list = []
    while True:
        choice = display_menu()

        if choice == "1":
            elm = input("Entrez le nom d'un élément à ajouter à la liste de course : ")
            create_element(elm)
            print(f"l'élément {elm} a bien été ajouté à la liste.)
