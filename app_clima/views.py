import datetime
import requests
from django.shortcuts import render
from app_clima.forms import CidadesForms

from dotenv import load_dotenv  # type: ignore
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def clima(cidade):
    url= f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    requisicao = requests.get(url)
    response = requisicao.json()
        
    clima = {
    "descricao" : response['weather'][0]['description'],
    "temperatura" : response['main']['temp'],
    "umidade" : response['main']['humidity']
    }
    
    return clima