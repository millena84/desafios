# Criptografia de Júlio César
# Segundo o Wikipedia, criptografia ou criptologia (em grego: kryptós, “escondido”, e gráphein, “escrita”) é o estudo e prática de princípios e técnicas para comunicação segura na presença de terceiros, chamados “adversários”. Mas geralmente, a criptografia refere-se à construção e análise de protocolos que impedem terceiros, ou o público, de lerem mensagens privadas. Muitos aspectos em segurança da informação, como confidencialidade, integridade de dados, autenticação e não-repúdio são centrais à criptografia moderna. Aplicações de criptografia incluem comércio eletrônico, cartões de pagamento baseados em chip, moedas digitais, senhas de computadores e comunicações militares. Das Criptografias mais curiosas na história da humanidade podemos citar a criptografia utilizada pelo grande líder militar romano Júlio César para comunicar com os seus generais. Essa criptografia se baseia na substituição da letra do alfabeto avançado um determinado número de casas. Por exemplo, considerando o número de casas = 3:
#
# Normal: a ligeira raposa marrom saltou sobre o cachorro cansado
#
# Cifrado: d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr
#
# Regras
# As mensagens serão convertidas para minúsculas tanto para a criptografia quanto para descriptografia.
# No nosso caso os números e pontos serão mantidos, ou seja:
# Normal: 1a.a
#
# Cifrado: 1d.d
#
# Escrever programa, em qualquer linguagem de programação, que faça uma requisição HTTP para a url abaixo:
#
# https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN
# Para encontrar o seu token , acesse a plataforma Codenation, faça o login e a informação estará na tela, conforme no exemplo abaixo:
#
#
#
# O resultado da requisição vai ser um JSON conforme o exemplo:
#
# {
# 	"numero_casas": 10,
# 	"token":"token_do_usuario",
# 	"cifrado": "texto criptografado",
# 	"decifrado": "aqui vai o texto decifrado",
# 	"resumo_criptografico": "aqui vai o resumo"
# }
# O primeiro passo é você salvar o conteúdo do JSON em um arquivo com o nome answer.json, que irá usar no restante do desafio.
#
# Você deve usar o número de casas para decifrar o texto e atualizar o arquivo JSON, no campo decifrado. O próximo passo é gerar um resumo criptográfico do texto decifrado usando o algoritmo sha1 e atualizar novamente o arquivo JSON. OBS: você pode usar qualquer biblioteca de criptografia da sua linguagem de programação favorita para gerar o resumo sha1 do texto decifrado.
#
# Seu programa deve submeter o arquivo atualizado para correção via POST para a API:
#
# https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN
# OBS: a API espera um arquivo sendo enviado como multipart/form-data, como se fosse enviado por um formulário HTML, com um campo do tipo file com o nome answer. Considere isso ao enviar o arquivo.
#
# O resultado da submissão vai ser sua nota ou o erro correspondente. Você pode submeter quantas vezes achar necessário, mas a API não vai permitir mais de uma submissão por minuto.
#
# OBS
# Neste estágio da aceleração não solicitamos que você nos envie o código do programa que você criou, mas recomendamos que você guarde uma cópia pois o mesmo pode ser solicitado nas próximas fases do processo.

import requests
import json
import hashlib

def reqJson(url):
    r = requests.get(url)
    dadosRecebidos = r.json()

    return dadosRecebidos

def deParaCripto(dadosRecebParaDePara):
    listaAlfaOrig = [" ", ",", ".", ";", ":", "!", "?", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    listaAlfaCifr = [" ", ",", ".", ";", ":", "!", "?", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                     "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e"]

    frase = dadosRecebParaDePara["cifrado"]
    frase = frase.lower()
    fraseTraduzida = ""

    print('#### frase para traduzir: ', frase)

    tamanho = len(frase)

    # traducao da mensagem
    for i in range(0, len(frase)):

        for j in range(0, len(listaAlfaCifr)):

            if frase[i] == listaAlfaCifr[j]:
                fraseTraduzida = fraseTraduzida + listaAlfaOrig[j]

    print('#### tamanho da frase: ', tamanho)
    print('#### frase traduzida: ', fraseTraduzida)
    dadosRecebParaDePara["decifrado"] = fraseTraduzida

    return dadosRecebParaDePara, fraseTraduzida


def resumoCripto(dadosRecebparaResumoCrip, frase):
    cripSha1 = hashlib.sha1(str.encode(frase))
    dadosRecebparaResumoCrip["resumo_criptografico"] = cripSha1.hexdigest()

    # inclusao do texto decifrado no json para saida

    print('#### json antes da conversão: ', dadosRecebparaResumoCrip)

    # serializar o json para postar:
    with open('answer.json', 'w') as jsonFile:
        json.dump(dadosRecebparaResumoCrip, jsonFile, indent=4)

    return dadosRecebparaResumoCrip


def postarJson(dadosRecebParaPostar):
    jsonNovo = json.dumps(dadosRecebParaPostar, indent=4)

    arquivo = open('answer.json', 'w')
    arquivo.write(jsonNovo)

    # postar a resposta
    urlPost = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=89239c926b23ba1e2545d15574e745b3a1f9539a'

    filepath = '/home/millena/Documentos/desafios/answer.json'

    post = requests.post(urlPost, files={'answer': open(filepath, 'rb')})

    return dadosRecebParaPostar


def main():
    urlToken = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=89239c926b23ba1e2545d15574e745b3a1f9539a"

    # requisita o json na url para fazer a conversao
    dadosRecebidosInicio = reqJson(urlToken)

    # de-para da criptografia
    dadosRecebidosFraseTradu, frasePura = deParaCripto(dadosRecebidosInicio)

    # fazer o resumo criptografico sha1:
    dadosRecebidosResumoCripto = resumoCripto(dadosRecebidosFraseTradu, frasePura)

    # serializar o json para postar:
    dadosRecebidosFinal = postarJson(dadosRecebidosResumoCripto)

    print('#### json depois da conversao: ', dadosRecebidosFinal)
    return


main()
