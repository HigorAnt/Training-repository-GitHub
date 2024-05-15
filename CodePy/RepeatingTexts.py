def repeatString(string, vezes):
    return string * vezes

stringInput = input("Digite uma string: ")
numberInput = int(input("Digite um número inteiro: "))

resultado = repeatString(stringInput, numberInput)

print("Resultado:", resultado)