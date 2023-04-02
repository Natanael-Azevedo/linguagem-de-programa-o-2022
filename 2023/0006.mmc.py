'''calcule o mmc de a e b'''

a = int(input("Entre com um numero: "))
b = int(input("Entre com um numero: "))

if a > b: 
    maior = a 
else:
    maior = b 

while (True): 
    if maior%a==0 and maior%b==0:
        print(maior)
        break
    else:
        maior = maior+1