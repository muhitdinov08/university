import datetime
from uuid import uuid4

from django.db import models
from django.utils.text import slugify


class AbtractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subject(AbtractModel):
    name = models.CharField(max_length=28, )
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name="subjects")
    speciality = models.ManyToManyField('Speciality', related_name="subjects")

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        db_table = "subject"

    def __str__(self):
        return f"{self.name}"


class Teacher(AbtractModel):
    Degree = [
        ("master", "Master"),
        ("bachelor", "Bachelor"),
        ("academic", "Academic"),
        ("drscience", "DrScience"),
        ("phs", "PhD"),
    ]

    first_name = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    degree = models.CharField(max_length=9, choices=Degree)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        db_table = "teacher"

    def __str__(self):
        return "{0}{1}".format(self.first_name, self.last_name)


class Speciality(AbtractModel):
    name = models.CharField(max_length=28)
    code = models.UUIDField(default=uuid4)
    is_active = models.BooleanField(default=False)
    start_date = models.DateField()
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Speciliality"
        verbose_name_plural = "Specilialities"
        db_table = "speciality"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify("-".join([self.start_date, self.name]))
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.name}"
