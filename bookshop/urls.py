from django.urls import path
from bookshop.views import HomepageView, PublishersView, StoreView, UserLoginView, LogoutView, RegisterView, \
    StoreListView, StoreDetailView, StoreCreateView, AuthorsList, BooksList, BookDetailView

app_name = 'bookshop'
urlpatterns = [
    path("", HomepageView.as_view(), name="home-page"),
    path('authors/', AuthorsList.as_view(), name="authors-list"),
    path("publisher/", PublishersView.as_view(), name="publisher-page"),
    path("store/", StoreView.as_view(), name="store-page"),
    path("login/", UserLoginView.as_view(), name="login-page"),
    path("logout/", LogoutView, name="logout-page"),
    path("book-list/", BooksList.as_view(), name="books-list"),
    path("register/", RegisterView, name="register-page"),
    path("store_list/", StoreListView.as_view(), name="store-list"),
    path("store_create/", StoreCreateView.as_view(), name="store-create"),
    path("store_detail/<int:pk>", StoreDetailView.as_view(), name="store-detail"),
    path("book_detail/<int:pk>", BookDetailView.as_view(), name="book-detail"),

]
