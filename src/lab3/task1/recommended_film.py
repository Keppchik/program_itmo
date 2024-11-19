class Film:
    """Класс, в котором хранятся id и имя фильма"""

    def __init__(self, film_id, name):
        """Инициализирует объект Film"""

        self.film_id = film_id
        self.name = name


class Person:
    """Класс, в котором хранятся id пользователя и id фильмов, посмотренных пользователем"""

    def __init__(self, person_id, history):
        """Инициализирует объект Person"""

        self.person_id = person_id
        self.history = history


class RecommendedFilm:
    """Класс для поиска рекомендованного фильма по алгоритму"""

    def __init__(self, films_path, history_path):
        """Инициализирует объект RecommendedFilm"""

        self.persons = []
        self.films = {}
        self.create_films(films_path)
        self.create_persons(history_path)

    def create_films(self, filepath):
        """Читает список фильмов из файла и сохраняет их в словаре films"""

        with open(filepath, "r", encoding="utf-8") as file:
            films = []
            for line in file.readlines():
                if line.strip():
                    film_id, name = line.split(",")
                    films.append(Film(film_id, name))
        self.films = {film.film_id: film.name for film in films}

    def create_persons(self, filepath):
        """Читает список историй просмотров пользователей из файла и сохраняет их в листе persons"""

        with open(filepath, "r", encoding="utf-8") as file:
            for i, films in enumerate(file.readlines()):
                films = films.strip().split(",")
                person_id = i + 1
                self.persons.append(Person(person_id, films))

    def recommended_film(self, user_history):
        """Находит рекомендованный фильм для пользователя на основе его истории просмотров по алгоритму:
        1. Для просмотров пользователя из историй по всем пользователям выбираются те, у которых хотя бы половина фильмов совпадает с заданной.
        2. Из отобранных списков исключаются все, которые пользователь уже посмотрел.
        3. Для оставшегося списка фильмов подсчитывается суммарное количество просмотров среди всех пользователей сервиса и фильм с максимальным числом просмотров выбирается как рекомендация (если таких фильмов оказалось несколько, выбирается любой из них)."""

        user_history = set(user_history.split(","))
        simular_persons = []
        for person in self.persons:
            same_history = set(person.history) & user_history
            if len(same_history) >= (len(user_history) / 2):
                simular_persons.append(person)

        good_films = set()
        for person in simular_persons:
            good_films = good_films | (set(person.history) - user_history)

        recommended_films = [0] * (len(self.films) + 1)
        for film in good_films:
            for person in self.persons:
                for watched_film in person.history:
                    if watched_film == film:
                        recommended_films[int(film)] += 1

        recommended_film_id = str(recommended_films.index(max(recommended_films)))
        if recommended_film_id != "0":
            return self.films[recommended_film_id]
        return "Нет рекомендованного для вас фильма"


if __name__ == "__main__":
    FILMS_PATH = "texts/films.txt"
    HISTORY_PATH = "texts/history.txt"

    USER_HISTORY = str(input())
    recommended_film = RecommendedFilm(FILMS_PATH, HISTORY_PATH).recommended_film(USER_HISTORY)

    print(recommended_film)
