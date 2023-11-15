import random
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    lista_acertos = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    qtd_erros = 0

    print(lista_acertos)

    while(not enforcou == 6 and not acertou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper() #tira os espaços do início e do final

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra): #o .upper() deixa todas as letras da palavra em letra maiúscula
                    lista_acertos[index] = letra
                index = index + 1
        else:
            print(f"A letra {chute} não existe nesta palavra")
            qtd_erros = qtd_erros + 1

        enforcou = qtd_erros
        acertou = "_" not in lista_acertos

        print(lista_acertos)

    if(acertou):
        print("Parabéns, você acertou a palavra secreta!")
    else:
        print("Você perdeu! Mais sorte da próxima vez.")
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()