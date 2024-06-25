from django.shortcuts import render, redirect

from publishers.forms import PublisherForm
from publishers.models import Publisher


# Create your views here.
def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST or None, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            logo = form.cleaned_data['logo']
            obj = Publisher(name=name, logo=logo)
            obj.save()
    else:
        form = PublisherForm()
    context = {'form': form}
    return render(request, 'publishers/add_publisher.html', context)


def remove_publisher(request, publisher_id):
    obj = Publisher.objects.get(pk=publisher_id)
    obj.delete()
    return redirect("list_publishers")


def list_publishers(request):
    obj = Publisher.objects.all()
    context = {'objects': obj}
    return render(request, 'publishers/list_publisher.html', context)
