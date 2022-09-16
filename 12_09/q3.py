'''Escreva um programa que recebe como entrada uma sequência de 10 valores quaisquer. Seu programa deverá informar qual o maior e qual o menor  valor informado, além do MDC (máximo divisor comum) para estes dois valores. '''
lista =[]
resto=int(0)
for x in range(10):
    lista.append(int(input()))   
maior=max(lista)
menor=min(lista)
#print("=-"*30)
#print(maior, menor)
#print("=-"*30)
#maior,menor
mdc=maior

while maior % mdc != 0 or menor % mdc != 0: 
        mdc = mdc - 1

  
print(f"{maior} {menor} {mdc}")   
