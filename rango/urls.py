from django.http.response import HttpResponse
from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]

def about(request):
    return HttpResponse("Rango says here is the about page.")