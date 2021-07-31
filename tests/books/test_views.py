import datetime
import pytest

from rest_framework import status
from rest_framework.utils import json
from model_bakery import baker

from books.models import Book
from books.serializers import Bookserializer

pytestmark = pytest.mark.django_db


class TestViewBooks:
    endpoint = '/api/books/'

    def test_get_all_books(self, api_client, auth_api_client):
        baker.make(Book, _quantity=3)

        api_client.force_login(auth_api_client)
        response = api_client.get(
            self.endpoint
        )

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(json.loads(response.content), list)
        assert len(json.loads(response.content)) == 3

    def test_post_book_success(self, api_client, auth_api_client):
        book = baker.prepare(Book)
        body = {
            "id": book.id,
            "title": book.title,
            "description": book.description,
            "phone_number": book.phone_number,
            "created_at": book.created_at,
            "updated_at": book.updated_at,
        }

        api_client.force_login(auth_api_client)
        response = api_client.post(
            self.endpoint,
            body,
            format='json',
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert "id" in json.loads(response.content)

    def test_post_book_invalid(self, api_client, auth_api_client):
        body_invalid = {
            "title": "title1231222223",
            "description": "lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem",
            "phone_number": "asdasdasd"
        }

        api_client.force_login(auth_api_client)
        response = api_client.post(
            self.endpoint,
            body_invalid,
            format='json',
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_retrieve_book(self, book, api_client, auth_api_client):
        url = f'{self.endpoint}{book.id}/'

        api_client.force_login(auth_api_client)
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(json.loads(response.content), dict)



    def test_update_book_success(self, book, api_client, auth_api_client):
        url = f'{self.endpoint}{book.id}/'
        body_new_book = {
            "id": book.id,
            "title": "Updated",
            "description": "Updated",
            "phone_number": book.phone_number,
            "created_at": book.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "updated_at": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }

        api_client.force_login(auth_api_client)
        response = api_client.put(
            url,
            body_new_book,
            format='json',
        )

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(json.loads(response.content), dict)
        assert json.loads(response.content).get('title') == body_new_book.get('title')


    def test_update_book_invalid(self, book, api_client, auth_api_client):
        url = f'{self.endpoint}{book.id}/'
        body_new_book_invalid = {
            "id": book.id,
            "title": "Updated",
            "description": "Updated",
            "phone_number": "asdfghj",
            "created_at": book.created_at.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            "updated_at": datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        }
        api_client.force_login(auth_api_client)
        response = api_client.put(
            url,
            body_new_book_invalid,
            format='json',
        )

        assert isinstance(json.loads(response.content), dict)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_delete_book(self, book, api_client, auth_api_client):
        url = f'{self.endpoint}{book.id}/'

        api_client.force_login(auth_api_client)
        response = api_client.delete(
            url,
            format='json',
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_not_authenticated_client(self, client):
        response = client.get('/api/books/')

        assert response.status_code == status.HTTP_403_FORBIDDEN
