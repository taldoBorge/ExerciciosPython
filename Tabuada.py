numero = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {numero}:")
for i in range(1, 101): #range é uma classe usada pra fazer contagens nesse caso de 1 a 100
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")