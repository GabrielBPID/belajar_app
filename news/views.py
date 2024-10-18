from django.shortcuts import render

def index(request):
    context ={
        'title':'News Page',
    }
    return render(request, 'news.html', context)