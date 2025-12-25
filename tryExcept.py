#this code is a exercice about try and except blocks in python

#o primeiro captura a entrada do usuario e tenta converter pra inteiro, tratando erro caso a entrada seja invalida
number = input("Please enter a number: ")
try:
    number = int(number)
    print(f"You entered the number: {number}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
#o segundo captura um arquivo .txt e tenta ler seu conteudo, tratando erro caso o arquivo nao existe 


try:
    archive = open("genericFile.txt", "r")
except FileNotFoundError:
    print("Error: The file was not found.")
