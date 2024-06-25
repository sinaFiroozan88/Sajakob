from django.shortcuts import render, redirect
from authors.forms import AuthorForm
from authors.models import Author


# Create your views here.
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST or None, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            obj = Author(name=name, image=image)
            obj.save()
    else:
        form = AuthorForm()
    context = {'form': form}
    return render(request, 'authors/add_author.html', context)


def remove_author(request, author_id):
    obj = Author.objects.get(pk=author_id)
    obj.delete()
    return redirect("list_authors")


def list_author(request):
    obj = Author.objects.all()
    context = {'objects': obj}
    return render(request, 'authors/list_author.html', context)
