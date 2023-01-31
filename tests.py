from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляркласса BooksCollector()
class TestBooksCollector:

    def test_cant_set_rating_for_missing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Над пропастью во ржи")
        assert collector.get_book_rating("Над пропастью во ржи") == 1


class TestBooksCollector:
    def test_cannot_set_rating_for_unexisting_book(self):
        collector = BooksCollector()
        collector.set_rating("Великий Гэтсби", 5)
        assert collector.get_book_rating("Великий Гэтсби") is None


class TestBooksCollector:
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Великий Гэтсби")
        assert collector.get_book_rating("Великий Гэтсби") == 1


class TestBooksCollector:
    def test_unadded_book_has_no_rating(self):
        collector = BooksCollector()
        book_name = "The Catcher in the Rye"
        collector.add_favorite_book(book_name)
        assert book_name not in collector.favorite_books


class TestBooksCollector:
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = "Над пропастью во ржи"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name in favorites


class TestBooksCollector:
    def test_cannot_add_book_in_favorites_if_not_in_books_rating(self):
        collector = BooksCollector()
        book_name = "Убить пересмешника"
        assert collector.add_book_in_favorites(book_name) == False


class TestBooksCollector:
    def test_remove_book_from_favorites(self):
        collector = BooksCollector()
        book_name = "Убить пересмешника"
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, 5)
        collector.add_to_favorites(book_name)
        collector.remove_from_favorites(book_name)
        assert book_name not in collector.books_rating
