from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
def index(request):
    mypost=Blogpost.objects.all()
    return render(request, 'eblog/index.html',{'mypost':mypost})

def blogpost(request,id):
    post=Blogpost.objects.filter(post_id=id)
    return render(request, 'eblog/blogpost.html',{'post':post[0]})
