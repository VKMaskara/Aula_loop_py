import os
import time
os.system("cls")
contador = 1

while (contador <= 4):
    senha = input("Digite uma senha numérica: ")
    senha = "".join(senha.split())
    
    if(senha == "1234"):
        os.system("cls")
        for c in range(5,1,-1):
            print(f"Sistema Iniciando em {c}s")
            time.sleep(1)
        os.system("cls")
        print("\n=== SISTEMA INICIADO COM SUCCESSO ===")
        input("Pressione Enter para finalizar o sistema...")
        os.system("cls")
        print("\n--- Sistema finalizado ---")
        break
        
    elif (senha != "1234"):
        os.system("cls")
        if contador == 3:
            print("\n*** ALERTA! ÚLTIMA TENTATIVA! ***")
        else:
            print(f"\nSemia incorreta. Tente novamente.")
            print(f"Tentativa {contador-1} de 3")
        contador += 1
