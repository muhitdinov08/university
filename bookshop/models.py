from django.contrib.auth.models import AbstractUser
from django.db import models


class AbtractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(AbstractUser):
    GENDER_CHOICE = [
        ('m', 'Male'),
        ('f', 'Female'),
    ]

    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.username


class Publisher(AbtractBaseModel):
    name = models.CharField(max_length=86)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Book(AbtractBaseModel):
    name = models.CharField(max_length=56)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author, related_name="books")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    pubdate = models.DateField()

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
