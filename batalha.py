import random
import getpass

def contra_bot():
    bot_camp = ["0()", "1()", "2()", "3()",
             "4()", "5()", "6()", "7()"]

    bomba_bot = random.randrange(0,8)
    bot_camp[bomba_bot] = bomba_bot,"(x)"
    print(bot_camp)

    pessoa_camp = ["0()", "1()", "2()", "3()",
             "4()", "5()", "6()", "7()"]
    print(pessoa_camp)

    chute_pessoa = input("qual possição você quer sua bomba?")
    chute_pessoa = int(chute_pessoa)

    pessoa_camp[chute_pessoa] = chute_pessoa,"(x)"

    while(pessoa_camp, "(x)" in pessoa_camp):
        print(pessoa_camp)
        chute = input("onde voce quer atirar?")
        chute = int(chute)
        if(chute_pessoa == chute):
            pessoa_camp[chute] = chute, "(x) (0)"
        if(chute == bomba_bot):
            print("você acertou o barco inimigo!!")
            break
        else:
            print("você errou o barco inimigo")
            pessoa_camp[chute] = chute, "(0)"
        print("turno do inimigo")
        chute_bot = random.randrange(0,8)
        if(chute_bot == chute):
            pessoa_camp[chute] = chute, "(B) (0)"
        if(chute_bot == chute_pessoa):
            print("o inimigo te acertou!!")
            break
        else:
            print("o inimigo errou")
            pessoa_camp[chute_bot] = chute_bot, "(B)"

def contra_player():
    conta = 0
    um_camp = ["0()", "1()", "2()", "3()",
                "4()", "5()", "6()", "7()"]
    dois_camp = ["0()", "1()", "2()", "3()",
                "4()", "5()", "6()", "7()"]

    print(um_camp)
    um_jogador = getpass.getpass("JOGADOR 1: onde vai querer posicionar o navio")
    dois_jogador = getpass.getpass("JOGADOR 2: onde vai querer posicionar o navio")
    um_jogador = int(um_jogador)
    dois_jogador = int(dois_jogador)

    um_camp[um_jogador] = um_jogador, "(x)"
    dois_camp[dois_jogador] = dois_jogador, "(x)"

    while(conta == 0):
        print("vez do jogador 1")
        bomba1 = getpass.getpass("JOGADOR 1:onde quer atirar?")
        bomba1 = int(bomba1)
        if(bomba1 == dois_jogador):
            print("O JOGADOR 1 GANHOU")
            break
        else:
            print("o jogador 1 errou")
            print("vez do jogador 2")
        bomba2 = getpass.getpass("JOGADOR 2: onde quer atirar")
        bomba2 = int(bomba2)
        if(bomba2 == um_jogador):
            print("O JOGADOR 2 GANHOU")
            break
        else:
            print("o jogador 2 errou")

jogo = input("como voce quer jogar?(1)contra bot(2)multiplayer")
jogo = int(jogo)
if(jogo == 1):
    contra_bot()
else:
    contra_player()