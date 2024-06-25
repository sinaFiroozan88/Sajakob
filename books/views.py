from django.shortcuts import render, redirect

from books.forms import BookForm
from books.models import Book


# Create your views here.
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            pages = form.cleaned_data['pages']
            cover = form.cleaned_data['cover']
            publisher = form.cleaned_data['publisher']
            owner = form.cleaned_data['owner']
            obj = Book.objects.create(title=title, author=author, pages=pages, cover=cover, publisher=publisher,
                                      owner=owner)
            obj.save()
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'books/add_book.html', context)


def remove_book(request, author_id):
    obj = Book.objects.get(pk=author_id)
    obj.delete()
    return redirect("list_books")


def list_books(request):
    obj = Book.objects.all()
    context = {'objects': obj}
    return render(request, 'books/list_book.html', context)
