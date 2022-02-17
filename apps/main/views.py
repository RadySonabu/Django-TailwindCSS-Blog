from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def index(request):

    if request.user.is_authenticated:
        return render(request, "main/index.html")
    else:
        return render(request, "main/landing.html")