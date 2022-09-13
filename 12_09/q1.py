'''
Escreva um programa que recebe uma string e imprime 'Legal' na tela caso a string contenha apenas números e letras. Imprima 'Chata' caso contrário. Lembre-se, uma string nada mais é que uma lista de caracteres. 

Dica: Use in ou not in para verificar se um valor qualquer está ou não está contido em uma lista.
'''
entre = input()
alfa = "abcdefghijklmnopqrstuvwxyz0123456789"
for x in entre.lower():
    if x in alfa:
        print("Legal")
        break
    else:
        print("Chata")
        break