import pytest

from main import BooksCollector

@pytest.fixture  #создание фикстуры
def collector():
    collector = BooksCollector()
    return collector