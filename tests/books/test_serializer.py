import pytest
import factory

from books.serializers import Bookserializer
from tests.factories import BookFactory

pytestmark = pytest.mark.unit

class TestBookSerializer:

    def test_serializer_model(self):
        book = BookFactory.build()
        serializer = Bookserializer(book)

        assert serializer.data

    def test_serializer_data(self):
        valid_serialized_data = factory.build(
            dict,
            FACTORY_CLASS=BookFactory
        )
        serializer = Bookserializer(data=valid_serialized_data)

        assert serializer.is_valid()
        assert not serializer.errors







