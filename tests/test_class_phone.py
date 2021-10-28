from assistant.address__book_classes import Phone, Birthday, Record
from datetime import date, datetime


def test_phone():
    a = Phone('+38-(050)-32312345')
    b = Phone('38[050]+32312345')
    assert a.phone == '3805032312345'
    assert b.phone == '3805032312345'
