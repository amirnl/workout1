from django.shortcuts import render

def Equipment(request):

    return render(request,"Equipment.html",{})

def money(request):

    return render(request,"money.html",{})

def renew(request):

    return render(request,"renew.html",{})

def team(request):

    return render(request,"team.html",{})

def home(request):

    return render(request,"home.html",{})

