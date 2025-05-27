import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Tente adivinhar o número entre 1 e 100!")

# Loop para o usuário tentar adivinhar
while True:
    try:
        palpite = int(input("Qual é o seu palpite? "))
        
        if palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto}.")
            break
    except ValueError:
        print("Por favor, digite um número válido.")
