from django.shortcuts import render
from .models import Stargazer


def gitstar_list(request):
    stargazers = Stargazer.objects.all()
    context = {'stargazers': stargazers}
    return render(request, 'gitstar/gitstar_list.html', context)
