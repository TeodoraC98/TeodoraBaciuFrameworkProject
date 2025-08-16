from django.shortcuts import render
from .management.commands.setup_role import Command
def home(request):
    comand_create_grout=Command().handle()
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

