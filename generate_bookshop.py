import datetime
import random
from datetime import timedelta

from faker import Faker

faker = Faker()


def fake_test():
    pass
    # print(faker.().lower())
# print(faker.book())


def main():
    for _ in range(10):
        # Store.objects.create(name=faker.company(), is_active=random.choice([True, False]))
        # Author.objects.create_superuser(username=faker.first_name().lower(), password=faker.ean(length=8))
        # book = Book.objects.create(name=faker.first_name_male().lower(), pages=random.randint(100, 500),
        #                            price=random.uniform(4, 35),
        #                            rating=random.uniform(0, 5),
        #                            publisher=Publisher.objects.get(id=random.randint(1, 10)),
        #                            pubdate=faker.date())
        store = Store.objects.create(name=faker.company())
        for j in range(random.randint(1, 10)):
            book = Book.objects.get(id=random.randint(1, 51))
            store.books.add(book)
        store.save()


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "university.settings")
    application = get_wsgi_application()

    from bookshop.models import Author, Publisher, Book, Store

    main()
    # fake_test()
