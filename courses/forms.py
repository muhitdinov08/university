from django import forms

from courses.models import Speciality, Teacher


class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=36)
    date = forms.DateField()
    is_active = forms.BooleanField()

    def save(self):
        name = self.cleaned_data["name"]
        date = str(self.cleaned_data["date"])
        is_active = self.cleaned_data["is_active"]
        Speciality.objects.create(name=name, start_date=date, is_active=is_active)


class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=28)
    last_name = forms.CharField(max_length=28)
    degree = forms.CharField(max_length=15)
    age = forms.IntegerField()
    email = forms.EmailField()

    def save(self):
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        degree = self.cleaned_data["degree"]
        age = self.cleaned_data["age"]
        email = self.cleaned_data["email"]
        Teacher.objects.create(first_name=first_name, last_name=last_name, degree=degree, age=age,
                               email=email)
