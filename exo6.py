from datetime import datetime


### entities ###
class Expense:
    def __init__(self, id: int, date: datetime, amount: float, category_id: int):
        self.id = id
        self.date = date
        self.amount = amount
        self.category_id = category_id


class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


### controllers ###
class ExpenseController:
    def __init__(self):
        self.categories_list = [Category(1, "Cinéma"), Category(2, "Dîner"), Category(3, "Jeux vidéo")]
        self.expense_list = []

    def expense_index(self):
        dashboard = "| id | date | amount | category |\n"
        dashboard += "| --- | --- | --- | --- |\n"
        if self.expense_list:
            for expense in self.expense_list:
                dashboard += f"| {expense.id} | {expense.date.strftime('%Y-%m-%d')} | {expense.amount} | {expense.category_id} |\n"
        else:
            print("Vous n'avez pas de montants enregistrés.")
        return dashboard

    def expense_create(self):
        print("Choisissez une catégorie:")
        for i, category in enumerate(self.categories_list):
            print(f"{i + 1}. {category.name} (ID: {category.id})")
        category_id = int(input("Entrez le numéro de la catégorie: "))
        category = next((category for category in self.categories_list if category.id == category_id), None)
        if category is None:
            print("ID de catégorie invalide")
            return

        date = input("Entrez la date (YYYY-MM-DD): ")
        amount = float(input("Entrez le montant: "))

        new_expense = Expense(len(self.expense_list) + 1, datetime.strptime(date, "%Y-%m-%d"), amount, category.id)
        self.expense_list.append(new_expense)
        print("Dépense créée!")

    def expense_read(self):
        id = int(input("Entrez l'id de la dépense que vous souhaitez lire : "))
        expense = next((expense for expense in self.expense_list if expense.id == id), None)
        if expense is None:
            print("ID de dépense invalide")
            return
        print(f"ID : {expense.id}")
        print(f"Date : {expense.date.strftime('%Y-%m-%d')}")
        print(f"Montant : {expense.amount}")
        print(
            f"Categorie : {next((category for category in self.categories_list if category.id == expense.category_id), None).name}")

    def expense_update(self):
        id = int(input("Entrez l'id de la dépense que vous souhaitez modifier : "))
        expense = next((expense for expense in self.expense_list if expense.id == id), None)
        if expense is None:
            print("ID de dépense invalide")
            return
        print("Choisissez une catégorie:")
        for i, category in enumerate(self.categories_list):
            print(f"{i + 1}. {category.name} (ID: {category.id})")
        category_id = int(input("Entrez le numéro de la catégorie : "))
        category = next((category for category in self.categories_list if category.id == category_id), None)
        if category is None:
            print("ID de catégorie invalide")
            return

        new_date = input("Entrez la nouvelle date (YYYY-MM-DD) (ou 'none' pour ne pas changer) : ")
        if new_date.lower() != 'none':
            new_date = datetime.strptime(new_date, "%Y-%m-%d")
            expense.date = new_date

        new_amount = input("Entrez le nouveau montant (ou 'none' pour ne pas changer) : ")
        if new_amount.lower() != 'none':
            expense.amount = float(new_amount)

        expense.category_id = category.id
        print("Dépense modifiée !")

    def expense_delete(self):
        id = int(input("Entrez l'id de la dépense que vous souhaitez supprimer : "))
        expense = next((expense for expense in self.expense_list if expense.id == id), None)
        if expense is None:
            print("ID de dépense invalide")
            return
        self.expense_list.remove(expense)
        print("Dépense supprimée !")


### main ###
class Main:
    def __init__(self):
        self.expenseController = ExpenseController()

    def menu(self):
        while True:
            print("Bienvenue !")
            print("Que désirez-vous faire ?")
            print("1. Voir les dépenses")
            print("2. Ajouter une nouvelle dépense")
            print("3. Voir le détail d'une dépense")
            print("4. Modifier une dépense")
            print("5. Supprimer une dépense")
            print("6. Quitter")
            choice = int(input("Entrez votre choix: "))

            if choice == 1:
                print(self.expenseController.expense_index())
            elif choice == 2:
                self.expenseController.expense_create()
            elif choice == 3:
                self.expenseController.expense_read()
            elif choice == 4:
                self.expenseController.expense_update()
            elif choice == 5:
                self.expenseController.expense_delete()
            elif choice == 6:
                print("Au revoir!")
                break
            else:
                print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    launcher = Main()
    launcher.menu()
