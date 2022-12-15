"""Jogo da Velha"""

from random import sample
import time



tabuleiro_de_jogo = """
 {:^2}| {:^2}| {:^2}
---+---+---
 {:^2}| {:^2}| {:^2}
---+---+---
 {:^2}| {:^2}| {:^2}
"""
tabuleiro_de_posicoes = tabuleiro_de_jogo[:]

x = "X" #jogador ou marcador X
o = "O" #jogador ou marcador O
ZERO = 0

JOGADOR_PRINCIPAL = x  #define que o jogador principal será X 
JOGADOR_SECUNDARIO = o #define que o jogador secundário será O

NOME_DO_JOGADOR_PRINCIPAL = "Você"
NOME_DO_JOGADOR_SECUNDARIO = "A máquina"

posicoes = list(range(1, 10))
posicoes_dos_marcadores = [""]*9
posicoes_preenchidas = []
posicoes_restantes = posicoes[:]

jogadas_o = []
jogadas_x = []

jogadas_vencedoras = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], 
    [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]
]

tabuleiro_de_posicoes = tabuleiro_de_posicoes.format(*posicoes)   

def deu_velha(jogadas: list): 
    for velha in jogadas_vencedoras:
        contador = 0
        for item in velha:            
            if item in jogadas:
                contador += 1
            else:
                break
        if contador == 3:
            print("Velha:",velha)
            return True
    return False    

def eh_jogador_principal(jogador: str): 
    return jogador == JOGADOR_PRINCIPAL 
            
def escolher_posicao_aleatoria():   
    posicao_aleatoria = sample(posicoes_restantes, 1)[0]
    return posicao_aleatoria                           
   
def receber_posicao(jogador: str):
    posicao = None                
    if eh_jogador_principal(jogador):
        try:
            posicao = int(input("Escolha uma posição[1-9]:"))            
        except ValueError: 
            print("Não é um número inteiro.")
            return None 
    else:
        #escolhe uma posição aleatória  
        posicao = escolher_posicao_aleatoria()
        time.sleep(0.1)                             
    return posicao
    
def posicao_esta_preenchida(posicao: int):
    return posicao in posicoes_preenchidas

def atualizar_marcadores_do_tabuleiro(marcador: str, posicao: int):
    indice = posicao - 1
    posicoes_dos_marcadores[indice] = marcador  

def atualizar_tabuleiro_de_jogo():
    tabuleiro_preechido = tabuleiro_de_jogo.format(*posicoes_dos_marcadores)  
    return tabuleiro_preechido 
    
def atualizar_listas_de_posicoes(posicao: int):  
    posicoes_preenchidas.append(posicao)
    posicoes_restantes.remove(posicao)    

def adicionar_posicao(jogador: str, posicao: int):
    if jogador == x:
        jogadas_x.append(posicao)
    else:
        jogadas_o.append(posicao)
    #atualiza as listas de posições do jogo
    atualizar_listas_de_posicoes(posicao)
    #atualiza marcadores exibidos no tabuleiro 
    atualizar_marcadores_do_tabuleiro(jogador, posicao)

def jogador_ganhou(jogador: str): 
    jogadas = []  
    if jogador == x:
        jogadas = jogadas_x 
    else:
        jogadas = jogadas_o        
    return deu_velha(jogadas) == True
                   
def informar_posicoes_do_tabuleiro(jogador: str):
    if eh_jogador_principal(jogador):
        print(tabuleiro_de_posicoes)  
     
def exibir_tabuleiro_de_jogadas(jogador: str, fim_de_jogo: bool=False):
    #preenche o tabuleiro de jogo com marcadores nas posições jogadas
    tabuleiro_preenchido = atualizar_tabuleiro_de_jogo()

    if fim_de_jogo:         
        print(tabuleiro_preenchido)                  
    else:
        informar_posicoes_do_tabuleiro(jogador)
        print(tabuleiro_preenchido)                   
         
def exibir_mensagem_de_vitoria(jogador: str):
    if eh_jogador_principal(jogador):
        print(f"{NOME_DO_JOGADOR_PRINCIPAL} ganhou!")
    else:
        print(f"{NOME_DO_JOGADOR_SECUNDARIO} ganhou!")

def deu_empate(numero_de_jogadas: int): 
    numero_de_posicoes = len(posicoes)
    return numero_de_jogadas == numero_de_posicoes

def alterar_vez_de_jogo(jogador: str):
    if jogador == x:
        #X eh o jogador atual
        jogador = o
    else:
        #O eh o jogador atual
        jogador = x
    return jogador 
def posicao_eh_valida(posicao):
    if posicao == None:            
        return False 
    if posicao < 1 or posicao > 9:
        print("Essa posição não está no tabuleiro.")             
        return False
    if posicao_esta_preenchida(posicao):
        print("Posição já preenchida")
        return False        
    return True 

def exibir_titulo_do_jogo():    
    print("Jogo da Velha".title().center(40,"="))
                                  
def iniciar_jogo():
    
    fim_de_jogo = False
    numero_de_jogadas = 0 #número de jogadas realizadas
    jogador = JOGADOR_PRINCIPAL #define quem inicia a partida: X ou O

    #exibe as posições do tabuleiro para o usuário 
    informar_posicoes_do_tabuleiro(jogador) 
    
    while fim_de_jogo == False:        
        #recebe entrada do usuário        
        posicao = receber_posicao(jogador)        
        if posicao == ZERO:
            print("Jogo encerrado")
            break   
        if posicao_eh_valida(posicao):
            #adiciona a posição na lista de jogadas do jogador
            adicionar_posicao(jogador, posicao)
            #verifica se o jogador ganhou
            if jogador_ganhou(jogador):                
                exibir_mensagem_de_vitoria(jogador) 
                fim_de_jogo = True               
                #exibe o tabuleiro com as posições preenchidas 
                exibir_tabuleiro_de_jogadas(jogador, fim_de_jogo)               
                continue
            #altera a vez de jogo para outro jogador
            jogador = alterar_vez_de_jogo(jogador)
            #incrementa 1 a numero_de_jogadas
            numero_de_jogadas += 1
        else:
            #volta para o início do loop
            continue                         
        exibir_tabuleiro_de_jogadas(jogador)
        #verifica se deu empate
        if deu_empate(numero_de_jogadas):
            print("Empate")
            fim_de_jogo = True            

exibir_titulo_do_jogo()                          
iniciar_jogo()