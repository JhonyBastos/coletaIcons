import csv
import os

from django.shortcuts import render, redirect
from core.models import Icons
import requests
from bs4 import BeautifulSoup
# Create your views here.

def lista_icons(request):
    icon = Icons.objects.all()
    dados = {'icons':icon} #define como os dados da tabela serão chamados no html
    return render(request, 'listagem.html', dados)

def coleta_icons(request):
    if request.POST:
        os.system("clear")

        url = "http://themedesigner.in/demo/admin-press/main/icon-material.html"
        icons = []

        request = requests.get(url)
        soup = BeautifulSoup(request.text, "html.parser")

        icons = soup.find_all('span')
        with open('icons.csv', 'w', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(icons)


    return redirect('/listagem')