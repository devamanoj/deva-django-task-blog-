from django.shortcuts import render
from .models import Posts,Comment
from django.views.generic.edit import CreateView

# Create your views here.



def Home(request):
    data = Posts.objects.all().order_by("-time")[:3]
    return render(request, "deva_app/home.html", {"data": data})

def details(request,pk):
    posts_details = Posts.objects.get(slug=pk)
    return render(request,"deva_app/postdetails.html",{"post":posts_details})

def all_details(request):
    data = Posts.objects.all()
    return render(request,"deva_app/details.html",{"data":data})

class FormViews(CreateView):
    model = Posts
    template_name = "deva_app/forms.html"
    success_url = "forms"
    fields = "__all__"


class commentCreateView(CreateView):
    model = Comment
    template_name = "deva_app/comments.html"
    fields = '__all__'
    success_url ='/comments' 