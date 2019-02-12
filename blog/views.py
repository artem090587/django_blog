from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse('<h3>Hello from Django!</h3>')

def index(request):
    if request.method == 'GET':
        return render(request, 'blog/index.html', {})