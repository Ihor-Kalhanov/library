import datetime

import pytest
from http import HTTPStatus

pytestmark = pytest.mark.django_db


class TestBookModel:

    def test_book_fields_success(self, book):
        assert book.title == "test_book"
        assert book.descriprion == "test_description"
        assert book.phone_number == 12345
        assert isinstance(book.created_at, datetime.datetime)
        assert isinstance(book.updated_at, datetime.datetime)

    def test_book__str__(self, book):
        assert book.title in str(book)
















