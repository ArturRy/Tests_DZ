import requests
from main import direct, supernames, top_3_name, unique_names, mentors, courses, Some_name
import pytest

some_name = 'Name'


class TestPytest():
    def test_unique(self):
        res = unique_names(mentors)
        expected = 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, ' \
                   'Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, ' \
                   'Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, ' \
                   'Эдгар, Юрий'
        assert res == expected

    @pytest.mark.xfail
    def test_name_top(self):
        res = top_3_name(mentors)
        expected = 'NONE_NONE_NONE'
        assert res == expected

    @pytest.mark.skipif(Some_name == 'Name', reason='Some reason')
    def test_supernames(self):
        res = supernames(mentors, courses)
        expected = 'Александр'
        assert expected in res

    def test_directory(self):
        res = direct().status_code
        expected_min = 200
        expected_max = 300
        assert expected_max > res > expected_min
