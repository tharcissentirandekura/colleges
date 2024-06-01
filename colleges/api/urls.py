from django.urls import path
from . import views

app_name = 'colleges'
urlpatterns = [
    path(
        '',
        views.home,
        name='home'
    ),
    path(
        'colleges/',
        views.CollegeListCreate.as_view(),
        name='create-view-create'
    ),#creatig a path for the CollegeListCreate view

    path(
        'colleges/<int:pk>/',
        views.CollegeRetrieveUpdateDestroy.as_view(),
        name='update-delete-retrieve'
    ),#creating a path for the CollegeRetrieveUpdateDestroy view

    path(
        'colleges/<str:name>/',
        views.CollegeRetrieveUpdateDestroy.as_view(),
        name='update-delete-retrieve'
    ),#search by name of college

    path(
        'colleges/<str:location>/',
        views.CollegeRetrieveUpdateDestroy.as_view(),
        name='update-delete-retrieve'
    ), # search by location of college

]