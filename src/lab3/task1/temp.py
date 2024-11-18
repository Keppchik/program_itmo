from logging import raiseExceptions


class Film:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Person:
    def __init__(self, id, history):
        self.id = id
        self.history = history

def read_file(filename):
    f = open(filename, 'r')
    data = f.readlines()
    f.close()
    return data

def create_films(data):
    data = [x.replace("\n", "") for x in data]
    data = [x for x in data if x]
    films = []
    for i, line in enumerate(data):
        line = line.split(",")
        id = line[0]
        name = line[1]
        films.append(Film(id, name))

    films_dict = {film.id: film.name for film in films}
    return films, films_dict

def create_person(data):
    data = [x.replace("\n", "") for x in data]
    data = [x for x in data if x]
    persons = []
    for i, history in enumerate(data):
        history = history.split(",")
        id = i + 1
        persons.append(Person(id, history))

    return persons

def input_data():
    input_history = set(input("Введите индексы фильмов, которые вы смотрели, через запиткю: ").split(","))
    while True:
        k = 0
        for id in input_history:
            if id.isnumeric():
                k += 1
        if k == len(input_history):
            break
        else:
            input_history = set(input("Вы неправильно ввели значения, попробуйте ещё раз: ").split(","))
    return input_history


def persons_with_same_history(history):
    suitable_persons_value = []
    for person in persons:
        same_history = history.intersection(set(person.history))
        if len(same_history) >= (len(history) / 2):
            value = len(same_history) / len(history)
            suitable_persons_value.append((person, value))
    return suitable_persons_value

def recommended_films_id(input_history, persons):
    films = set()
    for person in persons:
        films = films | (set(person.history) - input_history)
    return films

def recommended_films_id_by_value(input_history, persons_value):
    persons_value = sorted(persons_value, key=lambda x: x[1], reverse=True)
    films = []
    films.append(set(persons_value[0][0].history) - input_history)
    for i in range(1, len(persons_value)):
        if persons_value[i][1] == persons_value[i - 1][1]:
            films[-1] = films[-1] | (set(persons_value[i][0].history) - input_history)
        else:
            films.append(set(persons_value[i][0].history) - input_history)

    for film in films:
        if len(film) == 0:
            pass
        else:
            return film
    return None


def popular_film_id(films, persons):
    max_count = 0
    popular_film = ""
    for film in films:
        count = 0
        for person in persons:
            for person_history in person.history:
                if person_history == film:
                    count += 1
        if count > max_count:
            popular_film = film
            max_count = count

    return popular_film

def find_recommended_film(input_history, persons, films_dict):
    recommended_persons_value = persons_with_same_history(input_history)
    recommended_persons = [t[0] for t in recommended_persons_value]

    recommended_films = recommended_films_id(input_history, recommended_persons)

    recommended_films_by_value = recommended_films_id_by_value(input_history, recommended_persons_value)

    popular_film = popular_film_id(recommended_films, persons)

    popular_film_by_value = popular_film_id(recommended_films_by_value, persons)

    if popular_film not in films_dict:
        result = None
    else:
        result = films_dict[popular_film]

    if popular_film_by_value not in films_dict:
        return (result, None)
    else:
        return (result,films_dict[popular_film_by_value])


if __name__ == '__main__':
    films_data = read_file("task1/texts/films.txt")
    history_data = read_file("task1/texts/history.txt")

    films, films_dict = create_films(films_data)
    persons = create_person(history_data)

    input_history = input_data()

    recommended_film, recommended_film_by_value = find_recommended_film(input_history, persons, films_dict)
    print(f"Рекомендованный фильм для вас: {recommended_film}")
    print(f"Рекомендованный фильм для вас по системе ценности: {recommended_film_by_value}")





