import random

def jogar():
    print(35*"*")
    print("Bem vindo ao jogo de adivinhação")
    print(35*"*")

    numero_secreto = round(random.randrange(1, 101) * 100) # o random pode gerar de 0.0 a 1.0, por isso
    nivel = 1, 2 or 3                                      # utilizamos o randon.randrange, aí delimitamos que ele gera de 1 a 100 pois o 101 é exclusivo

    while(nivel != 1,2 and 3):
        print("\nNíveis de dificuldade: ")
        print("(1) fácil"
              "\n(2) médio"
              "\n(3) difícil")

        nivel = int(input("\nEscolha um nível de dificuldade: "))
        if(nivel == 1):
            num_tentativas = 20
            break
        elif(nivel == 2):
            num_tentativas = 10
            break
        elif(nivel == 3):
            num_tentativas = 5
            break
        else:
            print("\nEscolha um nível de dificuldade válido!")

    '''
                           #Laço com while
    while(rodada <= num_tentativas):
        print(f"Você está com {rodada} tentativa(s) de {num_tentativas} tentativas, boa sorte!")
        chute = int(input("Digite o seu número: "))
        print(f"Você digitou {chute}")
    
        acertou     = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto
    
        if(acertou):
            print(f"Você acertou! O número {chute} era o número secreto")
        elif(chute_maior):
            print("O número digitado é maior que o número secreto")
        else:
            print("O número digitado é menor que o número secreto")
    
        rodada = rodada + 1
    
    print("Fim do jogo!")
    '''

                      #Laço com o for

    for rodada in range (1, num_tentativas+1): #ou então for rodada in range (1,4):
                                                    #ou então for rodada in [1,2,3]:
        print(f"\nVocê está com {rodada} tentativa(s) de {num_tentativas} tentativas, boa sorte!")
        chute = int(input("Digite um número entre 1 e 100: "))
        print(f"Você digitou {chute}")

        if(1>chute<100):
            print("\nVocê não cumpriu com os requisitos!")
            continue

        acertou     = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print(f"\nVocê acertou! O número {chute} era o número secreto")
        elif(chute_maior):
            print("\nO número digitado é maior que o número secreto")
        elif(chute_menor):
            print("\nO número digitado é menor que o número secreto")

        rodada = rodada + 1

    print("Fim do jogo!")




















    '''
    AQUI É ONDE ESTOU COLOCANDO TUDO EM PRÁTICA
    '''
    # print("**********************************")
    # print("Bem vindo ao jogo de adivinhação")
    # print("**********************************")
    #
    # num_secreto = 50
    # num_tentativas = 3
    # rodada = 1
    #
    # while(rodada <= num_tentativas):
    #     print(f"Você está com {rodada} tentativa(s) de {num_tentativas}")
    #     chance = int(input("Qual será o número secreto? Digite: "))
    #
    #     acertou     = chance == num_secreto
    #     chute_maior = chance > num_secreto
    #     chute_menor = chance < num_secreto
    #
    #     if(acertou):
    #         print("Parabéns, você acertou o número secreto!")
    #     elif(chute_maior):
    #         print("O número que você digitou é maior, tente novamente.")
    #     elif(rodada == 3, chute_maior):
    #         print("O número que você digitou é maior.")
    #         break
    #     elif(rodada == 3, chute_menor):
    #         print("O número que você digitou é menor")
    #         break
    #     else:
    #         print("O número que você digitou é menor, tente novamente.")
    #
    #     rodada = rodada + 1
    #
    #     if(rodada == 3):
    #         print("Esta é a sua última rodada!")
    #
    # print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()