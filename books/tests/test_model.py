import pytest
from datetime import datetime


pytestmark = pytest.mark.django_db

class TestBookModel:

    def test_book_fields(self, book):
        assert book.title == "test_book"
        assert book.descriprion == "test_description"
        assert book.relase_date == "2000-12-21"

    def test_book__str__(self, book):
        assert isinstance(book.title, str)






