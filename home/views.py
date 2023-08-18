from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import BaseDetailView

from .forms import RegisterMovieForm, MovieUpdateForm
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
    # print(data)
    return JsonResponse(data, safe=False)

class ajax_data_edit_view(View):

    def get(self,request):
        print(request.GET)

        movie_id = int(request.GET.get("movie_id"))

        print(movie_id)

        all = Movie.objects.all().values()
        # data = json.dumps(list(all), cls=DjangoJSONEncoder)
        list_data = list(all)
        data = {}
        for item in list_data:
            if movie_id == item['id']:
                data = item
        print(movie_id + 1000000)
        print(data)

        # data = {'message': 'This is data retrieved via AJAX GET request.'}
        # print(data)
        return JsonResponse(data, safe=False)

    def post(self, request):
        print('hiiiiiii Post Ajax')
        # print(movie_id + 300000)
        print(request.POST.get("movie_id"))
        print(request.POST)
        movie_id = int(request.POST.get("movie_id"))
        movie = Movie.objects.get(id=movie_id)

        movie.save()
        print(movie.movie_name)

        form = MovieUpdateForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()

        return redirect('#')




class EditView(View):

    def get(self, request,movie_id):

        # Movie.objects.get(id=movie_id).delete()
        # messages.success(request, 'mevie deleted succ')
        #
        print(movie_id)
        print(movie_id)
        print(movie_id)
        print(movie_id)
        print(movie_id)

        return render(request, 'home/edit.html')


    def post(self, request,movie_id):

        print("post movie id")
        return redirect('home:movie_register')
