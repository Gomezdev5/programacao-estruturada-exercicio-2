def q1():
    """ Faça um programa que calcula a quantidade de divisores de um
    número (incluindo 1 e o próprio número) que são divisíveis por 3.
    """


    numero = int(input("Digite um numero"))
    contador = 0
    # o numero +1 vai até o numero dentro (Exemplo coloco o 4 no input= 1,2,3,4,5) ele vai correr até o numero 5, porém não vai entrar o numero 5.
    #Parte 1 - Programa mostra os divisores
    #Parte 2 - Com os numeros que são divisores, verificar se são divisores:, incremento um contador
    
    for i in range(1, numero + 1):
        if (numero % i == 0) and (i % 3 == 0):
           contador += 1
    print(contador)

def q2():

    #Escreva um programa que receba como entrada dois números inteiros e retorne a soma dos números positivos no intervalo definido por eles, considerando inclusive os extremos.

    num1 = int(input("Digite o numero 1"))
    num2 = int(input("Digite o numero 2"))

    if num1 > num2:
        temp = num1
        num1 = num2
        num2= temp

    soma = 0
    for i in range(num1, num2):
        if i > 0:
            soma += i
    print(soma)


def q3():

    """Um professor precisa saber qual a média das notas de uma sala e pediu sua ajuda para construir um programa que permita 
    inserir as notas finais de cada aluno e, ao final, exibir a média da sala. Lembre-se que as notas variam de 0 a 10 e o professor digitará -1 
    quando quiser encerrar as entradas. Obs.: use variáveis de ponto flutuante """

    qnt, soma, nota = 0, 0, 0
    while True: #irá sempre ler as notas
        
        nota = int(input("Digite uma nota: "))

        if nota == -1: #para o while
            break

        if nota in range(0,11): 
            soma += nota
            qnt += 1
        else:
            print("Valor da nota está fora do intervalo")

    media = soma / qnt

    print(f"A média das notas foi ", media)

def q5():
    N = int(input("Digite o valor de N: "))
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))

    multiplos = [i for i in range(A, B + 1) if i % N == 0]
    
    if multiplos:
        for multiplo in multiplos:
            print(multiplo)
    else:
        print("INEXISTENTE")

def q6():
    i = 1
    n = int(input("Digite um número natural: "))
    
    while True:
        produto = i * (i + 1) * (i + 2)
        if produto == n:
            return True
        elif produto > n:
            return False
        i += 1
        if n:
            print(f"{n} é um número triangular.")
        else:
            print(f"{n} não é um número triangular.")

def q7():
    n = int(input("Digite um número entre 1 e 40: "))

# Verificar se o valor de n está dentro do intervalo permitido
    if 1 <= n <= 40:
        # Loop para realizar as iterações
        for i in range(1, n + 1):
            # Gerar a lista de números para a iteração atual e convertê-los para string
            linha = ' '.join(str(j) for j in range(1, i + 1))
            
            print(linha)
    else:
        print("Número fora do intervalo permitido. Por favor, digite um número entre 1 e 40.")

def q8():
    # Solicitar a quantidade de dias e a quilometragem total ao usuário
    dias = int(input("Digite a quantidade de dias: "))
    quilometragem_total = float(input("Digite a quilometragem total rodada: "))

    # Preço por diária e cota de quilometragem
    preco_diaria = 90
    cota_km_por_dia = 100
    taxa_extra_por_km = 12

    cota_total = dias * cota_km_por_dia

    valor_diarias = dias * preco_diaria

    quilometragem_excedente = max(0, quilometragem_total - cota_total)

    valor_taxa_extra = quilometragem_excedente * taxa_extra_por_km

    valor_total = valor_diarias + valor_taxa_extra

    valor_total = dias, quilometragem_total

    print(f"Valor total a ser pago: R$ {valor_total:.2f}")
def q9():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))

    numeros = [a, b, c]
    numeros.sort()
    


    numeros_ordenados = (a, b, c)

    
    print("Números em ordem crescente:", numeros_ordenados[0], numeros_ordenados[1], numeros_ordenados[2])

q9()
