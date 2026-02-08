from fastapi import FastAPI,HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from datetime import datetime
import io

from criar_graficos import criar_grafico_bar,criar_grafico_linha,validador_de_datas

class InfoServices(BaseModel):
    competencias:list[int]
    meta:int = 150
    tema_grafico:str = 'darkgrid'
    grafico:str = 'bar'
    nome:str = 'minha_imagem'
    tema_redacao:str = 'idosos'
    redacao:str = ' OI sou o melhor'
class InfoServicesLine(BaseModel):
    somas:list[int]
    tema:str = 'darkgrid'
    pointers:str = 'True'
    datas:list[str]
class InfoServicesLineMonth(BaseModel):
    somas:list[int]
    tema:str = 'darkgrid'
    pointers:str = "True"
    comeco:str
class InfoServicesLineVarious(BaseModel):
    somas:list[int]
    tema:str = 'darkgrid'
    pointers:str = "True"
    comeco:list[str]

app = FastAPI()

@app.post('/criar_graficos/barra')
def criar_grafico(dados:InfoServices):
    dados_a = criar_grafico_bar(dados.competencias,dados.meta,dados.grafico,dados.tema_grafico)
    headers = {'Content-Disposition':f'attachment; filename={dados.nome}.png'}
    return StreamingResponse(dados_a,media_type='image/png',headers=headers)
@app.post('/criar_graficos/linha/meses')
def criar_grafico_linha_meses(dados:InfoServicesLine):
    if len(dados.somas) == len(dados.datas) and len(dados.datas) >= 2:
        grafico = criar_grafico_linha(dados.somas,dados.pointers,dados.datas,dados.tema)
        header = {'Content-Disposition':'attachment; filename = imagem.png'}
        return StreamingResponse(grafico,media_type='image/png',headers = header)
    else:
        return HTTPException(400,'O número de meses é menor ou igual a 1 ou as médias das notas de cada mes estão erradas')
@app.post('/criar_grafico/linha/variado')
def gerador_grafico_resumo_variado(valores:InfoServicesLineVarious):
    lista = []
    for i in valores.comeco:
        try:
            if validador_de_datas(i):
                lista.append(i)   
        except:
            raise HTTPException(400,'Com os valores passados não dá para fazer um gráfico.')
                    
    header = {'Content-Disposition':'attachment; filename = imagem.png'}
    grafico_a = criar_grafico_linha(valores.somas,valores.pointers,valores.comeco,valores.tema)
    return StreamingResponse(grafico_a,media_type='image/png',headers = header)
