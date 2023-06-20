#Uma livraria deseja listar os livros mais vendidos do mês no padrão POSIÇÃO - TÍTULO DO LIVRO. Escreva um programa em Python que receba uma lista de livros com sua respectiva posição no ranking dos mais vendidos e exiba essa lista em tela, conforme o exemplo a seguir.
#Ranking de Mais Vendidos
#1 - Senhor dos Anéis
#2 - O apanhador no campo de centeio

def main():
    livros = []
    
    tam = int(input('Digite o tamanho da sua lista: '))
    
    for i in range(tam):
        liv = input('Digite o nome do livro: ')
        rank = int(input('Digite sua posição no ranking: '))
        livros.append((rank, liv))
    
    livros_ordenados = sorted(livros)
    
    print('Ranking de Mais Vendidos')
    
    for rank, liv in livros_ordenados:
        print(f'{rank} - {liv}')
 

if __name__ == "__main__":
    main()