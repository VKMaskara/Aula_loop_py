# CRIE UM ALGORITMO QUE CALCULE A TABUADA DE UM NÚMERO INFORMADO PELO USUÁRIO
# AUTOR: VITOR KAUÊ
# DATA: 27/09/2023
print("=" * 50)
print("🧮 TABUADA PYTHON 🧮".center(50, "-"))
print("=" * 50)

num = int(input("\nDigite um número para ver a tabuada: "))

print("\n" + "-" * 50)
print(f"Tabuada do {num}".center(50))
print("-" * 50)

for i in range(1, 11):
    print(f"{num:2}  x {i:2}  =  {num * i:3}".center(50))

print("-" * 50)
print("Fim da tabuada! 📐e = ∑∞ⁿ⁼⁰ ¹ₙ🤓".center(50))
print("=" * 50)