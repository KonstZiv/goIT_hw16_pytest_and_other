from assistant.address__book_classes import Birthday
from datetime import datetime


def test_birthday():
    date_str = '10-10-2021'
    date = datetime.strptime(date_str, '%d-%m-%Y')
    assert Birthday(date_str).birthday == date
