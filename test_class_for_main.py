"""Клас для тестирования модуля main консольного приложения 'персональный помощник'"""
from hw12_classes import AdressBook, Record
from main import parse, get_handler

class TestMain:
    """Класс для тестирования модуля main консольного приложения 'персональный помощник'"""

    def test_parse(self):
        """Тестирует функцию parse(). В ходе теста проверяется работа вложенных функций
        parse_phone() и parse_word()"""
        assert parse('hello') == ('hello', '', '')
        assert parse('addBob Marley +38') == ('add', 'Bob Marley +38', '')
        assert parse('phone Bob Marley +800[123]4567') == ('phone', 'Bob Marley', '+800[123]4567')
        assert parse('show all') == ('show all', '', '')
        assert parse('exit') == ('exit', '', '')
        assert parse('.') == ('.', '', '')
        assert parse('close') == ('close', '', '')
        assert parse('good bye') == ('good bye', '', '')
        assert parse('help') == ('help', '', '')
        assert parse('search zzzzzz') == ('search', 'zzzzzz', '')
        assert parse('other phone +322123456-67') == ('other phone', '', '+322123456-67')
        assert parse('bd add') == ('bd add', '', '')
        assert parse('sdfghjk') == ('unrecognize', '', '')

    def test_get_handler(self):
        """Тестирует функцию parse(). В ходе теста проверяется работа вложенных функций
        help_f(), add_f(), hello_f(), phone_f(), show_all_f(), exit_f(), unrecognize_f(),
        add_phone(), bd_add_f()"""
        adressbook = AdressBook()
        assert get_handler(('help', '', ''), adressbook) == """формат команд:
        - add - формат: add name phone_number - добавляет новый контакт
        - other phone - формат: other phone name phone_number -
        добавляет дополнительный телефон в существующую запись
        - show all - формат: show all [N] - показывает всю адресную книгу.
        N - необязательный параметр - количество одновременно выводимых записей
        - exit/./close/goog bye - формат: exit - остановка работы с программой.
        Важно! чтобы сохранить все изменения и введенные данные - используйте
        эту команду
        - phone - формат: phone name - поиск телефона по имени. Можно ввести
        неполной имя либо его часть - программа выведет все совпадения
        - hello - формат: hello - просто Ваше привествие программе. Доброе слово
        - оно и для кода приятно)
        - bd add - формат: bd add name dd-mm-YYYY - ввод либо перезапись ранее
        введенной даты рождения. Соблюдайте формат ввода даты.
        - search - формат: search pattern - поиск совпадений по полям имени и
        телефонов. Будут выведены все записи в которых есть совпадения"""
        assert get_handler(('hello', '', ''), adressbook) ==  "How can I help you?"
        assert get_handler(('exit', '', ''), adressbook) ==  None
        assert get_handler(('.', '', ''), adressbook) ==  None
        assert get_handler(('close', '', ''), adressbook) ==  None
        assert get_handler(('good bye', '', ''), adressbook) ==  None
        assert get_handler(('unrecognize', '', ''), adressbook) ==  'ввод не распознан. Для получения помощи введите "help"'
        assert get_handler(('add', 'Bob Marley', '+38-044-444-33-22'), adressbook) ==  f"в адресную книгу внесена запись: \n{adressbook['Bob Marley']}"
        assert get_handler(('phone', 'Bob Marley', '+38-044-444-33-22'), adressbook) ==  adressbook.search('Bob Marley')
        assert get_handler(('search', 'Bob Marley', '+38-044-444-33-22'), adressbook) ==  adressbook.search('Bob Marley')
        assert get_handler(('show all', '', ''), adressbook) == "вывод окончен"
        assert get_handler(('other phone', 'Bob Marley', '+38-067-111-55-99'), adressbook) ==  f"в запись добавлен новый телефон: \n {adressbook['Bob Marley']}"
        assert get_handler(('other phone', 'Jimi Hendrix', '+63-999-88-77'), adressbook) ==  "имени Jimi Hendrix нет в адресной книге"
        assert get_handler(('bd add', 'Bob Marley', '06-02-1945'), adressbook) == f"в запись добавлена дата рождения: \n {adressbook['Bob Marley']}"
        assert get_handler(('bd add', 'Jimi Hendrix', '27-11-1942'), adressbook) == "имени Jimi Hendrix нет в адресной книге"
        

