from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # メインページ
    return render(request, 'cms/index.html')
    