def concatenar_dados():
    data = []

    while True:
        entrada = input("Digite um dado (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        data.append(entrada)

    resultado = ''.join(map(str, data))

    return resultado

resultado_concatenado = concatenar_dados()

print("Dados concatenados:", resultado_concatenado)