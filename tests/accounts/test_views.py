import pytest

from rest_framework import status
from rest_framework.utils import json
from model_bakery import baker

from accounts.models import User

pytestmark = pytest.mark.django_db


class TestViewsUsers:
    endpoint = '/api/accounts/users/'

    def test_get_all_users(self, api_client, auth_api_client):
        baker.make(User, _quantity=3)

        api_client.force_login(auth_api_client)
        response = api_client.get(
            self.endpoint
        )

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(json.loads(response.content), list)
        assert len(json.loads(response.content)) == 4

    def test_retrieve_user(self, auth_api_client, user):
        url = f'{self.endpoint}{user.id}/'

        response = auth_api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(json.loads(response.content), dict)

    def test_register_user_success(self, api_client):
        url = '/api/accounts/registration/'
        body_new_user = {
            "email": "test@test.com",
            "password1": "Maffia12345",
            "password2": "Maffia12345"
        }
        response = api_client.post(
            url,
            body_new_user,
            format='json',
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert "key" in json.loads(response.content)

    def test_register_user_invalid(self, api_client):
        url = '/api/accounts/registration/'
        body_new_user_invalid = {
            "email": "test@test.com",
            "password1": "Maffia12345",
        }
        response = api_client.post(
            url,
            body_new_user_invalid,
            format='json',
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert json.loads(response.content).get('password2') == ['This field is required.']

    def test_update_user(self, api_client, auth_api_client):
        url = f'{self.endpoint}{auth_api_client.id}/'
        body_new_user = {
            "id": auth_api_client.id,
            "email": auth_api_client.email,
            "username": "Updated",
            "first_name": "Updated",
            "last_name": "Updated"

        }
        api_client.force_login(auth_api_client)
        response = api_client.put(
            url,
            body_new_user,
            format='json',
        )
        response_content = json.loads(response.content)

        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response_content, dict)
        assert response_content.get('email') == body_new_user.get('email')
        assert response_content.get('username') == body_new_user.get('username')

    def test_update_user_invalid(self, api_client, auth_api_client):
        url = f'{self.endpoint}{auth_api_client.id}/'
        body_new_user_invalid = {
            "id": auth_api_client.id,
            "email": 'asdfghj',
            "username": "Updated",
            "first_name": "Updated",
            "last_name": "Updated"

        }
        api_client.force_login(auth_api_client)
        response = api_client.put(
            url,
            body_new_user_invalid,
            format='json',
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert isinstance(json.loads(response.content), dict)

    def test_delete_user(self, api_client, auth_api_client):
        url = f'{self.endpoint}{auth_api_client.id}/'

        api_client.force_login(auth_api_client)
        response = api_client.delete(
            url,
            format='json',
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_user_dont_exist(self, api_client, auth_api_client):
        url = f'{self.endpoint}141231241/'

        api_client.force_login(auth_api_client)
        response = api_client.delete(
            url,
            format='json',
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert "detail" in json.loads(response.content)
