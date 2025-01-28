from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "third_task/main.html")
def market(request):
    context = {
        'first': "Atomic Heart",
        'second': "Cyberpunk 2077",
        'third' : 'PayDay 2'}
    return render(request, "third_task/market.html", context)
def buy_menu(request):
    return render(request, "third_task/buy_menu.html")