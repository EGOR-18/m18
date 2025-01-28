from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "third_task/main.html")
def market(request):
    context = {
        'games': ['Atomic Heart',
                   'Cyberpank 2077',
                   'PayDay 2']}
    return render(request, "third_task/market.html", context)
def buy_menu(request):
    return render(request, "third_task/buy_menu.html")