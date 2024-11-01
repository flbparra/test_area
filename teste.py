import pandas as pd

# Lista para armazenar dados em cada iteração
dados_coletados = []

# Função ou loop para coleta de dados (aqui simulado como um loop simples)
for i in range(5):  # Exemplo com 5 iterações, mas pode ser qualquer número
    descricao = f'Terreno em condomínio à venda, {700 + i * 10}m²'  # Exemplo de dados
    preco = f'{350000 + i * 5000}'
    localizacao = 'Zona Industrial, SGCV Lote 13'
    quartos = 27 + i
    banheiros = 1
    vagas_garagem = 1
    outras_infos = 1

    # Dicionário com dados da iteração atual
    dados = {
        "Descrição": descricao,
        "Preço": preco,
        "Localização": localizacao,
        "Quartos": quartos,
        "Banheiros": banheiros,
        "Vagas de garagem": vagas_garagem,
        "Outras informações": outras_infos
    }
    
    # Adiciona os dados da iteração atual à lista
    dados_coletados.append(dados)

# Após a coleta de dados, cria o DataFrame
df = pd.DataFrame(dados_coletados)

# Exibe o DataFrame
print(df)