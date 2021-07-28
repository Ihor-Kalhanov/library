import pytest
from books.serializers import Bookserializer
from books.tests.factories import BookFactory

pytestmark = pytest.mark.unit

class TestBookSerializer:

    def test_serialize_model(self):
        book = BookFactory.build()
        serializer = Bookserializer(book)

        assert serializer.data

    def test_serialize_data(self):
        book = BookFactory.build()
        expected_serialized_data = {
            "title": book.title,
            "descriprion": book.descriprion,
            "phone_number": book.phone_number,
            "created_at": book.created_at,
            "updated_at": book.updated_at
        }
        serializer = Bookserializer(data=expected_serialized_data)

        assert serializer.is_valid()
        assert serializer.data == expected_serialized_data





