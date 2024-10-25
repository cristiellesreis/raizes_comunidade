from django.shortcuts import render
import requests
from datetime import date

API_KEY = "inserir chave"


def fases_lua(cidade):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{cidade}/{date.today()}?unitGroup=us&key={API_KEY}&include=days&&elements=moonphase,datetime"
    requisicao = requests.get(url)
    response = requisicao.json()
    print(response)
    codigo_fase_lua = response['days'][0]['moonphase']

    fases_lua = {}
    if codigo_fase_lua >= 0 and codigo_fase_lua < 0.25:
        fases_lua={
            "fase": "Lua Nova",
            "descricao": "Durante a lua nova, é aconselhável interromper as atividades de plantio e colheita. Aproveite esse tempo para dedicar-se ao planejamento e à preparação do seu jardim. É uma oportunidade ideal para elaborar novos designs, criar novas áreas de cultivo e acondicionar o solo para futuras plantações. Este período representa uma fase de renovação e preparação para os ciclos lunares que virão.",
            "imagem_lua": "https://assets.hgbrasil.com/weather/icons/moon/new.png"

        }
    elif codigo_fase_lua >= 0.25 and codigo_fase_lua < 0.5:
            fases_lua={
            "fase": "Lua Crescente",
            "descricao": "Na fase crescente da lua, é o momento ideal para semear plantas que produzem frutos e sementes, como tomates, pimentões e abóboras. Essa fase favorece o crescimento e o desenvolvimento das plantas, por isso, foque em cultivar aquelas que você deseja ver prosperar.",
            "imagem_lua": "https://assets.hgbrasil.com/weather/icons/moon/waxing_crescent.png"
        }
            
    elif codigo_fase_lua >= 0.5 and codigo_fase_lua < 0.75:
            fases_lua={
            "fase": "Lua Cheia",
            "descricao": "Durante a lua cheia, é o momento perfeito para a colheita de vegetais e ervas. Nessa fase, as plantas geralmente atingem seu pico de maturação, resultando em produtos de excelente qualidade. Aproveite essa oportunidade para desfrutar dos frutos do seu trabalho no jardim.",
            "imagem_lua": "https://assets.hgbrasil.com/weather/icons/moon/full.png"
            
        }
    
    elif codigo_fase_lua >= 0.75 and codigo_fase_lua <= 1:
            fases_lua={
            "fase": "Lua Minguante",
            "descricao": "Na fase minguante da lua, é hora de se dedicar à manutenção e ao cuidado do solo. Este é um período ideal para realizar podas de limpeza, remover ervas daninhas e fertilizar a terra. Além disso, é um bom momento para transplantar plantas, pois a lua minguante favorece o crescimento das raízes.",
            "imagem_lua": "https://assets.hgbrasil.com/weather/icons/moon/waning_crescent.png"
        }
            
    print(fases_lua)
    return fases_lua
