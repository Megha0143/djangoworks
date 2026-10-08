from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
from django.http import JsonResponse
from django.views import View
from .models import Movie
class Movielist(View):
    def get(self, request):
        s=list(Movie.objects.all().values())
        # print(s)
        # print(type(s))

        return JsonResponse(s,safe=False)



