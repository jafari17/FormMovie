from django import forms

class RegisterMovieForm(forms.Form):
    movie_name = forms.CharField(max_length=100)
    director = forms.CharField(max_length=100)
    Release_date = forms.CharField(max_length=100)
    Genre = forms.CharField(max_length=100)
    imdb = forms.CharField(max_length=100)


class RegisterTestForm(forms.Form):
    test_name = forms.CharField(max_length=100)
    director = forms.CharField(max_length=100)
    release_date = forms.IntegerField()
    genre = forms.CharField(max_length=100)
    imdb = forms.IntegerField()
