from django.shortcuts import render
from cats.models import Cat
from .models import Drink, Food, Treats, Notice


def index(request):
    """" A view to return the index page """
    drinks = Drink.objects.all()
    cats = Cat.objects.all()
    food = Food.objects.all()
    treats = Treats.objects.all()
    notice = Notice.objects.all()

    context = {
        'drinks': drinks,
        'cats': cats,
        'food': food,
        'treats': treats,
        'notice': notice,
        'page': 'cafe'
    }
    return render(request, 'home/index.html', context)
