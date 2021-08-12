import datetime

import pytest
from books.models import Book


from rest_framework.test import APIClient
from rest_framework.authentication import get_user_model

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_api_client(user):
    client = APIClient()
    client.force_login(user)

    return client


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        email='emaitest@test.com',
        username='testusername',
        first_name='test_first_name',
        last_name='test_last_name',
        password='testpassword12345',
    )


@pytest.fixture
def user_admin(django_user_model):
    return django_user_model.objects.create_user(
        email='emaitestadmin@test.com',
        username='testusernameadmin',
        first_name='test_first_name_admin',
        last_name='test_last_name_admin',
        password='testpassword12345admin',
        is_staff=True
    )


@pytest.fixture
def book(auth_api_client):
    instance = Book.objects.create(
        title="test_book",
        owner=auth_api_client,
        description="test_description",
        phone_number=12345,
        created_at=datetime.datetime.now()
    )

    return instance

# @pytest.fixture
# def custom_user():
#     instance = User.objects.create(
#         email='emaitest@test.com',
#         username='testusername',
#         first_name='test_first_name',
#         last_name='test_last_name',
#         password='testpassword12345',
#     )
#
#     return instance
#
#
# @pytest.fixture
# def custom_user_admin():
#     instance = User.objects.create(
#         email='emaitestadmin@test.com',
#         username='testusernameadmin',
#         first_name='test_first_name_admin',
#         last_name='test_last_name_admin',
#         password='testpassword12345admin',
#         is_staff=True
#     )
#
#     return instance
