nome = 'Daniel'
idade = 40
profissao = 'Programador'
linguagem = 'Python'

dados = {"nome": "Adelaide", "idade": 40}

print('Nome: %s Idade: %d' % (nome, idade)) # Esse formato não é utilizado mas!
print()

print('Nome: {} Idade: {}'.format(nome, idade))
print()

print('Nome: {0} Idade: {1}'.format(nome, idade))
print()

print('Nome: {1} Idade: {0} Nome: {1} {1}'.format(idade, nome))
print()

print('Nome: {nome} Idade: {idade}'.format(nome=nome, idade=idade))
print()

print('Nome: {name} Idade: {age} {name} {name} {age}'.format(age=idade, name=nome))
print()

print("Nome: {nome} Idade: {idade}".format(**dados))
print()

print(f'Nome:{nome} Idade:{idade}')
print()