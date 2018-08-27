from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import EntryForm
from .models import Entry


# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


def calendar(request):
    entries = Entry.objects.filter(author=request.user)
    return render(request, 'mainapp/calendar.html', {'entries': entries})


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
            return HttpResponseRedirect('/calendar')
        pass
    else:
        form = EntryForm()

    return render(request, 'mainapp/form.html', {'form': form})


def delete(request, pk):
    print("Method: ", request.method)
    if request.method == "GET" or request.method == "DELETE":
        entry = get_object_or_404(Entry, pk=pk)
        entry.delete()
    else:
        return HttpResponseRedirect('/calendar')


def error(request):
    return render(request, 'mainapp/error.html')


# def login(request):
#     return render(request, 'mainapp/registration/login.html')
#
#
# def logout(request):
#     return render(request, 'mainapp/registration/logout.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/calendar')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
