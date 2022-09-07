'''
Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista L1 com todos os númeres pares positivos menores do que N.

Depois, o seu programa deve fazer uma cópia L2 da lista L1 e ler dois valores inteiros, I1 e I2, da entrada.

Você deve remover de L2 o elemento nos índice I1, e em seguida o elemento no índice I2. Após isso, imprima na saída as listas L1 e L2.
'''
num = int(input())
par = []
for i in range(1,num):
    if i<num and i%2==0:
        par.append(i)

pares = par[:]

I1 = int(input("entre com um valor: "))
I2 = int(input("entre com outro valor: "))

del pares[I1]
del pares[I2]

print(par)
print(pares)
