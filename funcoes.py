# > FUNÇÕES

# 1. O que são funções e por que utilizar?

# funções que já utilizamos anteriormente......

"""print() # - Imprimir uma mensagem ( int, float, str) no console (terminal, cmd)

input() # - Retorna um dado informado pelo usuário ( entrada padrão) e pode receber uma string

len() # - Recebe uma lista e retorna o tamanho dessa lista

max () # - Retorna o maior valor de uma lista

# 2. Criação de funções (O significado de def(definir uma função))."""
# Funções inicial
def saudacao():
    print('Seja bem-vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()

print()


# Funções com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Daniel', 'Python')

print()

# Funções com parâmetros dafault

def saudacao(nome, curso= 'Python'):
    print(f'Seja bem-vinda(o), {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}!')

saudacao('Daniel')

print()

# Funções com retorno

def soma(num1, num2):
    return num1 + num2 # Obs: A partir do momento dentro de uma função existe uma palavra return ele vai retornar aquele valor e vai encerrar aquela função.

resultado = soma(5, 7)

print('O resultado da soma é', resultado)
print()

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao =='-':
        return num1 - num2
    
resultado = calculadora(10, 20, '-')

print(resultado)



