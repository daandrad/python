saldo = 2000.0
saque = float(input("Informe o valor do saque"))

if saldo >= saque:
    print("Realizando saque!: ")
    
else:
    print("Saldo insuficiente!") 



opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
    print("Retire seu dinheiro")

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    sys.exit("Opção invalida")



maior_idade = 18
idade_especial = 16

idade = int(input("Informe sua idade: "))

if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH.")

elif idade == idade_especial:
    print("Ele pode tirar com uma autorização do responsavel")

else:
    print("Ainda não pode tirar a CNH")   


