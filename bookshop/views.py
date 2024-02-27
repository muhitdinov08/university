from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, DetailView, TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin
from bookshop.forms import PublisherCreateForm, StoreCreateForm, LoginForm, UserRegisterModelForm

from bookshop.models import Publisher, Store, Author, Book


# Create your views here.


class CustomLoginRequiredMixin(LoginRequiredMixin):

    def get_permission_denied_message(self):
        messages.set_level()
        return super().get_permission_denied_message()


class HomepageView(View):
    def get(self, request):
        return render(request, "bookshop/home.html")


class PublishersView(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        form = PublisherCreateForm()
        context = {
            "publishers": publishers,
            "form": form
        }
        return render(request, "bookshop/publisher.html", context=context)

    def post(self, request):
        publishers = Publisher.objects.all()
        form = PublisherCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookshop:publisher-page')
        else:
            return render(request, "bookshop/publisher.html", context={
                "publishers": publishers,
                "forms": form
            })


class StoreView(View):
    def get(self, request):
        store = Store.objects.all()
        form = StoreCreateForm()
        context = {
            "store": store,
            "form": form
        }
        return render(request, "bookshop/store.html", context=context)

    def post(self, request):
        stores = Store.objects.all()
        form = StoreCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "bookshop/store.html")
        else:
            return render(request, "bookshop/publisher.html", context={
                "publishers": stores,
                "forms": form
            })


class StoreListView(ListView):
    model = Store
    stores = Store.objects.all()
    context_object_name = "stores"
    template_name = "bookshop/store_list.html"


class UserLoginView(TemplateView):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                messages.success(request, 'User successfully logged in')
                return redirect('bookshop:home-page')
            else:
                messages.warning(request, 'User not found')
        else:
            return render(request, 'bookshop/login.html', {'form': form})

    def get(self, request, **kwargs):
        form = LoginForm()
        return render(request, 'bookshop/login.html', {'form': form})


def LogoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('bookshop:home-page')
    else:
        return render(request, 'bookshop/logout.html')


def RegisterView(request):
    if request.method == "POST":
        form = UserRegisterModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User successfully registered")

            return redirect('bookshop:home-page')
        else:
            return render(request, 'bookshop/register.html', {'form': form})
    else:
        form = UserRegisterModelForm(request.GET)
        return render(request, 'bookshop/register.html', context={'form': form})


class StoreCreateView(View):
    def get(self, request):
        form = StoreCreateForm(request.GET)
        return render(request, 'bookshop/store_create.html', context={"form": form})

    def post(self, request):
        form = StoreCreateForm(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Store successfully created')
            form.save()
            return redirect('bookshop:store-list')
        else:
            return render(request, 'bookshop/store_create.html', {'form': form})


class StoreDetailView(DetailView):
    model = Store
    template_name = "bookshop/store_detail.html"
    context_object_name = "store"


class BookDetailView(DetailView):
    def get(self, request, **kwargs):
        book = Book.objects.get(id=kwargs['pk'])
        return render(request, 'bookshop/book-detail.html', {'book': book})


class AuthorsList(ListView):
    def get(self, request, **kwargs):
        authors = Author.objects.all()
        return render(request, 'bookshop/authors.html', context={"authors": authors})


class BooksList(ListView):
    def get(self, request, **kwargs):
        books = Book.objects.all()
        return render(request, 'bookshop/book_list.html', context={"books": books})
