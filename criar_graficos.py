import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dateutil.parser import parse 
import io
def validador_de_datas(data):
    try:
        parse(data)
        return True
    except:
        return False
def criar_grafico_bar(competencias,meta,grafico,tema) -> io.BytesIO:
    comp = [f'competência {i}' for i in range(1,6)]
    df = pd.Series(competencias,index=comp)
    #Criar gráfico
    cores = ['green' if competencias[i] >= meta else 'red' for i in range(5)]
    if grafico == 'bar':
        plt.figure(figsize=(10,15))
    else:
        plt.figure(figsize=(15,10))
    sns.set_style(tema)
    df.plot(kind = grafico,color = cores)
    plt.title('Gráfico de competências')
    if grafico == 'bar':
        plt.xlabel('competências')
        plt.ylabel('notas')
    else:
        plt.xlabel('notas')
        plt.ylabel('competências')
    buf = io.BytesIO()
    plt.savefig(buf,format = 'png')
    plt.close()
    buf.seek(0)
    return buf
def criar_grafico_linha(somas,ponteiros,datas,tema = 'darkgrid'):
    s = pd.Series(somas,index = datas)
    print(s.index)
    try:
        sns.set_style(tema)
    except ValueError:
        sns.set_style('darkgrid')
    plt.figure(figsize=(15,10))
    if ponteiros == "True":
        s.plot(x = s.index,y = s.values,kind = 'line',style='o',linestyle = '-')
    else:
        s.plot(x = s.index,y = s.values,kind = 'line')
    plt.title('Gráfico por notas')
    plt.xlabel('redações')
    plt.ylabel('notas')
    buf =  io.BytesIO()
    plt.savefig(buf,format = 'png')
    plt.close()
    buf.seek(0)
    return buf
    