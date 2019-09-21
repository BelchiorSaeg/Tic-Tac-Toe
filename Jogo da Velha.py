##  -Funções

#   Verifica se a área está desponivel para jogada
def disponibilidade(area): return "-" in area


#   Mostra a situação atual do jogo
def mostrar_jogo():
    clear()
    print ("    1 2 3 \n    {}|{}|{} A \n    {}|{}|{} B \n    {}|{}|{} C \n".format(a1,a2,a3,b1,b2,b3,c1,c2,c3))


#   Tabela com todas ás areas/variáveis do jogo.
def areas_val():
    return [a1,a2,a3], [b1,b2,b3], [c1,c2,c3], [a1,b1,c1],[a2,b2,c2], [a3,b3,c3], [a1,b2,c3], [a3,b2,c1]


#   Verifica se o jogo foi encerrado e retorna: Empate,Votória e Derrota
def vitoria():

    for x in areas_val(): # X = sub-listas em "def Areas_val" que equivalem as possibilidades de finalização do jogo

        contador_x = x.count("x")
        contador_o = x.count("O")

        if contador_x == 3:
            mostrar_jogo()
            print ("Parabéns, Você Venceu!! :D\n")
            return "encerrado"

        if contador_o == 3:
            mostrar_jogo()
            print ("lamento, Voce Perdeu! :( \n")
            return "encerrado"

        if not disponibilidade([a1,a2,a3,b1,b2,b3,c1,c2,c3]):
            mostrar_jogo()
            print ("Empate!!, Tente Novamente!\n")
            return "encerrado"

    return "continua"


#  Função do movimento da CPU
def cpu_mov(jogada,history_cpu,history_usr):

    # Verifica e tenta realizar uma jogada de vitoria.
    for x in areas_val():

        contador_x = x.count("x")
        contador_o = x.count("O")
        subL_index = areas_val().index(x) #index de x

        if (contador_o == 2) and (contador_x == 0) and (disponibilidade(x)):
            return ( ( areas_dem[subL_index] )[x.index("-")] )

    # Verifica e tenta impedir a possível vitória do usuário
    for x in areas_val():

        contador_x = x.count("x")
        contador_o = x.count("O")
        subL_index = areas_val().index(x)

        if (contador_x == 2) and (contador_o == 0) and (disponibilidade(x)):
            return ( ( areas_dem[subL_index] )[x.index("-")] )

    # Função para impedir uma jogada do usuário:
        condicao = [a2 == "x" and b1 == "x", a2 == "x" and b3 == "x", c2 == "x" and b1  == "x", c2 == "x" and b3 == "x"]
        if any(condicao) and b2 == "-": return "b2"
    

    #Função para caso o computador inicie!
    if (jogada == 1) or (jogada == 2) or (jogada == 3):

        if jogada == 1:
            x = ["c3", "a3", "a1", "c1"]
            y = random.choice(x)
            while y in history_cpu or y in history_usr: y = random.choice(x)
        if jogada == 2:
            x = ["c3", "a3", "a1", "c1"]
            y = random.choice(x)
            while y in history_cpu or y in history_usr: y = random.choice(x)
            return y
        if jogada == 3:
            x = ["c3", "a3", "a1", "c1"]
            y = random.choice(x)
            while y in history_cpu or y in history_usr: y = random.choice(x)
            return y

    #Função para caso o Usuário incie!!
    if len(history_cpu) == 0 and len(history_usr) == 1 and disponibilidade(b2): return "b2"

    if disponibilidade(b2):

        return "b2"

    x = ["a1", "a3", "c1", "c3"]
    y = random.choice(x)
    while y in history_cpu or y in history_usr: y = random.choice(x)
    return y

    #Função caso a CPU já tenha colocado 1
    for x in areas_val():

        contador_o = x.count("O")
        subL_index = areas_val().index(x) #index de x

        if contador_o == 1 and disponibilidade(x):
            return ( ( areas_dem[subL_index] )[x.index("-")] )

    #Função para caso caso a CPU não tenha a possibilidade de continuar uma sequência
    index = random.randrange(8) #index de Coluna/Linha
    while "-" not in (areas_val()[index]): index = random.randrange(8)

    s_index = random.randrange(3) #index de Area na Coluna/Linha
    while "-" != (areas_val()[index])[s_index]: s_index = random.randrange(3)

    return (areas_dem[index])[s_index]

##  Fim cpu_mov


import random

repeticao = "S" 

##  Processamento do Jogo:

while repeticao != "n" and repeticao != "N":

    # Inicialização de Varáveis
    a1,a2,a3,b1,b2,b3,c1,c2,c3  = "-","-","-","-","-","-","-","-","-" #Áreas do jogo
    areas_dem                   = ("a1","a2","a3"), ("b1","b2","b3"), ("c1","c2","c3"), ("a1","b1","c1"),("a2","b2","c2"), ("a3","b3","c3"), ("a1","b2","c3"), ("a3","b2","c1") # Lista que representa todas as áreas
    status                      = "rodando" #Status da procedência do Jogo
    history_cpu                 = [] #Histórico de jogadas da CPU
    history_usr                 = [] #Histórico de jogadas do jogador
    contador_erro               = 0 #contagem de entradas invalidas por parte do usuário
    clear                       = lambda: print ("\n" * 45) #Limpar a tela



    # Define quem começará a jogar
    prim_jogad = (random.choice(["cpu","user"]))

    if   prim_jogad == "user":
        print(" Você Começa! \n")
        jogada = 9

    else:
        print(" O Computador Começa! \n")
        jogada = 1

    # Jogo começado com a CPU: Primeiro movimento da CPU
    if prim_jogad == "cpu":
    
        history_cpu.append ( cpu_mov(jogada,history_cpu,history_usr) )

        locals()[ history_cpu[-1] ]             = "O"
        prim_jogad                              = "Finalizada"
        jogada                                  = jogada + 1

        print ("\n Vez do Computador: \n")
        mostrar_jogo()

    else: mostrar_jogo()


    ##  Processamento Geral do Jogo
    while status != "encerrado":

        opcao               = input(" Sua vez: ").lower()
        resposta            = ""

        if ((opcao in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]) and (locals()[opcao] == "-")) or (opcao == "8246"):

            if opcao != "8246": #USER MOVIM

                history_usr.append(opcao)
                locals()[opcao] = "x"
                status          = vitoria()
                
                if status != "encerrado": mostrar_jogo()


            if status != "encerrado": #CPU MOVIM

                print ("\n Vez do Computador: \n")
                history_cpu.append ( cpu_mov(jogada,history_cpu,history_usr) )
            
                locals()[ history_cpu[-1] ] = "O"### Alterações
                status                      = vitoria()
                jogada                      = jogada + 1
                
                if status != "encerrado": mostrar_jogo()

        # Tratamento de Inserção de VAR errada por parte do Usuário
        elif ((opcao in ["a1","a2","a3","b1","b2","b3","c1","c2","c3"])):
            
            contador_erro = contador_erro + 1
            if (locals()[opcao] == "x"): print("\nVocê já jogou aí! \n\n")
            if (locals()[opcao] == "O"): print("\nA CPU já jogou aí! \n\n")
        else:
            
            contador_erro = contador_erro + 1
            if contador_erro == 5:
                contador_erro = 0
                print("\n---  jogue apenas usando esses atalhos: {}!!  ---\n\n".format(["a1","a2","a3","b1","b2","b3","c1","c2","c3"]))
                mostrar_jogo()
                print("\n")
            else: print ("\nEssa opção não está presente no jogo!\n\n")
    
    repeticao = input("\n\n\n----Deseja continuar?? [S/N]: ----\n")
    print("\n\n")
    clear()
