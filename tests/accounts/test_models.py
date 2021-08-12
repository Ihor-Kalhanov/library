from datetime import datetime

import pytest

pytestmark = pytest.mark.django_db


class TestCustomUserModel:

    def test_custom_user_fields(self, user):
        assert auth_api_client.email == 'emaitest@test.com'
        assert auth_api_client.username == 'testusername'
        assert auth_api_client.first_name == 'test_first_name'
        assert auth_api_client.last_name == 'test_last_name'
        assert not auth_api_client.is_staff
        assert auth_api_client.is_active
        assert isinstance(auth_api_client.date_joined, datetime)

    def test_custom_user_admin_fields(self, user_admin):
        assert auth_api_client_admin.email == 'emaitestadmin@test.com'
        assert auth_api_client_admin.username == 'testusernameadmin'
        assert auth_api_client_admin.first_name == 'test_first_name_admin'
        assert auth_api_client_admin.last_name == 'test_last_name_admin'
        assert auth_api_client_admin.is_staff
        assert auth_api_client_admin.is_active
        assert isinstance(auth_api_client_admin.date_joined, datetime)

    def test_book__str__(self, user):
        assert auth_api_client_admin.email in str(auth_api_client_admin)
