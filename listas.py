# > Listas

# Antes
nota1  = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [17.9, 9.7, 8.2]

# Criando Listas
lista = []
lista = list()
lista3 = [40, 'Daniel', 3.14159, True]
lista_de_lista = [10, [1, 2, 3]]

# Indexação e Slices (fatiamento)

lista = [42, 'Adelaide', 3.14159, True]

print(lista[0:])
print(lista3[0:])
print()

# Slices

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista)
print()

# Iterações com For

# 1. Utilizando os próprios  elementos da lista
 
for elemento in lista:
    print(elemento, end=" ")

print()

# 2. Utilizando os índices

print('Comprimento da lista:', len(lista)) # O *len* sempre trás  a quantidade de elementos da lista

print()

for i in range(len(lista)):
    print(lista[i])

print()

