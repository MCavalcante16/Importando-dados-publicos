#Imports
import requests
import json

#Getting Json Data
#Sumario
url=requests.get('https://portalunico.siscomex.gov.br/classif/api/sumario')
sumario = url.json()

#Secao
for secao in sumario:
    all_url = 'https://portalunico.siscomex.gov.br/classif/api/nomenclatura/'

    #Capitulo
    for capitulo in secao['capitulos']:
        print(all_url + capitulo['codigo'])
        sleep(0.5)
        capitulo_url=requests.get(all_url + capitulo['codigo'])
        capitulo = capitulo_url.json()

        #Posicao
        for posicao in capitulo['filhos']:
            if (posicao['possuiFilhos']):
                print(all_url + posicao['codigo'])
                sleep(0.5)
                posicao_url = requests.get(all_url + posicao['codigo'])
                posicao = posicao_url.json()

                #Subposicao
                for subposicao in posicao['filhos']:
                    if (subposicao['possuiFilhos']):
                        print(all_url + subposicao['codigo'])
                        sleep(0.5)
                        subposicao_url = requests.get(all_url + subposicao['codigo'])
                        subposicao = subposicao_url.json()

                        #Item
                        for item in subposicao['filhos']:
                            if (item['possuiFilhos']):
                                print(all_url + item['codigo'])
                                sleep(0.5)
                                item_url = requests.get(all_url + item['codigo'])
                                item = item_url.json()

                                #Subitem
                                for subitem in item['filhos']:
                                    if (subitem['possuiFilhos']):
                                        print(all_url + subitem['codigo'])
                                        sleep(0.5)
                                        subitem_url = requests.get(all_url + subitem['codigo'])
                                        subitem = subitem_url.json()


with open('tipi_table.txt', 'w') as tipi_table:
    json.dump(sumario, tipi_table)