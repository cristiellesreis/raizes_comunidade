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
    codigo_condicao_clima = response['weather'][0]['id']
    print(codigo_condicao_clima)


    if codigo_condicao_clima >= 200 and codigo_condicao_clima < 300:
        detalhe = "Ah, os dias de tempestade... embora sejam desafiadores, também trazem a água essencial para as plantinhas! Durante essas chuvas intensas, é fundamental cuidar para que suas plantas não fiquem excessivamente molhadas, especialmente se estiverem em vasos."
    elif codigo_condicao_clima >= 300 and codigo_condicao_clima < 400:
        detalhe = "Hoje há uma chuva suave! Suas plantas estão sendo bem hidratadas pela água do céu, portanto, você não precisa se preocupar em regá-las."
    elif codigo_condicao_clima >= 500 and codigo_condicao_clima < 600:
        detalhe = "Dia chuvoso! Suas plantas estão devidamente hidratadas, então você pode deixar o regador de lado e se aconchegar em casa."
    elif codigo_condicao_clima >= 600 and codigo_condicao_clima < 700:
        detalhe = "Um dia de neve! Suas plantas estão protegidas pelo manto branco, mas não se esqueça de verificar a umidade do solo. Dê a elas um pouco de água quando a neve derreter, para garantir que continuem saudáveis."    
    elif codigo_condicao_clima >= 700 and codigo_condicao_clima < 800:
        detalhe = "Clima instável! Cuide da sua horta e não deixe de conferir a rega! Dê a elas um pouco de água para mantê-las firmes e saudáveis."
    elif codigo_condicao_clima == 800:
        detalhe = "Hoje é um dia ensolarado! Suas plantas vão adorar um bom banho de sol. Regue-as bem e não se esqueça de relaxar e curtir o jardim também."
    elif codigo_condicao_clima >= 800 and codigo_condicao_clima < 900:
        detalhe = "Um dia encoberto! Suas plantas não terão muita luz do sol, mas não se esqueça da rega. Forneça um pouco de água para mantê-las saudáveis."
    else:
        detalhe = "Clima instável! Cuide da sua horta e não deixe de conferir a rega! Dê a elas um pouco de água para mantê-las firmes e saudáveis."

        
    clima = {
    "descricao" : response['weather'][0]['description'].capitalize(),
    "temperatura" : response['main']['temp'],
    "max_temp" : response['main']['temp_max'],
    "min_temp" : response['main']['temp_min'],
    "umidade" : response['main']['humidity'],
    "icon" : response['weather'][0]['icon'],
    "detalhe": detalhe
    }
    
    return clima