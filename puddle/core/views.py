from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm, LoginForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    return render(request, "core/index.html", {
        "items": items,
        "categories": categories
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

def sign_up(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/login/")
    else:
        form = SignupForm()

    return render(request, "core/signup.html", {
        "form": form
    })

def login(request):
    form = LoginForm()

    return render(request, "core/login.html", {
        "form": form
    })