from django.shortcuts import render
from .models import Stargazer


def gitstar_list(request):
    stargazers = Stargazer.objects.all()
    if stargazers:
        context = {'stargazers', stargazers}
    else:
        context = {}
    return render(request, 'gitstar/gitstar_list.html', context)
