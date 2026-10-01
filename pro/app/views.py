from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
# function based

# def Home(request):
#
#
#     if(request.method=="GET"):
#
#
#         return HttpResponse("Welcome to Django")



#Define index view  returns message "Index page"

# def Index(request):
#     if(request.method=="GET"):
#
#         return HttpResponse("Index Page")


# class based

class Home(View):
    def get(self,request):
        return HttpResponse("welcome to django")


class Index(View):
    def get(self,request):
        return HttpResponse("Index Page")

