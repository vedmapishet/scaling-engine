import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collect):
        collect.add_new_book('Гордость и предубеждение и зомби')
        collect.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collect.get_books_genre()) == 2, 'Книги не добавились'

    @pytest.mark.parametrize('book_names', ['', 'Название_книги_на_сорок_один_символ_отриц',
                                            'Название_книги_на_сорок_два_символаа_отриц'])
    def test_add_new_book_add_negative_book(self, collect, book_names):
        collect.add_new_book(book_names)
        assert len(collect.get_books_genre()) == 0, 'Проверка условия метода не пройдена, книга добавилась'

    def test_set_book_genre_added_genre_book_positive_result(self, collect):
        collect.add_new_book('Шерлок Холм')
        collect.set_book_genre('Шерлок Холм', 'Детективы')
        assert collect.books_genre.get('Шерлок Холм') == 'Детективы'

    def test_set_book_genre_add_genre_is_not_list(self, collect):
        collect.add_new_book('Шерлок Холм')
        collect.set_book_genre('Шерлок Холм', 'Жанр_которого_нет')
        assert collect.books_genre.get('Шерлок Холм') == '', 'Книге добавился жанр которого нет в допустимых жанрах'

    def test_get_book_genre_for_name_positive_result(self, collect):
        collect.add_new_book('Шерлок Холм')
        collect.set_book_genre('Шерлок Холм', 'Детективы')
        assert collect.get_book_genre('Шерлок Холм') == 'Детективы'

    def test_get_books_with_specific_genre_get_two_books_detectiv(self, collect):
        collect.books_genre = {'Шерлок Холмс': 'Детективы', 'Шерлок Холмс_1': 'Детективы', 'Шерлок Холмс_2': 'Ужасы',
                               'Шерлок Холмс_3': 'Мультфильмы'}
        assert len(collect.get_books_with_specific_genre('Детективы')) == 2

    def test_get_books_for_children_two_books(self, collect):
        collect.books_genre = {'Шерлок Холмс': 'Мультфильмы', 'Шерлок Холмс_1': 'Детективы', 'Шерлок Холмс_2': 'Ужасы',
                               'Шерлок Холмс_3': 'Комедии'}
        assert len(collect.get_books_for_children()) == 2

    def test_add_book_in_favorites_add_one_book(self, collect):
        collect.add_new_book('Шерлок Холм')
        collect.add_book_in_favorites('Шерлок Холм')
        assert len(collect.get_list_of_favorites_books()) == 1 and collect.favorites[0] == 'Шерлок Холм'

    def test_add_book_in_favorites_add_two_double_book(self, collect):
        collect.add_new_book('Шерлок Холм')
        collect.add_book_in_favorites('Шерлок Холм')
        collect.add_book_in_favorites('Шерлок Холм')
        assert len(collect.get_list_of_favorites_books()) == 1, 'В избранное добавился дубль книги'

    def test_delete_book_from_favorites(self, collect):
        collect.add_new_book('Шерлок Холм')
        collect.add_book_in_favorites('Шерлок Холм')
        collect.delete_book_from_favorites('Шерлок Холм')
        assert len(collect.favorites) == 0



