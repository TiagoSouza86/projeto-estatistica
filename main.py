dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]
   
def limpar_dados(lista):
    # Retorna apenas se o item for do tipo int ou float
    return [item for item in lista if isinstance(item, (int, float))]

dados_limpos = limpar_dados(dados_sujos)
print(dados_limpos)
    # Retorne uma lista apenas com int ou float
pass
def calcular_media () :
    pass
def calcular_mediana () :
    pass
def calcular_variancia () :
    pass
def obter_extremos () :
    pass
dados = limpar_dados ( dados_sujos )
print ( f" Dados processados : { dados }")