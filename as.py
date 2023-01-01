import matplotlib.pyplot as plt
import json

with open('rib_20110317_1619.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

with open('IP_AS.json' , 'w') as arquivo:

    arquivo.write('[\n')
    for linha in linhas:
        if '|' in linha:
            if '.' in linha.split('|')[1]:
                arquivo.write('\t  "IPv4", {')
                arquivo.write('\t "{}": "{}"'.format(linha.split('|')[1], linha.split('|')[2]))
                arquivo.write('\t},\n')
            elif ':' in linha.split('|')[1]:
                arquivo.write('\t "IPv6", {')
                arquivo.write('\t"{}": "{}"'.format(linha.split('|')[1], linha.split('|')[2]))
                arquivo.write('\t},\n')
    arquivo.write(']')
    arquivo.close()

with open('IP_AS.json', 'r') as arquivo:
    dados = json.load(arquivo)

ipv4 = []
ipv6 = []

for linha in dados:
    if 'IPv4' in linha:
        ipv4.append(linha)
    elif 'IPv6' in linha:
        ipv6.append(linha)

#grafico em barras de IPv4 e IPv6
plt.bar(['IPv4', 'IPv6'], [len(ipv4), len(ipv6)])
plt.show()
#grafico de pizza de IPv4 e IPv6
plt.pie([len(ipv4), len(ipv6)], labels=['IPv4', 'IPv6'], autopct='%1.1f%%')
#legenda
plt.show()