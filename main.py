import json

import requests


def texto(link):
    response = requests.get(link)
    return json.loads(response.text)


alavanca = True

while alavanca:
    print('''
Bem vindo a API do Covid-19!
Deseja consultar os casos por:

[1] Estado
[2] Paises
[3] Brasil
''')

    escolha = input('Digite uma opção: ')

    if escolha == '1':
        alavanca = False
        estados = (
            'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MS', 'MT', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
            'RJ',
            'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO')
        print('Lista de UF: https://bit.ly/3gMh3XL')
        estado = input('Digite o UF de algum estado: ').upper()
        if estado not in estados:
            print('Escolha um estado válido!')
        else:
            url = f'https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{estado.lower()}'
            json = texto(url)
            print(f'''
Estado/UF: {json['state']}/{json['uf']}
Casos: {json['cases']}
Mortes: {json['deaths']}
Suspeitos: {json['suspects']}
Atualizado: {json['datetime']}
''')

    elif escolha == '2':
        alavanca = False
        url = 'https://covid19-brazil-api.now.sh/api/report/v1/countries'
        json = texto(url)
        for pais in json['data']:
            print(f'''
País: {pais['country']}
Casos Totais: {pais['confirmed']}
Casos recuperados: {pais['recovered']}
Mortes: {pais['deaths']}
Atualizado: {pais['updated_at']}
''')

    elif escolha == '3':
        alavanca = False
        url = 'https://covid19-brazil-api.now.sh/api/report/v1/brazil'
        json = texto(url)
        json = json['data']
        print(f'''
País: {json['country']}
Casos totais: {json['confirmed']}
Casos recuperados: {json['recovered']}
Mortes: {json['deaths']}
Atualizado: {json['updated_at']}
''')

    else:
        print('Você digitou uma opção inválida, tente novamente!')

input('Pressione uma ENTER para fechar...')
