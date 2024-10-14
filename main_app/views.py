from django.shortcuts import render


def index(request):
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о нас и о магазине.",
    }
    return render(request, "about.html", context)
