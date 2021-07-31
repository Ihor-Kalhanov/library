import pytest
import factory

from accounts.serializers import UserSerializer
from tests.factories import UserFactory, UserAdminFactory

pytestmark = pytest.mark.unit


class TestUserSerializer:

    def test_serializer_model(self):
        user = UserFactory.build()
        user_admin = UserAdminFactory.build()
        serializer_user = UserSerializer(user)
        serializer_user_admin = UserSerializer(user_admin)

        assert serializer_user.data and serializer_user_admin.data

    def test_serializer_valid_data(self):
        valid_serialized_data = factory.build(
            dict,
            FACTORY_CLASS=UserFactory
        )
        serializer = UserSerializer(data=valid_serialized_data)

        assert serializer.is_valid()
        assert not serializer.errors

    def test_serializer_invalid_data(self):
        invalid_serialized_data = factory.build(
            dict,
            FACTORY_CLASS=UserFactory
        )
        invalid_serialized_data['email'] = 'not valid email'
        serializer = UserSerializer(data=invalid_serialized_data)
        assert not serializer.is_valid()
        assert serializer.errors

