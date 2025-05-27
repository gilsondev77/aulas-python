# Solicitar o número de pessoas na turma
n = int(input("Quantas pessoas estão na turma? "))

# Variável para armazenar a soma das idades
soma_idades = 0

# Coletar as idades de todas as pessoas
for i in range(n):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    soma_idades += idade

# Calcular a média das idades
media = soma_idades / n

# Determinar a classificação da turma
if 0 <= media <= 25:
    print("A turma é jovem")
elif 26 <= media <= 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")
