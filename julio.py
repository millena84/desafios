
import requests
import json
import hashlib


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

print('#### Json: ', dadosRecebidos)
print('#### frase para traduzir: ', frase)

tamanho = len(frase)

# traducao da mensagem
for i in range(0, len(frase)):
    
    for j in range(0, len(listaAlfaCifr)):
        
        if frase[i] == listaAlfaCifr[j]:
            fraseTraduzida = fraseTraduzida + listaAlfaOrig[j]

print('#### tamanho da frase: ', tamanho)
print('#### frase traduzida: ', fraseTraduzida)

# fazer o resumo criptografico sha1:
#dadosRecebidos ["resumo_criptografico"] = hashlib.sha1(frase.encode())
cripSha1 = hashlib.sha1(frase.encode())
dadosRecebidos["resumo_criptografico"] = cripSha1.hexdigest()

#inclusao do texto decifrado no json para saida
dadosRecebidos["decifrado"] = fraseTraduzida

print('#### json antes da conversão: ', dadosRecebidos)

# serializar o json para postar:
jsonNovo = json.dumps(dadosRecebidos, indent=4)
#with open('answer.json', 'w') as f:
#    jsonNovo = json.dump(dadosRecebidos, f)

print('#### json depois da conversão: ', jsonNovo)

arquivo = open('answer.json', 'w')
arquivo.write(jsonNovo)

# postar a resposta
urlPost = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=89239c926b23ba1e2545d15574e745b3a1f9539a'

#post = requests.post(urlPost, jsonNovo)

filepath = '/home/ubuntu/answer.json'

post = requests.post(urlPost, files={'answer': open(filepath, 'rb')})



 
