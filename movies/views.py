from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core import exceptions
from .models import Movie


def movies(request):
    data = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': data})


def home(request):
    return HttpResponse('Home page')


def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})


def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect('/movies')

    return render(request, 'movies/add.html')


def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except exceptions.ObjectDoesNotExist:
        raise Http404('Movie does not exist')
    except exceptions.BadRequest:
        raise Http404('Movie does not found')
    except Exception:
        raise Http404('Movie does not found')
    movie.delete()
    return HttpResponseRedirect('/movies')
