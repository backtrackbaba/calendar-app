from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EntryForm
from .models import Entry


# Create your views here.


def index(request):
    entries = Entry.objects.all()
    return render(request, 'mainapp/index.html', {'entries': entries})


def details(request, pk):
    try:
        entry = Entry.objects.get(pk=pk)
    except Entry.DoesNotExist:
        # raise Http404("No Model matches the given query.")
        return render(request, 'mainapp/error.html')

    return render(request, 'mainapp/details.html', {'entry': entry})


def add(request):
    if request.method == 'POST':

        form = EntryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entry.objects.create(
                name=name,
                date=date,
                description=description
            ).save()
            return HttpResponseRedirect('/')
        pass
    else:
        form = EntryForm()

    return render(request, 'mainapp/form.html', {'form': form})


def delete(request, pk):
    try:
        Entry.objects.get(pk=pk).delete()
    except:
        return render(request, 'mainapp/error.html')
    return HttpResponseRedirect('/')


def error(request):
    return render(request, 'mainapp/error.html')
