from django.urls import path
from . import views

app_name ='home'
urlpatterns = [
    path('index', views.HomeView.as_view(), name='home'),
    path('', views.RegisterMovieView.as_view(), name='movie_register'),
    path('detail/<int:movie_id>/', views.DetailView.as_view(), name= 'details'),
    path('delete/<int:movie_id>/', views.DeleteView.as_view(), name='delete'),
    path('registermovie/data/', views.ajax_data_view, name='movie_register_ajax'),

    path('edit/<int:movie_id>', views.EditView.as_view(), name='edit'),
    path('edit/ajax/', views.ajax_data_edit_view.as_view(), name='edit_ajax_get'),

]