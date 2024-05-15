def checkPalindrome(palavra):
    palavra = palavra.replace(" ", "").lower()
    
    palavra_invertida = palavra[::-1]
    
    if palavra == palavra_invertida:
        return "A palavra é um palíndromo."
    else:
        return "A palavra não é um palíndromo."

palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

resultado = checkPalindrome(palavra)

print(resultado)