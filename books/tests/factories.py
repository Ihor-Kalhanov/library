import factory
from faker import Factory as FakerFactory
from books.models import Book
from django.utils.timezone import now
import datetime
faker = FakerFactory.create()

class BookFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.name())
    descriprion = factory.LazyAttribute(lambda x: faker.name())
    relase_date = factory.LazyAttribute(lambda x: now())
    created_at = factory.LazyAttribute(lambda x: now())
    updated_at = factory.LazyAttribute(lambda x: now())
    class Meta:
        model = Book



