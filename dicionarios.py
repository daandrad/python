# > DICIONÁRIOS

# Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = { 'nome': 'Daniel', 'idade': 40, 'altura': 1.85}

print(dicionario)
print()
print(dicionario['idade']) # No dicionário a gente diz qual é a chave.
print()

# Adicionando elementos em um dicionários

dicionario['programador'] = True

print(dicionario)
print()

# iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

print()

# Testando a existência de uma chave

print('peso' in dicionario)
