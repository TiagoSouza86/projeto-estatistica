dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]
def limpar_dados () :
# Retorne uma lista apenas com int ou float
    pass
def calcular_media (lista) :
    for i in lista:
        soma = 0
        termos = 0
        soma += i
        termos += 1
        media = soma / termos
        return media
        
def calcular_mediana () :
    pass
def calcular_variancia () :
    pass
def obter_extremos () :
    pass
dados = limpar_dados ( dados_sujos )
print ( f" Dados processados : { dados }")