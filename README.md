# fome_zero

# 1.	Problema de Negócios
A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO Guerra foi recém-contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:

## 1 - Geral 
  1.	Quantos restaurantes únicos estão registrados? 
  2.	Quantos países únicos estão registrados? 
  3.	Quantas cidades únicas estão registradas? 
  4.	Qual o total de avaliações feitas? 
  5.	Qual o total de tipos de culinária registrados? 

## 2 - Pais 
  1.	Qual o nome do país que possui mais cidades registradas? 
  2.	Qual o nome do país que possui mais restaurantes registrados? 
  3.	Qual o nome do país que possui a maior quantidade de tipos de culinária distintos? 
  4.	Qual o nome do país que possui a maior quantidade de avaliações feitas? 
  5.	Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega e restaurantes que aceitam reservas? 
  6.	Qual o nome do país que possui, na média, a maior quantidade de avaliações e a maior nota média registrada? 
  7.	Qual o nome do país que possui, na média, a menor nota média registrada? 
  8.	Qual a média de preço de um prato para dois por país? 

## 3 - Cidade 
  1.	Qual o nome da cidade que possui mais restaurantes registrados? 
  2.	Qual o nome da cidade que possui mais restaurantes com nota média acima de 4? E com a nota média abaixo de 2.5? 
  3.	Qual o nome da cidade que possui o maior valor médio de um prato para dois? 
  4.	Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas? 
  5.	Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?  
  6.	Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas ou que fazem pedidos online? 

## 4 - Restaurantes 
  1.	Qual o nome do restaurante que possui a maior quantidade de avaliações? 
  2.	Qual o nome do restaurante com a maior nota média? 
  3.	Qual o nome do restaurante que possui o maior valor de um prato para duas pessoas? 
  4.	Qual o nome do restaurante de tipo de culinária brasileira que possui a menor e a maior média de avaliação? 
  5.	Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas? 
  6.	Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas? 

# 2.	Premissas assumidas para análise
  1.	O modelo de negócio é um marketplace
  2.	As principais visões geradas para o dashboard foram: visão geral, visão de países, visão de restaurantes e visão de cidades.
  3.	A análise foi realizada em cima de dados sem um período definido

# 3.	Estratégia da solução
Criação de um dashbord online utilizando as métricas que mensuram as principais visões do modelo de negócio da empresa:
  1.	Visão Geral
  2.	Visão Países
  3.	Visão Cidades
  4.	Visão Restaurantes
  5.	Visão Culinárias
     
Para cada visão foi apresentado os seguintes conjuntos de métricas:
  ### 1.	Visão Geral
        1.	Total de Restaurantes
        2.	Total de países
        3.	Total de cidades
        4.	Tipos de culinárias
        5.	Total de avaliações registradas
        6.	Média das avaliações
        7.	Mapa contendo a localização dos restaurantes

### 2.	Visão Paises
        1.	Quantidade de restaurantes por pais
        2.	Quantidade de cidades com restaurantes por pais
        3.	Média de avaliação por país
        4.	Média de preços de pratos por país

### 3.	Visão Cidades
        1.	Número de restaurantes por cidade
        2.	Top 7 cidades com as melhores notas
        3.	Top 7 cidades com as piores notas
        4.	Top 10 cidades com maior variedade de culinária

### 4.	Visão Restaurantes
        1.	Pais com melhor avaliação
        2.	Melhor restaurante desse país
        3.	Melhor culinária
        4.	Valor do prato para 2 pessoas
        5.	Avaliação do restaurante
        6.	Top 10 restaurantes 

## 4.	Top 3 Insigths de dados
  1.	O EUA é o país que mais aparece no ranking de melhores médias de avaliação, porém não é o país com maior número de restaurantes.
  2.	Para um melhor balizamento para exploração de estratégias de marketing para turistas nas escolhas de viagens, uma vez que o aplicativo é mundial, seria necessário a padronização de uma moeda para exploração de melhores preços em pratos para duas pessoas.
  3.	Os restaurantes com pedidos online recebem mais acessos de avaliações na plataforma.

## 5.	O produto do projeto
Um painel interativo hospedado em Cloud e disponível para qualquer dispositivo conectado a internet.

O painel pode ser acessado e visualizado através do link: https://fomezero.streamlit.app/

## 6.	Conclusão
Objetivo do projeto foi criar uma painel interativo que pudesse dar ao CEO uma visão panorâmica do negócio exibindo as métricas da melhor maneira possível.

## 7.	Próximos passos
  1.	Incrementar o painel com dados de pedidos, para que possa ser mensurado a evolução do faturamento
  2.	A adoção de uma moeda padrão para melhor visualização em termos financeiros
  3.	Buscar mais dados do tipo de publico que acessa e usa a plataforma
  4.	Adicionar novas visões no painel

