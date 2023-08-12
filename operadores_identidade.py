curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

c1 = curso is nome_curso
print(c1)

c2 = curso is not nome_curso
print(c2)

c3 = saldo is limite
print(c3)

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)