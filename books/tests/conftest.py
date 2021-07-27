import pytest
from books.models import Book
from django.contrib.auth.models import User

@pytest.fixture
def book():
    instance = Book.objects.create(
        title="test_book",
        descriprion="test_description",
        relase_date="2000-12-21"

    )

    return instance

@pytest.fixture
def user_fixture():
    instance = User.objects.create(
        username='test_user',
        password='testpassword',
        is_staff=False,
        is_active = False,
        is_superuser = False,
    )
    return instance
