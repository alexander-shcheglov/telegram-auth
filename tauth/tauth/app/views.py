from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect


def t_auth(request):
    return render(request, 'app/templates/hello.html', context=request.COOKIES)

def t_logout(request):
    if request.user.is_authenticated:
        profile = request.user.telegramuserprofile
        profile.token = None
        profile.save()
        logout(request)
    return redirect('/')

def can_login(request):
    if request.user.is_authenticated:
        return HttpResponse(status=200)
    return HttpResponse(status=401)
