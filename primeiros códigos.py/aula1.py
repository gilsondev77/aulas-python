#saudacao = ("hello Word")
#print (saudacao)

# Solicita ao usuário para inserir uma frase
frase = input("Digite uma frase: ")

# Solicita ao usuário para inserir uma palavra ou caractere
caractere = input("Digite uma palavra ou caractere para verificar: ")

# Verifica se o caractere está na frase
if caractere in frase:
    print("O caractere está contido na frase.")
else:
    print("O caractere não está contido na frase.")


 
