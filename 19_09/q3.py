'''
Um triângulo retângulo pode ter lados que são valores inteiros. O conjunto de três valores ,  e  para os lados de um triângulo retângulo, sendo  a hipotenusa,  é chamado de tripla de Pitágoras se satisfaz o relacionamento de que a soma dos quadrados dos catetos é igual ao quadrado da hipotenusa. Isto é:
﻿
 
 
 ﻿
﻿
Escreva um programa que recebe do usuário um valor  e retorna os valores de ,  e  inteiros que representam um triângulo retângulo com a máxima hipotenusa , tal que . 
﻿
Note que o único valor informado pelo usuário é o valor  e que na impressão do resultado são mostrados os valores de ,  e  em sequência
'''
c = int(input())


for i in range(c, 0, -1):
    for j in range(c, 0, -1):
        
        if i**2 + j**2 == c**2:
            b = i
            a = j
            break

print(f'Tripla: {a} {b} {c}')