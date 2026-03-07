dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]

def calcular_media (lista) :
    for i in lista:
        soma = 0
        termos = 0
        soma += i
        termos += 1
        media = soma / termos
        return media
        
   
def limpar_dados(lista):
    # Retorna apenas se o item for do tipo int ou float
    return [item for item in lista if isinstance(item, (int, float))]

dados_limpos = limpar_dados(dados_sujos)
print(dados_limpos)


def calcular_variancia () :
    pass
def obter_extremos () :
    pass
dados = limpar_dados ( dados_sujos )
print ( f" Dados processados : { dados }")
print("Verificado por:Arthur Franco")

dados_limpos = [10, 20, 30, 40, 50, 15, 25]

def calcular_mediana(lista):
    
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2
    
    
    if n % 2 != 0:
      
        return lista_ordenada[meio]
    else:
       
        return (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2

resultado = calcular_mediana(dados)
print(f"Lista ordenada: {sorted(dados)}")
print(f"Mediana: {resultado}")
