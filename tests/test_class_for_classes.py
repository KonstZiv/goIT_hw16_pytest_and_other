"""сгруппированы тесты для тестирования классов и методов
hw12_classes.py"""

from re import A
import pytest
from datetime import datetime, date
from hw12_classes import AdressBook, Birthday, Phone, Record


class TestClasses:
    
    def test_phone(self):
        """Тест класса Phone. Проверяет правильность очистки от лишних символов и
        правильность сравнения телефонов"""
        phone_1 = Phone('+38-(050)-32312345')
        phone_2 = Phone('38[050]+32312345')
        assert phone_1.phone == '3805032312345'
        assert phone_2.phone == '3805032312345'
        assert phone_1 == phone_2

    
    def test_birthday(self):
        """Тест класса Birthday. Проверяет правильность заполнения атрибутов и 
        генерации исключений в случае выявленых ошибок"""
        date_str = '10-10-2021'
        date = datetime.strptime(date_str, '%d-%m-%Y')
        assert Birthday(date_str).birthday == date

        with pytest.raises(ValueError):
            Birthday('10-10-2025')

        with pytest.raises(TypeError):
            test_birthday = Birthday('10-10-2021')
            test_birthday.birthday = '10-10-2021'



    def test_record_init(self):
        """Тестирование класса Record. Тестирует процесс инициализации экземпляра класса"""
        record_1 = Record('Bob', '09-12-1971')
        assert record_1.name == 'Bob'
        assert record_1.birthday.birthday == datetime.strptime('09-12-1971', '%d-%m-%Y')
        record_2 = Record('Mary')
        assert record_2.birthday == None
        assert isinstance(record_2.phones, list)
        assert bool(record_2.phones) == False


    def test_add_phone_to_record(self):
        """Тестирование класса Record. Тестирует процесс добавления телефона в атрибут и
        и возбуждение исключения ValueError если такой телефон уже есть в атрибуте"""
        record_1 = Record('Bob')
        record_1.add_phone('+1-800-123456789')
        assert Phone('+1-800-123456789') in record_1.phones
        with pytest.raises(ValueError):
            record_1.add_phone('+1800-123-456-789')
        record_1.add_phone('+38-067-100-20-39')
        assert Phone('380671002039') in record_1.phones


    def test_del_phone_to_record(self):
        """Тестирование класса Record. Тестирует процесс удаления телефона из атрибута и
        и возбуждение исключения ValueError если такого телефона нет в атрибуте"""
        record_1 = Record('Bob')
        record_1.add_phone('+1-800-123456789')
        record_1.del_phone('+1(800)-123-456-789')
        assert bool(record_1.phones) == False
        with pytest.raises(ValueError):
            record_1.del_phone('+1(800)-123-456-789')

    def test_change_phone_to_record(self):
        """Тестирование класса Record. Тестирует процесс замены телефона в атрибуте"""
        record_1 = Record('Bob')
        record_1.add_phone('+1-800-123456789')
        record_1.change_phone('1-800-[123456789]', '+38-0512-44-55-77')
        assert not Phone('1-800-[123456789]') in record_1.phones
        assert Phone('+38-0512-44-55-77') in record_1.phones
    
    def test_days_tobirthday(self):
        """Тестирование класса Record. Тестирует правильность возвращаемого значения.
        Для сравнения используется эталонное значение"""
        date_str = '09-12-1971'
        record_1 = Record('Bob', date_str)
        etalon_data = datetime.strptime(date_str, "%d-%m-%Y")
        etalon = (etalon_data.replace(year=date.today().year + 1).date() - date.today()).days if date.today() > etalon_data.replace(year=date.today().year).date()\
                else (etalon_data.replace(year=date.today().year).date() - date.today()).days
        print('эталон ', etalon)
        assert record_1.days_tobirthday() == etalon

    def test_add_birthday_to_record(self):
        """Тестирование класса Record. Тестирует ввод ДР в атрибут Record.birthday"""
        record_1 = Record('Bob')
        record_1.add_birthday('10-10-2000')
        assert record_1.birthday.birthday == Birthday('10-10-2000').birthday

    def test_search_birthday(self):
        """Тестирование класса Record. Тестирует определение количество дней до ДР"""
        record_1 = Record('Bob')
        #Даты рождения в записи нет. Должна вернуть None
        assert record_1.search_birthday(data_start='01-12-1971') == None
        #Остальные варианты
        record_1.add_birthday('09-12-1971')
        assert record_1.search_birthday(data_start='09-12-1971') == record_1
        assert record_1.search_birthday(data_start='10-12-1971') == False
        assert record_1.search_birthday(data_start='01-12-1971', data_stop='15-12-1971') == record_1
        assert record_1.search_birthday(data_start='01-12-1971', data_stop='07-12-1971') == False
        assert record_1.search_birthday(data_start='01-12-1971', data_stop='15-12-1971', year=True) == record_1
        assert record_1.search_birthday(data_start='01-12-2021', data_stop='15-12-2021', year=True) == False

    def test_search_to_record(self):
        """Тестирование класса Record. Тестируем поиск по текстовым полям записи"""
        record_1 = Record('Bob Marley')
        record_1.add_phone('+1-123-456-789')
        record_1.add_phone('+38--50-555-44-678')
        assert record_1.search('bob') == record_1
        assert record_1.search('BOB') == record_1
        assert record_1.search('38') == record_1
        assert record_1.search('Mary') == False
        assert record_1.search('67123') == False

    def test_add_record_to_adressbook(self):
        """Тестирует класс Adressbook. Метод добавить запись"""
        adressbook_1 = AdressBook()
        assert bool(adressbook_1) == False
        record_1 = Record('Bob Marley')
        record_1.add_phone('+1-123-456-789')
        record_1.add_phone('+38--50-555-44-678')
        adressbook_1.add_record(record_1)
        assert adressbook_1[record_1.name] == record_1
        with pytest.raises(KeyError):
            adressbook_1.add_record(record_1)

    def test_del_record(self):
        """Тестирует класс Adressbook. Метод удалить запись"""
        adressbook_1 = AdressBook()
        record_1 = Record('Bob Marley')
        record_1.add_phone('+1-123-456-789')
        adressbook_1.add_record(record_1)
        assert record_1.name in adressbook_1
        adressbook_1.del_record('Bob Marley')
        assert not record_1.name in adressbook_1.data
        with pytest.raises(KeyError):
            adressbook_1.del_record('Bob Marley')

    def test_add_fake_records(self):
        """Тестирует класс Adressbook. Метод add_fake_records - наполнение объекта
        adressbook() фейковыми записями"""
        adressbook_1 = AdressBook()
        assert len(adressbook_1) == 0
        adressbook_1.add_fake_records(25)
        assert len(adressbook_1) == 25
        for key in adressbook_1:
            assert isinstance(adressbook_1[key], Record)
            assert adressbook_1[key].name == key 

    def test_search_in_adressbook(self):
        """Тестирует класс Adressbook. Метод search - поиск осоответствий по паттерну в
        adressbook()"""
        adressbook_1 = AdressBook()
        adressbook_1.add_fake_records(20)
        record_1 = Record('Bob Marley')
        record_1.add_phone('+1-123-456-789')
        adressbook_1.add_record(record_1)
        assert isinstance(adressbook_1.search('bob'), AdressBook)
        assert adressbook_1.search('bob')[record_1.name] == adressbook_1[record_1.name]
        assert not adressbook_1.search('bob') is adressbook_1

    def test_search_birthday_in_adressbook(self):
        """Тестирует класс Adressbook. Метод search - поиск записей в 
        adressbook() с ДР попадающими во временной интервал"""
        adressbook_1 = AdressBook()
        adressbook_1.add_fake_records(20)
        record_1 = Record('Bob Marley', '06-02-1945')
        adressbook_1.add_record(record_1)
        assert record_1.name in adressbook_1
        res = adressbook_1.search_birthday('06-02-1945')
        assert res[record_1.name] == record_1
        search_result = adressbook_1.search_birthday(data_start='01-02-1945', data_stop='01-02-1950')
        assert isinstance(search_result, AdressBook)


    def test_out_iterator(self):
        """Тестирует класс Adressbook. Метод out_iterator(num) - который на каждом шаге итерации
        возвращает объект класса AdressBook с количеством элементов до num (по num, на последнем
        шаге - остаток)"""
        adressbook = AdressBook()
        adressbook.add_fake_records(30)
        iter_adressbook = adressbook.out_iterator(5)
        for page in iter_adressbook:
            assert isinstance(page, AdressBook)
            assert len(page) == 5
        
        
        



