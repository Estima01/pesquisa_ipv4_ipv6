# pesquisa_ipv4_ipv6
<h1> Analise de topologia IPv4 e IPv6 </h1>

O código acima feito em Python, foi separado em duas etapas, a primeira a de filtragem, após obter os arquivos Bz2 convertidos para TXT via BGPSCANNER, feito no linux, é inserido seu caminho no código. Na qual o mesmo percorre o arquivo TXT e cria um dicionario fazendo uma relçao dos caminhos, e após isso ele indereça em um SET, na qual pode ser via IPv4 ou IPv6.

Após essa filtragem ele escreve em um novo arquivo TXT apenas as analise de quantidades de ASs que se comunicam só em IPv4, só em IPv6 e que se comunicam em ambas e seu numero total de AS.

O arquivo Graficos gera um grafico da analise para mais de 1 arquivo, podendo comparar assim seu uso ao longo do tempo e evolução.

Com os dados atuais foi obtido os seguntes resultados:
![Figure_1_EUA](https://user-images.githubusercontent.com/62814826/211423896-34b93940-e5f2-4ee1-82a5-8922f88843de.png)
![Figure_1_quenia](https://user-images.githubusercontent.com/62814826/211423922-0174b6df-4173-4e8d-bf02-0761567b478e.png)
![Figure_2_australia](https://user-images.githubusercontent.com/62814826/211423930-ccc62f0f-e794-4af6-964a-511049d712d9.png)
![Figure_brasil_1](https://user-images.githubusercontent.com/62814826/211423941-5d7e5aac-5a86-48b8-9730-996fb7b76013.png)
