import random

# vai gerar um número secreto aleatório entre 1 e 50
num_secreto = random.randint(1, 50)


while True:
    
    palpite = int(input("Digite um número entre 1 e 50: "))

    # Verificar se o palpite é muito alto, muito baixo ou correto
    if palpite > num_secreto:
        print("Seu palpite foi muito alto! Tente novamente.")
    elif palpite < num_secreto:
        print("Seu palpite foi muito baixo! Tente novamente.")
    else:
        print("Parabéns! Você acertou o número secreto!")
        break
