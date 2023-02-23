from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html", {
        "message": "Hello World"
    })

def contact(request):
    return render(request, "core/contact.html")