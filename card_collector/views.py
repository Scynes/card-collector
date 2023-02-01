from django.shortcuts import render

from card.models import Card

def index(request):
    cards = Card.objects.all()
    return render(request, 'index.html', { 'cards': cards })
