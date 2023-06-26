#Uma empresa deseja verificar se um determinado cupom está dentro da faixa de cupons gerados para a promoção de São João.
# Caso o número esteja dentro do intervalo, o programa deve exibir a mensagem "Cupom válido". Caso contrário, deve exibir a mensagem "Cupom inválido", sabendo que o primeiro cupom tinha o número 75 e o último gerado foi o 208.
#Escreva um programa em Python que recebe o número inteiro do cupom e verifique se o cupom é válido.

#criei minha função ja com o valor do primeiro e ultimo cupom
def verificar(cupom):
    primeiro_cupom = 75
    ultimo_cupom = 208
#verifiquei se o cupom esta entre esses numero..se estiver ele diz valido
    if primeiro_cupom <= cupom <= ultimo_cupom:
        return "Cupom válido"
    
    else:
        return "Cupom inválido"
#função principal pede um numero ao usuario e chamo a função para verificar.
def main():
    N_cupom = int(input("Digite o número do cupom: "))
    r = verificar(N_cupom)
    print(r)
    
if __name__=="__main__":
    main()
