"""Тестирование класса Record"""

from datetime import date, datetime
from hw12_classes import Record, Phone, Birthday


def test_record_init():
    """Тестирует процесс инициализации экземпляра класса"""
    a = Record('Bob', '09-12-1971')
    assert a.name == 'Bob'
    assert str(a.birthday) == '09-12-1971'
    b = Record('Mary')
    assert b.birthday == None
    a.add_phone('+1-800-123456789')
    assert Phone('+1-800-123456789') in a.phones

def test_add_phone_to_record():
    pass
    