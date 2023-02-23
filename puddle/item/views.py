from django.shortcuts import render

# Create your views here.
def detail(request, itemID):
    return render(request, "item/detail.html", {
        "id": itemID
    })