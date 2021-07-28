import factory
from faker import Factory as FakerFactory
from books.models import Book
from django.utils.timezone import now
import datetime
faker = FakerFactory.create()

class BookFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.name())
    descriprion = factory.LazyAttribute(lambda x: faker.name())
    phone_number = factory.LazyAttribute(lambda x: faker.random_number(digits=10))
    created_at = factory.LazyAttribute(lambda x: datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))
    updated_at = factory.LazyAttribute(lambda x: datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))

    class Meta:
        model = Book



