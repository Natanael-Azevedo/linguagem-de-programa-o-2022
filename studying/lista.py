'''
A partir de duas listas a e b, componha uma lista c, alternando os elementos de a e b.
'''


a = input().split()
b = input().split()
c = []
a1 = 0 
b1 = 0

for x in range(len(a)+len(b)):
    if(x%2==0 and a1<len(a)) or b1>= len(b):
        c.append(a[a1])
        a1+=1