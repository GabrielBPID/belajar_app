from django.shortcuts import render

def index(request):
    context ={
        'title':'App Django',
    }
    return render(request, 'index.html', context)