import factory
from faker import Factory as FakerFactory

from accounts.models import User
from books.models import Book

import datetime
faker = FakerFactory.create()

class BookFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.name())
    description = factory.LazyAttribute(lambda x: faker.name())
    phone_number = factory.LazyAttribute(lambda x: faker.numerify(text='###'))
    created_at = factory.LazyAttribute(lambda x: datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
    updated_at = factory.LazyAttribute(lambda x: datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))

    class Meta:
        model = Book


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda x: f'john{x}')
    email = factory.LazyAttribute(lambda x: f'{x.username}@example.org')
    first_name = factory.LazyAttribute(lambda x: faker.name())
    last_name = factory.LazyAttribute(lambda x: faker.name())
    is_staff = False
    is_active = True
    date_joined = factory.LazyAttribute(lambda x: datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))

    class Meta:
        model = User

class UserAdminFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda x: f'john{x}')
    email = factory.LazyAttribute(lambda x: f'{x.username}@example.org')
    first_name = factory.LazyAttribute(lambda x: faker.name())
    last_name = factory.LazyAttribute(lambda x: faker.name())
    is_staff = True
    is_active = True
    date_joined = factory.LazyAttribute(lambda x: datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))

    class Meta:
        model = User



