

import requests
import json

# requisita o json na url para fazer a conversao
urlToken="https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=89239c926b23ba1e2545d15574e745b3a1f9539a"

r = requests.get(urlToken)
dadosRecebidos = r.json()


# de-para da criptografia
listaAlfaOrig = [" ",",",".",";",":","!","?","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
listaAlfaCifr = [" ",",",".",";",":","!","?","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


#dadosRecebidos = {"numero_casas":5,"token":"89239c926b23ba1e2545d15574e745b3a1f9539a","cifrado":"n tsqd gjqnjaj ns xyfynxynhx ymfy n ithytwji rdxjqk. bnsxyts x. hmzwhmnqq?","decifrado":"","resumo_criptografico":""}


frase = dadosRecebidos["cifrado"]
frase = frase.lower()
fraseTraduzida = ""
print(dadosRecebidos)
print(frase)

tamanho = len(frase)

# traducao da mensagem
for i in range(0, len(frase)):
    
    for j in range(0, len(listaAlfaCifr)):
        
        if frase[i] == listaAlfaCifr[j]:
            fraseTraduzida = fraseTraduzida + listaAlfaOrig[j]

print(tamanho)
print(fraseTraduzida)

#inclusao do texto decifrado no json para saida
dadosRecebidos["decifrado"] = fraseTraduzida

print(dadosRecebidos)











