from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterMovieForm, RegisterTestForm
from .models import Movie, Test
from django.contrib import messages
# Create your views here.

import json
from django.core.serializers.json import DjangoJSONEncoder

class HomeView(View):
    def get(self, request):
        all = Movie.objects.all()

        print(Movie.objects.values())
        print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')

        return render(request, 'home/index.html', {'movies':all})

    def post(self, request):

        return render(request, 'home/index.html')

class RegisterMovieView(View):

    def get(self, request):
        # form = RegisterMovieForm()

        # all = Movie.objects.all().values()
        # all = json.dumps(list(blog), cls=DjangoJSONEncoder)
        # all = Test.objects.values()
        # print(all)

        return render(request, 'home/registermovie.html')

    def post(self, request):
        form = RegisterMovieForm(request.POST)
        # print(form.test_name)

        cd = form.data
        # print(cd)
        Movie.objects.create(movie_name=cd['movie_name'],
                            director=cd['director'],
                            release_date=cd['release_date'],
                            Genre=cd['Genre'],
                            imdb=cd['imdb'],
                            )
        return redirect('home:movie_register')



class DetailView(View):

    def get(self, request, movie_id):
            movie = Movie.objects.get(id=movie_id)

            return render(request, 'home/detail.html', {'movie':movie})

class DeleteView(View):

    def get(self, request, movie_id):
            Movie.objects.get(id=movie_id).delete()
            messages.success(request, 'mevie deleted succ')
            return redirect('home:movie_register')


def ajax_data_view(request):
    all = Movie.objects.all().values()
    # data = json.dumps(list(all), cls=DjangoJSONEncoder)
    data = list(all)

    # data = {'message': 'This is data retrieved via AJAX GET request.'}
    print(data)
    return JsonResponse(data, safe=False)

