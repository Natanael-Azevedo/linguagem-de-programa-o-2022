'''
Escreva um programa que solicite ao usuário dois números inteiros. Como resposta, o programa deverá exibir uma das seguintes mensagens:

"O primeiro número informado é par. O segundo número informado é ímpar"
"O primeiro número informado é ímpar. O segundo número informado é par"
"Ambos os números são pares"
"Ambos os números são ímpares"
'''
n1 = int(input())
n2 = int(input())

if n1%2==0 and n2%2!=0 :
    print("O primeiro número informado é par. O segundo número informado é ímpar")
if n1%2!=0 and n2%2==0 :
    print("O primeiro número informado é impar. O segundo número informado é par") 
if n1%2==0 and n2%2==0 :
    print("Ambos os números são pares")
if n1%2!=0 and n2%2!=0 :
    print("Ambos os números são impares")


