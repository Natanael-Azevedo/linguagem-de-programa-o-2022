num = 42339

n1 = num//10000
resto = num%10000

n2 = resto//1000
resto = resto%1000

n3 = resto//100
resto = resto%100

n4 = resto//10
resto = resto%10

n5 = resto//1

print(n1,n2,n3,n4,n5)