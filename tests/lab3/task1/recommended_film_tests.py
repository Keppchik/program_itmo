import unittest
from src.lab3.task1.recommended_film import RecommendedFilm


class RecommendedFilmTestCase(unittest.TestCase):
    films_path = "films.txt"
    history_path = "history.txt"
    recommendedFilm = RecommendedFilm(films_path, history_path)

    def test_func_create_films(self):
        self.assertEquals(self.recommendedFilm.films["1"], "Мстители: Финал")
        self.assertEquals(self.recommendedFilm.films["2"], "Хатико")

    def test_func_create_persons(self):
        self.assertEquals(self.recommendedFilm.persons[0].history, ['2','1','3'])
        self.assertEquals(self.recommendedFilm.persons[2].history, ['2','2','2','2','2','3'])

    def test_func_recommended_film1(self):
        user_input = "2,3"
        recommended_film = self.recommendedFilm.recommended_film(user_input)
        self.assertEquals(recommended_film, "Мстители: Финал")

    def test_func_recommended_film2(self):
        user_input = "3,4"
        recommended_film = self.recommendedFilm.recommended_film(user_input)
        self.assertEquals(recommended_film, "Хатико")

    def test_func_recommended_film3(self):
        user_input = "5,6"
        recommended_film = self.recommendedFilm.recommended_film(user_input)
        self.assertEquals(recommended_film, "Нет рекомендованного для вас фильма")

    def test_func_recommended_film_by_value1(self):
        user_input = "2,3"
        recommended_film = self.recommendedFilm.recommended_film_by_value(user_input)
        self.assertEquals(recommended_film, "Мстители: Финал")

    def test_func_recommended_film_by_value2(self):
        user_input = "1,4"
        recommended_film = self.recommendedFilm.recommended_film_by_value(user_input)
        self.assertEquals(recommended_film, "Дюна")

    def test_func_recommended_film_by_value3(self):
        user_input = "5,6"
        recommended_film = self.recommendedFilm.recommended_film_by_value(user_input)
        self.assertEquals(recommended_film, "Нет рекомендованного для вас фильма")

