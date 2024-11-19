import sys

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def __str__(self):
        return f'{self.name} ({self.age})'


class AgeGroup:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.persons = []

    def add_person(self, person):
        if self.low <= person.age <= self.high:
            self.persons.append(person)

    def sort_persons(self):
        self.persons.sort(key=lambda x: (-x.age, x.name))

    def has_persons(self):
        return len(self.persons) > 0


class Survey:
    def __init__(self, ages):
        self.age_groups = []
        self.create_age_groups(ages)
        self.persons = []

    def read_input(self):
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
        previous_age = 0
        for age in ages:
            self.age_groups.append(AgeGroup(previous_age, age))
            previous_age = age + 1
        self.age_groups.append(AgeGroup(previous_age, 123))

    def add_person(self, person):
        self.persons.append(person)
        for age_group in self.age_groups:
            age_group.add_person(person)

    def print_results(self):
        self.age_groups.sort(key=lambda x: x.low, reverse=True)
        for group in self.age_groups:
            group.sort_persons()
            if group.has_persons():
                print(f"{group.low}{'-'+str(group.high) if group.high < 123 else '+'}: {', '.join(map(str, group.persons))}")


if __name__ == '__main__':
    age_groups = list(map(int, sys.argv[1:]))
    survey = Survey(age_groups)
    survey.read_input()
    survey.print_results()

