# CIRAR ALGORITIMO QUE SOMMA TODOS OD NÚMERO MUTIPLOS DE 3 DE 0 A 500
# AUTOR: VITOR KAUÊ
# DATA: 27/09/2023

print("="*70)  # Imprime uma linha de "=" para separar visualmente o início do programa
print(" SOMA DOS MÚLTIPLOS DE 3 DE 0 A 500 ".center(70, "-"))  # Imprime o título centralizado e preenchido com "-"
print("="*70)  # Imprime outra linha de "=" para separar o cabeçalho

soma_3 = 0  # Inicializa a variável que irá armazenar a soma dos múltiplos de 3
multiplos = []  # Lista para armazenar todos os múltiplos de 3 encontrados

for mult in range(0, 501):  # Percorre todos os números de 0 até 500 (inclusive)
    if mult % 3 == 0:  # Verifica se o número é múltiplo de 3
        soma_3 += mult  # Soma o múltiplo de 3 à variável soma_3
        multiplos.append(mult)  # Adiciona o múltiplo de 3 à lista multiplos

# Exibe os múltiplos em linhas de 10 números para melhor visualização
print("\nMúltiplos de 3 entre 0 e 500:\n")  # Imprime o cabeçalho da lista de múltiplos
for i in range(0, len(multiplos), 10):  # Percorre a lista de múltiplos de 10 em 10
    linha = "  ".join(f"{n:3}" for n in multiplos[i:i+10]).center(70)  # Formata uma linha com até 10 múltiplos centralizados
    print(linha)  # Imprime a linha formatada

print("\n" + "-"*70)  # Imprime uma linha de "-" para separar a soma final
print(f"A soma total dos múltiplos de 3 de 0 a 500 é: {soma_3}".center(70))  # Imprime a soma total centralizada
print("-"*70)  # Imprime uma linha de "-" para finalizar o programa