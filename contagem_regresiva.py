# Algoritmo da contagem regressiva para estouro de fogos de artifício
# Autor: VITOR KAUÊ
# Data: 27/09/2023

import time  # Importa o módulo time para usar a função sleep

temp_inicio = 10  # Define o tempo inicial da contagem regressiva

print('='* 50)  # Imprime uma linha de separação
print("🚨CONTAGEM REGRECIVA PARA 2026🚨".center(50))  # Imprime o título centralizado
print('='* 50)  # Imprime outra linha de separação

while True:  # Inicia um loop infinito para aguardar o comando correto do usuário
    start = input("Digite 'INICIO' para iniciar a Contagem:\n").lower()  # Solicita o comando e converte para minúsculo

    if start == "inicio":  # Verifica se o comando está correto
        print('='* 50)  # Linha de separação
        print("Contagem regressiva iniciada!".center(50))  # Mensagem centralizada de início
        print('='* 50)  # Linha de separação
        time.sleep(2)  # Aguarda 2 segundos

        for c in range(temp_inicio,0, -1):  # Faz a contagem regressiva de 10 até 1
            print(f"{c}s".center(50))  # Imprime o número centralizado
            time.sleep(1)  # Aguarda 1 segundo entre cada número
        print(f"{'FIM! Fogos de artifício estourando! 🎆🎇':^50}")  # Mensagem final centralizada
        time.sleep(2)  # Aguarda 2 segundos
        break  # Sai do loop após a contagem
    else:
        print("Comando inválido. Por favor, digite 'INICIO' para começar a contagem.")  # Mensagem de erro
print('='* 50)  # Linha de separação
print("Feliz Ano Novo 2026! 🎉🎆".center(50))  # Mensagem final centralizada
print('='* 50)  # Linha de separação