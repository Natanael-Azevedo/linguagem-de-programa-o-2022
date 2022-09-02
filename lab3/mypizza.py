pizzas = ['calabressa','frango com catupiry','sertaneja','vegetariana']
pizza_do_amigo = pizzas[:]
pizzas.append('pesto')
pizza_do_amigo.append('pepperoni')
#print o nome das pizzas
print(f"essas são minhas pizzas favoritas: {[x for x in pizzas]}")
print('-='*15)
print(f"essas são as pizzas favoritas do meu amigo:{ [x for x in pizza_do_amigo]}")
print('-='*15)

