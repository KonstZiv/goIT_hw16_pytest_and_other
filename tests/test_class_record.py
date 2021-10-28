from assistant.address__book_classes import Record, Phone
from datetime import date, datetime


def test_record():
    a = Record('Bob', '09-12-1971')
    assert a.name == 'Bob'
    #assert a.birthday == Birthday('09-12-1971')
    b = Record('Mary')
    assert b.birthday == None
    a.add_phone('+1-800-123456789')
    assert Phone('+1-800-123456789') in a.phones
