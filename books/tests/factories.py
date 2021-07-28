import factory
from faker import Factory as FakerFactory
from books.models import Book
from model_bakery import baker
import datetime
faker = FakerFactory.create()

class BookFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.name())
    descriprion = factory.LazyAttribute(lambda x: faker.name())
    phone_number = factory.LazyAttribute(lambda x: faker.numerify(text='###'))
    created_at = factory.LazyAttribute(lambda x: datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
    updated_at = factory.LazyAttribute(lambda x: datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))

    class Meta:
        model = Book



