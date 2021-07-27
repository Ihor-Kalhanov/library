import pytest
from books.models import Book
from .factories import BookFactory

@pytest.fixture
def book():
    instance = Book.objects.create(
        title="test_book",
        descriprion="test_description",
        relase_date="2000-12-21"

    )

    return instance
