
from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'fourth_task/main.html',
                  {'header': 'Главная страница'})


def market(request):
    return render(request, 'fourth_task/market.html',
                  {'header': 'Игры',
                   'games': ['Atomic Heart',
                             'Cyberpank 2077',
                             'PayDay 2']})


def buy_menu(request):
    return render(request, 'fourth_task/buy_menu.html', {'header': 'Корзина'})