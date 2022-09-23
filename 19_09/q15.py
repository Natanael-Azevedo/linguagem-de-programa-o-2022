'''
Você deve escrever um programa para calcular o tipo de ingresso que uma pessoa deve pagar com base na sua idade e na sua ocupação.

Pessoas com menos de 10 anos e com mais 70 anos não pagam ingresso. Fora dessa faixa etária, pessoas com menos de 30 anos cuja ocupação seja estudante, ou pessoas cuja ocupação seja professor, ganham desconto no valor do ingresso.

Caso a pessoa não se enquandre em nenhuma dessas categorias, pagará o preço normal do ingresso.

A idade de uma pessoa é um valor inteiro, e a sua ocupação é uma palavra que consiste apenas de letras minúsculas. Cada valor será fornecido em uma linha separada. Veja os exemplos de entrada e saída a seguir.
'''

idade = int(input("informe idade:"))
ocupacao = input("informe ocupação:").lower()
if idade<10 or idade>70:
    print("Ingresso gratuito")
elif idade<30 and ocupacao=="estudante":
    print("Ingresso com desconto")
elif ocupacao=="professor":
    print("Ingresso com desconto")
else:
    print("Ingresso normal")