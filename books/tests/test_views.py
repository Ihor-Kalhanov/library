import pytest
from rest_framework import status
from rest_framework.utils import json

from books.serializers import Bookserializer
from books.views import BooksView

pytestmark = pytest.mark.django_db


class TestViewBooks:
    endpoint = '/api/books/'

    def test_get_all_books(self, client, django_user_model):
        user = django_user_model.objects.create_user(
            username="username",
            password="password")
        client.force_login(user)
        response = client.get(self.endpoint)
        response_content = json.loads(response.content)
        assert isinstance(response_content, list)
        assert response.status_code == status.HTTP_200_OK

    def test_post_book_success(self, api_client, django_user_model):
        user = django_user_model.objects.create_user(username='username', password='password')
        body = {
            "title": "title1231222223",
            "descriprion": "lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem",
            "phone_number": 12345
        }
        api_client.force_login(user)
        response = api_client.post(
            self.endpoint,
            body,
            format='json',
        )

        assert "id" in json.loads(response.content)
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_book_invalid(self, api_client, django_user_model):
        user = django_user_model.objects.create_user(username='username', password='password')
        body_invalid = {
            "title": "title1231222223",
            "descriprion": "lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem",
            "phone_number": "asdasdasd"
        }
        api_client.force_login(user)
        response = api_client.post(
            self.endpoint,
            body_invalid,
            format='json',
        )
        serializer = Bookserializer(data=body_invalid)
        assert serializer.is_valid() is False
        assert serializer.errors != {}
        assert response.status_code == status.HTTP_400_BAD_REQUEST


    def test_post_retrieve_book(self, book, api_client, django_user_model):
        user = django_user_model.objects.create_user(username='username', password='password')

        url = f'{self.endpoint}{book.id}/'
        api_client.force_login(user)
        response = api_client.get(url)
        assert isinstance(json.loads(response.content), dict)
        assert Bookserializer(json.loads(response.content))
        assert response.status_code == status.HTTP_200_OK




    def test_not_authenticated_client(self, client):
        response = client.get('/api/books/')

        assert response.status_code == status.HTTP_403_FORBIDDEN
