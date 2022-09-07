'''
Receba do usuário os nomes dos 20 times da Séria A do Brasileir~]ao. Assumindo que o usuário informrá estes nomes pela ordem atual de classificação, construa as seguintes listas:
1. Os quatro primeiros times que vão disputar a libertadores;
2.Os quatro times rebaixados;
3.O time(ou times) com o nome mais extenso;
4.Quais confrontos teriamos se o primeiro colocado jogasse contra o último, o segundo com o penultimo e assim sucessivamente;
'''
n = input("Informe a quantidade de times: ")
n= int(n)

times = []

for x in range(n):
    time = input("Informe o nome do time: ")
    times.append(time)
#1.
libertadores = times[:4]
#2.
rebaixamento= times[-4:]
#3.
maiores_comprimentos = [len(x) for x in times]
maior = max(maiores_comprimentos)
maiores_nomes = [x for x in times if len(x) == maior]
#4.
primeiros=times[:4]
ultimos=times[-4:]
ultimos.reverse()

for primeiro, segundo in zip(primeiros, ultimos):
    print(f'Confrontos: {primeiro} x {segundo}')


print("times")
print(times)
print("libertadores")
print(libertadores)
print("rebaixamento")
print(rebaixamento)
print(f'o(s) time(s) com o maior nome é o: {maiores_nomes}')
