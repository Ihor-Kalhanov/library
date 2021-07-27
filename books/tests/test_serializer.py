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
            "relase_date": book.relase_date,
            "created_at": book.created_at,
            "updated_at": book.updated_at

        }
        serializer = Bookserializer(book)
        assert serializer.data == expected_serialized_data
        # assert serializer.is_valid()




