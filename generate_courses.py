import os


def main():
    for _ in range(100):
        teacher = Teacher.objects.create(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            degree=faker.random_element(elements=('master', 'bachelor', 'academic', 'drscience', 'phs')),
            age=faker.random_int(min=25, max=65),
            email=faker.email(),
        )

        speciality = Speciality.objects.create(
            name=faker.job(),
            code=faker.uuid4(),
            is_active=faker.boolean(),
            start_date=faker.date_between(start_date='-5y', end_date='today'),
            slug=faker.slug(),
        )

        subject = Subject.objects.create(
            name=faker.catch_phrase(),
            teacher=teacher,
        )
        subject.speciality.add(speciality)

if __name__ == '__main__':
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "university.settings")
    application = get_wsgi_application()
    from faker import Faker

    from courses.models import Subject, Teacher, Speciality

    faker = Faker()
    main()