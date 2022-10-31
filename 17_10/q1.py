'''
Considere as definições de média, moda e mediana dadas a seguir para um conjunto v de n valores inteiros ordenados:
Média: somatório de todos os elementos do conjunto dividido pela quantidade de elementos;
Moda: valor que mais vezes ocorre no conjunto;
Mediana: é igual ao elemento central do conjunto, caso este possua uma quantidade ímpar de elementos. Caso a quantidade de elementos seja par, então a mediana é a média dos dois elementos centrais;
A partir da definição dada, implemente uma função que recebe como argumento um vetor de números inteiros  e retorna sua média, moda e mediana. Implemente também um programa para testar essa função a partir de valores fornecidos pelo usuário. Exemplo:
Entrada
Saída
5
1 2 3 3 5
(media, moda, mediana) = (2.80, 3, 3.00)

'''

def stats(media, moda,mediana):
    media = 4
    moda = 8
    mediana = 10

    return media, moda, mediana


print(stats(4,8,10))