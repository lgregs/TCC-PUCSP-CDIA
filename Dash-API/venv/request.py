import requests

# URL da sua API Flask
url_api = 'http://localhost:5000/api/vendas'

# Fazendo uma requisição GET à API
response = requests.get(url_api)

# Verificando se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Convertendo a resposta para JSON
    data = response.json()
    print("Dados da API:")
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")
