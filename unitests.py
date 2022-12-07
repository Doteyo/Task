from unittest import TestCase
from task2 import addToDict, sal, Keys, year, fill_gaps, ProfKeys
import random as rd

list1 = ['name', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at']

list2 = ['name', 'salary_from', 'salary_to', 'sos', 'salary_currency', 'area_name', 'published_at']

pk1 = ProfKeys(list1)

pk2 = ProfKeys(list2)


class AddToDictTests(TestCase):

    def test_empty_dict(self):
        temp = {}
        addToDict('a', temp, 1)
        self.assertEqual(temp, {'a': 1})

    def test_same_key(self):
        temp = {'a': 1}
        addToDict('a', temp, 5)
        addToDict('b', temp, 'gg')
        self.assertEqual(temp, {'a': 6, 'b': 'gg'})


class SalTest(TestCase):

    def test_clean_number(self):
        self.assertEqual(sal(20000, 50000, 'RUR'), 35000.0)

    def test_dirty_number(self):
        self.assertEqual(sal(12345, 69420, 'BYR'), 977500.575)

    def test_random_numbers(self):
        a = rd.random() * 10000
        b = a + rd.random() * 100000
        res = (a + b) / 2
        self.assertEqual(res, sal(a, b, 'RUR'))


class YearTest(TestCase):

    def test_first(self):
        Keys.published_at = 2
        self.assertEqual(year(["This", 'is', '5']), 5)

    def test_four_digits(self):
        Keys.published_at = 2
        self.assertEqual(year(["This", 'is', '12345']), 1234)


class FillGapsTest(TestCase):

    def test_empty_dict(self):
        self.assertEqual(fill_gaps({}, {"a": 1, 'b': 2}, 0), {'a': 0, 'b': 0})

    def test_keys_match(self):
        self.assertEqual(fill_gaps({'a': 5}, {"a": 1, 'b': 2}, 'yes'), {'a': 5, 'b': 'yes'})


class ProfKeysTest(TestCase):

    def test_correct_name(self):
        self.assertEqual(type(pk1).__name__, 'ProfKeys')

    def test_area_name(self):
        self.assertEqual(pk1.area_name, 4)

    def test_area_name_with_junk_item(self):
        self.assertEqual(pk2.area_name, 5)
