from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect


# Create your views here.


def index(request):
    book_list = Book.objects.all()
    context = {"book_list": book_list}
    return render(request, "myapp/index.html", context)


def detail(request, book_id):
    # Your view logic here
    book = Book.objects.get(id=book_id)
    return render(request, "myapp/detail.html", {"book": book})


def add_book(request):
    if request.method == "POST":
        name = request.POST.get(
            "name",
        )
        desc = request.POST.get(
            "desc",
        )
        price = request.POST.get(
            "price",
        )
        book_image = request.FILES["book_image"]
        book = Book(name=name, desc=desc, price=price, book_image=book_image)
        book.save()

    return render(request, "myapp/add_book.html")


def update(request, id):
    book = Book.objects.get(id=id)

    if request.method == "POST":
        form = BookForm(
            request.POST, request.FILES, instance=book
        )  # Correct the order of arguments
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = BookForm(instance=book)

    return render(request, "myapp/edit.html", {"form": form, "book": book})


def delete(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect("/")

    return render(request, "myapp/delete.html")
