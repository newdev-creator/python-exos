from datetime import date
from typing import Optional


class Person:
    def __init__(self, name: str, birthday: date, message: str):
        self.name = name
        self.birthday = birthday
        self.message = message


class BirthdayCalendar:
    person_list: list = []

    def __init__(self):
        pass

    def create_person(self, name: str, birthday: date, message: str) -> None:
        new_person = Person(name, birthday, message)
        self.person_list.append(new_person)

    def list_by_age(self) -> None:
        current_date = date.today()
        sorted_persons = []
        for person in self.person_list:
            birthday_date = person.birthday
            if current_date < birthday_date:
                print(f"{person.name} n'est pas née.")
            else:
                age = current_date.year - birthday_date.year - (
                            (current_date.month, current_date.day) < (birthday_date.month, birthday_date.day))
                sorted_persons.append((person.name, age))
        sorted_persons.sort(key=lambda x: x[1])
        for person, age in sorted_persons:
            print(f"{person} à {age} ans.")

    def search_person(self, name: str) -> Optional[Person]:
        for person in self.person_list:
            if person.name.lower() == name.lower():
                return person

        return None


calendar = BirthdayCalendar()

calendar.create_person("Jean", date(1990, 12, 25), "coucou toi")
calendar.create_person("Sara", date(2001, 2, 5), "coucou ma belle")
calendar.create_person("Zoé", date(2025, 2, 5), "coucou ma belle")

print(len(calendar.person_list))

person = calendar.search_person("Jean")

if person:
    print(f"Bon anniversaire {person.name} ! {person.message}")
else:
    print("Personne non trouvée")

calendar.list_by_age()
