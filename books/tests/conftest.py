import datetime

import pytest
from books.models import Book
from django.contrib.auth.models import User

from rest_framework.test import APIClient


@pytest.fixture
def book():
    instance = Book.objects.create(
        title="test_book",
        descriprion="test_description",
        phone_number=12345,
        created_at=datetime.datetime.now()
    )

    return instance


@pytest.fixture
def user_fixture():
    instance = User.objects.create(
        username='test_user',
        password='testpassword',
        is_staff=False,
        is_active=False,
        is_superuser=False,
    )
    return instance


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_client(django_user_model, api_client):
    return api_client.force_login(django_user_model.objects.create_user(username='username', password='password'))