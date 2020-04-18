
#dados = '{"dado1": 1, "dado2": "nome 2", "dado3": "descricao 3"}'

listaAlfaOrig = [" ",",",".",";",":","!","?","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
listaAlfaCifr = [" ",",",".",";",":","!","?","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


dadosRecebidos = {"numero_casas":5,"token":"89239c926b23ba1e2545d15574e745b3a1f9539a","cifrado":"n tsqd gjqnjaj ns xyfynxynhx ymfy n ithytwji rdxjqk. bnsxyts x. hmzwhmnqq?","decifrado":"","resumo_criptografico":""}

"""
dados = aspas + dadosRecebidos + aspas
dadosJson = json.loads(dados)
print(type(dadosJson))
print(dadosJson)
print(dadosJson["cifrado"])
"""

frase = dadosRecebidos["cifrado"]
frase = frase.lower()
fraseTraduzida = ""
print(dadosRecebidos)
print(frase)

tamanho = len(frase)

for i in range(0, len(frase)):
    
    for j in range(0, len(listaAlfaCifr)):
        
        if frase[i] == listaAlfaCifr[j]:
            fraseTraduzida = fraseTraduzida + listaAlfaOrig[j]

print(tamanho)
print(fraseTraduzida)

dadosRecebidos["decifrado"] = fraseTraduzida

print(dadosRecebidos)







