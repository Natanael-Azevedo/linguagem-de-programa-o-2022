guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry, "+name+ " can't make it to dinner")

#vamos convidar outra pessoa 
del(guests[1])
guests.insert(1, 'Luiz Felipe')

#convidando novamente 
name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

print("I found a bigger dinner table, so i gonna invate more people!")

guests.insert(0, "Tino Marques")
guests.insert(1, "Gabigol")
guests.append('Tite')

#nova lista de convidados

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

print("Oh no, i can only invite 2 people")

remove = guests.pop(5)
print(f'bye, {remove.title()}')
remove = guests.pop(4)
print(f'bye, {remove.title()}')
remove = guests.pop(3)
print(f'bye, {remove.title()}')
remove = guests.pop(2)
print(f'bye, {remove.title()}')

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")




