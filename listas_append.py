

# > MÉTODOS DE LISTAS

lista = [1, 2, 12, 8, 2]

# append (Add um elemento sempre no final da lista.)

print('antes do apeend: ', lista)
print()

lista.append(3) 

print ('Depois do append: ', lista)
print()

# insert (você escolhe onde que add o elemento na lista.)

lista.insert(2, 10)

print('Depois do insert: ', lista)
print()

# extend (Serve para juntar dois elementos na lista.)

lista2 = [1, 2, 3]

lista.extend(lista2)

print('Depois do extend: ', lista)
print()

# pop (Serve para remover o ultimo elemento na lista.)

lista.pop() # Sem botar nenhum parametro(índice), ele sempre vai remover o ultimo elemento.
print('Lista após o pop: ', lista)
print()

lista.pop(2) # Com parametro(índice), remover o elemento.
print('Lista após o pop: ', lista)
print()

# remove (Diz qual elemento você quer remover.* não o índice como no pop*)

lista.remove(12)
print('Depois do remove:', lista)
print()

# count (Quando você quer contar quantos elementos parece no sua lista.)

print('Quantidade de 2 na lista: ', lista.count(2))
print()

# index (Ele diz um índice de um determinado elemento numa lista.)

print('Indice do elemento 3: ', lista.index(3))
print()

# sort (Serve para ordenar a sua lista.)

lista.sort()

print(lista)
print()

lista.sort(reverse=True) # Ordem descrecenter.
print(lista)
print()

# FUNÇÕES PARA LISTAS

# len

print(len(lista))
print()

#sun (A soma da lista, ele vai somar todos os elementos da sua lista.)

print(sum(lista))
print()

#max (Vai retornar o maior valor da sua lista)

print('Maior elemento da lista: ', max(lista))
print()

#min (Vair retornar o menor valor da sua lista)

print('Menor elemento da lista: ', min(lista))
print()


