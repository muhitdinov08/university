from django.core.exceptions import ValidationError
from django.forms import ModelForm
from bookshop.models import Publisher, Store, Author, Book
from django import forms


class PublisherCreateForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ["name", "is_active"]


class StoreCreateForm(ModelForm):
    name = forms.CharField(max_length=100)
    books = forms.ModelMultipleChoiceField(queryset=Book.objects.all())

    class Meta:
        model = Store
        fields = ["name", "books"]


class UserRegisterModelForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)

    def save(self, commit=True):
        user = super().save(commit)
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 == password2:
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Passwords must be match")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Author
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=28)
    password = forms.CharField(max_length=28)
