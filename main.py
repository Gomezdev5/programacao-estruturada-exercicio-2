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

q3()



