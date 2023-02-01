from django.shortcuts import render

def index(request):
    return render(request, 'card_details.html')
