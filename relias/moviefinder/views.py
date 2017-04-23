import requests

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Movie
from .forms import TitleForm
from .serializer import MovieSerializer

def index(request):
    error = None

    if request.method == 'POST':
        if 'delete' in request.POST:
            form = TitleForm()
            movie_to_delete = Movie.objects.get(id = request.POST['delete'])
            movie_to_delete.delete()
        else:
            form = TitleForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['movie_title']
                query = 'http://www.omdbapi.com/?t=' + title
                if form.cleaned_data['movie_year']:
                    query += "&y=" + form.cleaned_data['movie_year']
                r = requests.get(query)
                json = r.json()
                if json['Response'] == "True":
                    for k, v in json.items():
                        if isinstance(v, list):
                            json[k] = repr(v)
                        if v == 'N/A':
                            json[k] = None
                    serializer = MovieSerializer(data=json)
                    if serializer.is_valid():
                        serializer.save()
                        return HttpResponseRedirect('/')
                    else:
                        print (serializer.errors)
                else:
                    error = json['Error']

    else:
        form = TitleForm()

    latest_movies = Movie.objects.order_by('-id')
    context = {'form': form, 'latest_movies': latest_movies, 'error': error}

    return render(request, 'moviefinder/index.html', context)
