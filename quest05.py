#Um professor deseja calcular a média de notas de uma turma de 10 alunos.
#Escreva um programa em Python que solicite ao professor as notas dos alunos e,
#em seguida, calcule e exiba a média das notas. Utilize um laço de repetição (FOR) para solicitar as notas dos alunos e uma variável para armazenar a soma das notas.

def calcular_media():
    soma_notas = 0
 
    for i in range(1, 11):
        notas = float(input(f"Informe a nota do aluno {i}: "))
        soma_notas += notas

    M = soma_notas / 10

    return M

media_notas = calcular_media()
print("A média das notas é: ", media_notas)
