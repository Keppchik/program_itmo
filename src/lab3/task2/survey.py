import sys


class Person:
    """Класс для представления человека с именем и возрастом"""

    def __init__(self, name, age):
        """Инициализирует объект Person"""

        self.name = name
        self.age = int(age)

    def __str__(self):
        """Возвращает ФИО (возраст) человека при str(Person)"""

        return f"{self.name} ({self.age})"


class AgeGroup:
    """Класс для представления возрастной группы"""

    def __init__(self, low, high):
        """Инициализирует объект AgeGroup"""

        self.low = low
        self.high = high
        self.persons = []

    def add_person(self, person):
        """Добавляет человека в возрастную группу"""

        if self.low <= person.age <= self.high:
            self.persons.append(person)

    def sort_persons(self):
        """Сортирует всех людей в возрастной группе по возрасту в порядке убывания, если возраст совпадает - по ФИО в порядке возрастания"""

        self.persons.sort(key=lambda x: (-x.age, x.name))

    def has_persons(self):
        """Возвращает True, если есть хоть один человек в возрастной группе, и False, если такого нет"""

        return len(self.persons) > 0


class Survey:
    """Класс для проведения опроса и распределения людей по возрастным группам"""

    def __init__(self, ages):
        """Инициализирует объект Survey"""

        self.age_groups = []
        self.create_age_groups(ages)
        self.persons = []

    def read_input(self):
        """Читает ФИО и возраст каждого человека из ввода пользователя"""

        print("Введите имена и возраст респондентов в виде строк: ")
        print("<ФИО>,<возраст>")
        print("Строка END сигнализирует об окончании списка.")
        for line in sys.stdin:
            line = line.strip()
            if line == "END":
                break
            name, age = line.split(",")
            age = int(age)
            self.add_person(Person(name, age))

    def create_age_groups(self, ages):
        """Создаёт возрастные группы из ввода пользователя"""

        previous_age = 0
        for age in ages:
            self.age_groups.append(AgeGroup(previous_age, age))
            previous_age = age + 1
        self.age_groups.append(AgeGroup(previous_age, 123))

    def add_person(self, person):
        """Добавляет человека в возрастную группу"""

        self.persons.append(person)
        for age_group in self.age_groups:
            age_group.add_person(person)

    def print_results(self):
        """Выводит группу и людей в ней"""

        self.age_groups.sort(key=lambda x: x.low, reverse=True)
        for group in self.age_groups:
            group.sort_persons()
            if group.has_persons():
                print(
                    f"{group.low}{'-'+str(group.high) if group.high < 123 else '+'}: {', '.join(map(str, group.persons))}"
                )


if __name__ == "__main__":
    age_groups = list(map(int, sys.argv[1:]))
    survey = Survey(age_groups)
    survey.read_input()
    survey.print_results()
