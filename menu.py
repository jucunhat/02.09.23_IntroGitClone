import calculadora

print("1. soma")
print("2. Subtracao")
print("3. Multiplicacao")
print("4. Dividir")
print("0. Sair")
opcao = int(input("Olá! Digite a opção que deseja:"))

if opcao == 1:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print("A soma é:", calculadora.somar(num1, num2))

elif opcao == 2:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print("A subtracao é:", calculadora.subtrair(num1, num2))

elif opcao == 3:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print("A multiplicacao é:", calculadora.multiplicacao(num1, num2))

elif opcao == 4:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    print("A divisao é:", calculadora.divisao(num1, num2))

elif opcao ==0:
    breakpoint

else:
    print("Função não definida na calculadora")

