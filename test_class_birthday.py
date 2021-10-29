"""Тест класса Birthday"""
import pytest
from datetime import datetime
from hw12_classes import Birthday


def test_birthday():
    date_str = '10-10-2021'
    date = datetime.strptime(date_str, '%d-%m-%Y')
    assert Birthday(date_str).birthday == date

    with pytest.raises(ValueError):
        Birthday('10-10-2025')

    with pytest.raises(TypeError):
        test_birthday = Birthday('10-10-2021')
        test_birthday.birthday = '10-10-2021'