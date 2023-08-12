texto = input("Informe um texto: ")
vogais = "AEIOU"


# Exemplo utilizado um iterável
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print() # adiciona uma quebra de linha


# Exemplo com range a função built-in range 
for numero in range(0, 51, 5):
    print(numero, end=" ")

print()

soma = 0

for i in range(1, 4):
    nota = float(input(f"Informe a sua nota {i}: "))

    soma = soma + nota

print(soma / 3)    