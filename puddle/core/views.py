from django.shortcuts import render
from item.models import Category

# Create your views here.
def index(request):
    return render(request, "core/index.html", {
        "message": "Hello World"
    })

def contact(request):
    return render(request, "core/contact.html")

def browse(request):
    allCategories = Category.objects.all()

    return render(request, "core/browse.html", {
        "categories": allCategories
    })