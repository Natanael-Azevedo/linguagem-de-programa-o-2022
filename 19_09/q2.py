"""Receba do usuário uma lista de valores inteiros com n elementos. A partir desta lista, gere duas listas auxiliares. Uma contendo seus elementos que são número perfeitos e outros contendo os que não são. Um número perfeito é aquele cuja soma de seus divisores, excluindo ele mesmo, é igual ao próprio número. Por exemplo: 6 = 1 + 2 + 3"""
n=int(input())
num=[]
perfeitos=[]
imperfeitos=[]
for x in range(n):
    a=int(input())
    num.append(a)
for x in num:
    s=0
    for b in range(1,x):
        if x%b==0:
            s=s+b
    if s==x:
        perfeitos.append(x)
    else:
        imperfeitos.append(x)
print(f'perfeitos = {perfeitos}\nnão-perfeitos = {imperfeitos}')