def AberturaDeJogo ():
    print ("Bem-vindo ao jogo do NIM! Escolha:")

    print ("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato 2")

    t = int(input(""))
    if t == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    else:
        print("Você escolheu um campeonato!")
        rodadas = ["**** Rodada 1 ****", "**** Rodada 2 ****", "**** Rodada 3 ****"]
        QntVezesQueCGanhou = 0
        QntVezesQueUGanhou = 0

        for rodada in rodadas: 
            print(rodada)
            vencedor = partida()
            if vencedor == "c":
                QntVezesQueCGanhou = QntVezesQueCGanhou + 1
            else:
                QntVezesQueUGanhou = QntVezesQueUGanhou + 1

        print("**** Final do campeonato! ****")
        print("Placar: Você ", QntVezesQueUGanhou," X ", QntVezesQueCGanhou, " Computador")

                   



def partida ():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if m > n:
        print("Oops, o limite é maior que o número de peças!")
    else:
        vez = "u"
            
        if n % (m+1) == 0:
            print("Você começa!")
            vez = "u"

        else:
            print("Computador começa!")
            vez = "c"


        while True == True:
            if vez == "c":
                Qtdsubtrair = computador_escolhe_jogada(n, m)
                if Qtdsubtrair == 1:
                    print ("O computador tirou uma peça.")
                else:
                    print("O computador tirou ", Qtdsubtrair, " peças.")
            else:
                Qtdsubtrair = usuario_escolhe_jogada(n, m)             
            
            n = n - Qtdsubtrair
            print("Agora restam ", n, " peças no tabuleiro.")
            if n <= 0:
                if vez == "c":
                    print ("Fim do jogo! O computador ganhou!")
                else:
                    print ("Fim do jogo! O usuário ganhou!")
                
                return vez
                
            else:
                if vez == "c":
                    vez = "u"
                else:
                    vez = "c"    

def computador_escolhe_jogada(n, m):
    if m == 1:
        return 1
    else: 
        peças = 1
        multiplo = False
        while multiplo == False:
            if ((n - peças) % (m + 1)) == 0:
                multiplo = True
            else:
                peças = peças + 1
                if peças > m:
                    return m

    return peças



def usuario_escolhe_jogada(n, m):
    válido = False
    while válido == False:
        peças = int(input("Quantas peças você vai tirar? "))
        if (peças > m) or (peças == 0):
        #if (peças == 0):
           print ("Oops! Jogada inválida! Tente de novo.")
        else:
            válido = True
            
    return peças

AberturaDeJogo ()