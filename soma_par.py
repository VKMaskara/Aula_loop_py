# Soma dos números pares
# Autor: VITOR KAUÊ
# Data: 27/09/2023

print("="*70)  # Imprime uma linha de "=" para separar visualmente o início do programa
print("   Soma dos Números Pares de 1 a 50   ".center(70))  # Imprime o título centralizado
print("="*70)  # Imprime outra linha de "=" para separar o título

soma_par = 0  # Inicializa a variável que irá armazenar a soma dos números pares

for par in range(1, 51):  # Loop de 1 até 50 (inclusive)
    if par % 2 == 0:  # Verifica se o número é par
        soma_par += par  # Soma o número par à variável soma_par
        print(f"{par}", end=" ")  # Imprime o número par na mesma linha, separado por espaço
print("\n" + "-"*70)  # Quebra a linha e imprime uma linha de "-"
print(f"A soma de todos os números pares entre 1 e 50 é: {soma_par}".center(70))  # Imprime o resultado centralizado
print("="*70)  # Imprime uma linha de "=" para finalizar o programa