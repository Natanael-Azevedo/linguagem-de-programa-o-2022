#reverse tuple
tuple1 = (10,20,30,40,50)
tuple1 = tuple1[::-1]
print(tuple1)

#acesse o valor 20
tuple2 = ("orange",[20,10,30],(50,40))
print(tuple2[1][1])

#cria uma tupla com 50 itens 
tupla3 = list(range(1,51))
cinquenta = [x for x in tupla3]
print(cinquenta)

#Unpack the tuple into 4 variables
tuple4 = (10, 20, 30, 40)
a,b,c,d = tuple4
print(a)
print(b)
print(c)
print(d)

#Swap two tuples in Python
tuple5 = (11, 22)
tuple6 = (99, 88)
tuple5, tuple6 = tuple6, tuple5 
print(tuple5)
print(tuple6)

#Copy specific elements from one tuple to a new tuple
tuple7 = (11, 22, 33, 44, 55, 66)
tuple8 = tuple7[3:-1]
print(tuple8)

#Modify the tuple
tuple9 = (11, [22, 33], 44, 55)
tuple9[1][0] = 222
print(f'\n Nova {tuple9}')

#Sort a tuple of tuples by 2nd item
tuple10 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple10 = tuple(sorted(list(tuple10), key=lambda x: x[1]))
print(tuple10)

#Counts the number of occurrences of item 50 from a tuple
tuple11 = (50, 10, 60, 70, 50)
print(tuple11.count(50))
