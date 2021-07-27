import pytest
from django.urls import reverse
from http import HTTPStatus
pytestmark = pytest.mark.django_db

class TestBookModel:

    def test_book_fields(self, book):
        assert book.title == "test_book"
        assert book.descriprion == "test_description"
        assert book.relase_date == "2000-12-21"

    def test_book__str__(self, book):
        assert isinstance(book.title, str)



class TestAdminUserModel:

    def test_new_admin_user(self, django_user_model):
        django_user_model.objects.create(
            username="test_user",
            password="testpassword",
            is_superuser=True
        )

    def test_an_admin_view(self, admin_client):
        response = admin_client.get('/admin/')
        assert response.status_code == HTTPStatus.OK
















