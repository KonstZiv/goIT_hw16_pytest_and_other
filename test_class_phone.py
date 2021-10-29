"""Тест для проверки класса Phone"""
from hw12_classes import Phone


def test_phone():
    """Проверяет правильность очистки от лишних символов и
    правильность сравнения телефонов"""
    phone_1 = Phone('+38-(050)-32312345')
    phone_2 = Phone('38[050]+32312345')
    assert phone_1.phone == '3805032312345'
    assert phone_2.phone == '3805032312345'
    assert phone_1 == phone_2
