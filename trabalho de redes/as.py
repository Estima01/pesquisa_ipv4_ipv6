
Ases = {}

#percorrer o arquivo e pegar os dados
with open('F:rib2022.txt' , 'r') as arquivo:
    dados = arquivo.readlines()

#percorrer os dados e pegar os ases
for linha in dados:
    prefixo, caminho = linha.split('|')[1], linha.split('|')[2]
    
    if "." in prefixo:
        # É IPv4
        protocolo = 'v4'
    elif ":" in prefixo:
        # É IPv6
        protocolo = 'v6'

    # Percorre cada AS no caminho
    for AS in caminho.split(" "):
        # Pega o próximo AS no caminho
        vizinho = AS[1:]

        # Atualiza o dicionário com o vizinho do AS atual
        if AS in Ases:
            Ases[AS][protocolo].add(vizinho)
        else:
            Ases[AS] = {'v4': set(), 'v6': set()}
            Ases[AS][protocolo].add(vizinho)

        # Atualiza o dicionário com o AS atual como vizinho do próximo AS
        if vizinho in Ases:
            Ases[vizinho][protocolo].add(AS)
        else:
            Ases[vizinho] = {'v4': set(), 'v6': set()}
            Ases[vizinho][protocolo].add(AS)

# Conta quantos ASes possuem IPv4 e IPv6
As_ipv4_ipv6 = 0
for AS in Ases:
    if Ases[AS]['v4'] and Ases[AS]['v6']:
        As_ipv4_ipv6 += 1

# Conta quantos ASes possuem IPv4
As_ipv4 = 0
for AS in Ases:
    if Ases[AS]['v4']:
        As_ipv4 += 1

# Conta quantos ASes possuem IPv6
As_ipv6 = 0
for AS in Ases:
    if Ases[AS]['v6']:
        As_ipv6 += 1

print("Total de AS que possuem IPV4 e IPV6: {}".format(As_ipv4_ipv6))
print("Total de AS que possuem IPV4: {}".format(As_ipv4))
print("Total de AS que possuem IPV6: {}".format(As_ipv6))
print("Total de AS: {}".format(len(Ases)))

#excrever os resultados em um arquivo
with open('quenia/rib2022.txt', 'w') as arquivo:
    arquivo.write(" Total de AS que possuem IPV4 e IPV6: {}".format(As_ipv4_ipv6))
    arquivo.write("Total de AS que possuem IPV4: {}".format(As_ipv4))
    arquivo.write("Total de AS que possuem IPV6: {}".format(As_ipv6))
    arquivo.write("Total de AS: {}".format(len(Ases)))
    