from django.shortcuts import render

def com (req):
    return render (req,"components.html")

def ind (req):
    return render (req,"index.html")