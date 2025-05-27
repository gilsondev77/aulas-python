    # Entrada de dados
letra = input("Digite uma letra: ").strip().lower()

# Verificação se é vogal ou consoante
if letra in "aeiou":
    print("A letra é vogal.")
elif letra.isalpha() and len(letra) == 1:  # Verifica se é uma única letra do alfabeto
    print("A letra é consoante.")
else:
    print("O caractere digitado não é uma letra.")
