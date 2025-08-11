from django.shortcuts import render

from recetas_app.models import Receta


def receta(request, slug):
    receta = Receta.objects.get(slug=slug)
    contexto={
        'receta': receta,
    }

    return render(request, 'receta/receta.html', context=contexto)