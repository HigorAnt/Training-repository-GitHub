def concatenar_dados():
    dados = []

    while True:
        entrada = input("Digite um dado (ou 'fim' para encerrar): ")
        if entrada.lower() == 'fim':
            break
        dados.append(entrada)

    resultado = ''.join(map(str, dados))

    return resultado

resultado_concatenado = concatenar_dados()

print("Dados concatenados:", resultado_concatenado)