import unittest
from src.lab3.task2.survey import Survey, AgeGroup, Person


class SurveyTestCase(unittest.TestCase):
    survey = Survey([18, 35, 50])

    def test_class_person(self):
        person = Person("Иванов Иван Иванович",23)
        self.assertEquals(str(person),"Иванов Иван Иванович (23)")

    def test_class_age_group(self):
        age_group = AgeGroup(18,30)
        age_group.add_person(Person("Иванов Иван Иванович",23))
        self.assertEquals(str(age_group.persons[0]), "Иванов Иван Иванович (23)")
        self.assertTrue(age_group.has_persons())

    def test_func_create_age_groups(self):
        self.assertEqual(len(self.survey.age_groups), 4)
        self.assertEqual(self.survey.age_groups[0].low, 0)
        self.assertEqual(self.survey.age_groups[0].high, 18)
        self.assertEqual(self.survey.age_groups[1].low, 19)
        self.assertEqual(self.survey.age_groups[1].high, 35)
        self.assertEqual(self.survey.age_groups[2].low, 36)
        self.assertEqual(self.survey.age_groups[2].high, 50)
        self.assertEqual(self.survey.age_groups[3].low, 51)
        self.assertEqual(self.survey.age_groups[3].high, 123)

    def test_add_person(self):
        person = Person("Иванов Иван Иванович", 23)
        self.survey.add_person(person)

        for age_group in self.survey.age_groups:
            if age_group.low <= person.age <= age_group.high:
                self.assertIn(person, age_group.persons)


