ffrom main import BooksCollector

    # класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollectore
    # обязательно указывать префикс Teste
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книгddg
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книгии
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

        # напиши свои тесты ниже
        # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Кино')
        collector.set_book_genre('Кино', 'Мультфильмы')
        assert  collector.books_genre['Кино']

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Кино')
        collector.set_book_genre('Кино', 'Мультфильмы')
        assert collector.get_book_genre('Кино') == 'Мультфильмы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита','Фантастика')

        assert len(collector. get_books_with_specific_genre('Фантастика')) != 0


    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')
        assert  collector.get_books_genre() == {'Мастер и Маргарита':'Фантастика'}

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Фунтик')
        collector.set_book_genre('Фунтик','Мультфильмы')

        assert   len(collector.get_books_for_children()) >0

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Фунтик')
        collector.set_book_genre('Фунтик', 'Мультфильмы')
        collector.add_book_in_favorites('Фунтик')

        assert 'Фунтик' in collector.favorites



    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Фунтик')
        collector.set_book_genre('Фунтик', 'Мультфильмы')
        collector.add_book_in_favorites('Фунтик')
        collector.delete_book_from_favorites('Фунтик')

        assert 'Фунтик' not in collector.favorites


    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        assert len(collector.favorites) == 0
