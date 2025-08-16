from django.shortcuts import render
from .management.commands.setup_role import Command
def home(request):
    return render(request,"app/home.html")

