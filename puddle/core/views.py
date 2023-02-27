from django.shortcuts import render
from item.models import Category, Item

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

def category_detail(request, category_id):
    chosenCategory = Category.objects.get(id=category_id)
    items = Item.objects.filter(category=chosenCategory)

    return render(request, "core/category.html", {
        "category_name": chosenCategory.name,
        "items": items
    })