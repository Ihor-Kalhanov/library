from http import HTTPStatus

import pytest

from books.views import BooksView


class TestViewBooks:

    def test_with_authenticated_client(self, client, django_user_model):
        user = django_user_model.objects.create_user(
            username="username",
            password="password")
        client.force_login(user)
        response = client.get('/api/books/')
        assert response.status_code == HTTPStatus.OK

    def test_not_authenticated_client(self, client):
        response = client.get('/api/books/')
        assert response.status_code == HTTPStatus.FORBIDDEN
