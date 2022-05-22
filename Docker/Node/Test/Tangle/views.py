from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return redirect("http://127.0.0.1:8000/admin")
# Create your views here.
