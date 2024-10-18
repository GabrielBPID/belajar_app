from django.shortcuts import render

def index(request):
    context ={
        'title':'About Page',
    }
    return render(request, 'about.html', context)