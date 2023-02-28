from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Item
from .forms import NewItemForm

# Create your views here.
def detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(id=item_id)[0:3]
    are_related_items = True if len(related_items) else False

    return render(request, "item/detail.html", {
        "item": item,
        "related_items": related_items,
        "are_related_items": are_related_items
    })

@login_required
def new(request):
    form = NewItemForm()

    return render(request, "item/new.html", {
        "form": form
    })