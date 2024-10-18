from django.shortcuts import render

def index(request):
    context ={
        'title':'Blog Page',
    }
    return render(request, 'blog.html', context)