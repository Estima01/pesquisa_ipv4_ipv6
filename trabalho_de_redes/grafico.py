import matplotlib.pyplot as plt
import numpy as np
import re

# Inicializar as variáveis ​​que armazenarão os dados
ipv4_counts = []
ipv6_counts = []
both_counts = []
dates = []

# Iterar sobre cada um dos arquivos
for year in range(2011, 2023):
    # Ler o arquivo
    with open(f"quenia/rib{year}.txt", "r") as f:
        lines = f.readlines()

    # Inicializar as variáveis ​​de contagem para este ano
    ipv4_count = 0
    ipv6_count = 0
    both_count = 0

    # Iterar sobre cada linha do arquivo
    for line in lines:
        # Procurar pelo padrão de texto correspondente a cada tipo de AS
        ipv4_match = re.search(r"Total de AS que possuem IPV4: \d+", line)
        ipv6_match = re.search(r"Total de AS que possuem IPV6: \d+", line)
        both_match = re.search(r"Total de AS que possuem IPV4 e IPV6: \d+", line)

        # Se o padrão de texto foi encontrado, extrair o número e adicioná-lo à contagem
        if ipv4_match:
            ipv4_count += int(ipv4_match.group(0).split()[-1])
        if ipv6_match:
            ipv6_count += int(ipv6_match.group(0).split()[-1])
        if both_match:
            both_count += int(both_match.group(0).split()[-1])

    # Adicionar as contagens para este ano às listas de resultados
    ipv4_counts.append(ipv4_count)
    ipv6_counts.append(ipv6_count)
    both_counts.append(both_count)

    # Adicionar a data para este ano à lista de datas
    dates.append(f"17-03-{year}")

# Plotar o gráfico usando as listas de resultados e datas

plt.title("Quantidade de AS por ano Quenia")
plt.plot(dates, ipv4_counts, label="IPV4")
plt.plot(dates, ipv6_counts, label="IPV6")
plt.plot(dates, both_counts, label="Ambos")
plt.xlabel("Ano")
plt.ylabel("Quantidade de AS")
plt.legend()
plt.show()
#grafico em barras
plt.title("Quantidade de AS por ano Quenia")
plt.bar(dates, ipv4_counts, label="IPV4")
plt.bar(dates, ipv6_counts, label="IPV6")
plt.bar(dates, both_counts, label="Ambos")
plt.xlabel("Ano")
plt.ylabel("Quantidade de AS")
plt.legend()
plt.show()