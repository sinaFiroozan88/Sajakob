from django.shortcuts import render, redirect
from genres.forms import GenreForm
from genres.models import Genre


# Create your views here.
def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST or None, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            obj = Genre(name=name, description=description)
            obj.save()
    else:
        form = GenreForm()
    context = {'form': form}
    return render(request, 'genres/add_genre.html', context)


def remove_genre(request, genre_id):
    obj = Genre.objects.get(pk=genre_id)
    obj.delete()
    return redirect("list_genres")


def list_genres(request):
    obj = Genre.objects.all()
    context = {'objects': obj}
    return render(request, 'genres/list_genre.html', context)
