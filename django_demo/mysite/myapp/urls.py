from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    # book/2
    path("book/<int:book_id>/", views.detail, name="detail"),
    path("add/", views.add_book, name="add_book"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
