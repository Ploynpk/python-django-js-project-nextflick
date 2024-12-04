from django.urls import path
from . import views

# create new url
urlpatterns = [
    # home url 
    path('', views.index, name='index'),
    # # login
    # path('login', views.login, name='login'),
    # # signup
    # path('signup' , views.signup, name='signup'),
    # # movie path with specific 
    # path('movie/<str:pk>/' , views.movie, name='movie'),
    # # list genere with specific 
    # path('genre/<str:pk>/' , views.genre, name='genre'),
    # # my fav list
    # path('my-list', views.my_list, name='my-list'),
    # # add to list 
    # path('add-to-list' , views.add_to_list, name='add-to-list'),
    # # search
    # path('search', views.search, name='search'),
]
