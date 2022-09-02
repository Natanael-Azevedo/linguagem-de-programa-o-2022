'''Python refers to values that cannot 
change as immutable, and an immutable 
list is called a tuple.'''

buffet = ('salada','macarrão','feijoada','lasanha','cuscuz')
buffet =[prato for prato in buffet]
print(f'Pratos originais: {buffet}')

buffet = ('churrasco','camarão','feijoada','lasanha','cuscuz')
buffet =[prato for prato in buffet]
print(f'Novos pratos: {buffet}')
