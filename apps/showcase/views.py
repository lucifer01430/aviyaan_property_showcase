from django.shortcuts import render

def showcase_home(request):
    return render(request, 'showcase/showcase_home.html')