def calculadora(num1, num2, operacao):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Erro: Operação inválida"
    
# Exemplo de uso da calculadora
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
resultado = calculadora(num1, num2, operacao)
print("Resultado:", resultado)
