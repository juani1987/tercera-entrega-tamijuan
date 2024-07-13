from django.shortcuts import render


def inicio(request):
    return render(request, "misdatos/index.html")


def products(request):
    return render(request, "misdatos/products.html")
