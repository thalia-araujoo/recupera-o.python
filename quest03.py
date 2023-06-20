#Uma loja deseja calcular o desconto a ser aplicado em um produto segundo a idade do cliente.
# Se o cliente tiver menos de 21 anos, o desconto será de 15%.
# Caso contrário, o desconto será de 10%.
# Escreva uma função em Python chamada "calcular_desconto" que recebe a idade do cliente como parâmetro
# e retorna o valor do desconto a ser aplicado.

def calcular_desconto(idade):
    if idade < 21:
        print("seu desconto será de 15%, por ser menor de 21 anos.")
        
    else:
        print("Seu desconto será de 10%, por ser maior de 21 anos.")
        
def main():
    ID_Pessoa = int(input("Informe sua idade: "))
    
    r = calcular_desconto(ID_Pessoa)
    
    
    
if __name__=="__main__":
    main()         

        
    