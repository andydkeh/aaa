import pygame
from pygame.locals import *
from tkinter import Tk, messagebox
from PIL import ImageTk

largura_tela = 800
altura_tela = 600

tamanho_bloco = 40

cor_fundo = (0, 0, 0)
cor_personagem = (255, 255, 0)
cor_saida = (0, 255, 0)

labirinto = [
    "XXXXXXXXXXXXXXXXXXXX",
    "X                  X",
    "X XXXXXXXXXX XXXX X",
    "X X           X   X",
    "X X XXXXXXXXX XXX X",
    "X X       X X     X",
    "X XXXXXXX X XXXXX X",
    "X                  X",
    "XXXXXXXXXXXXXXXXXXFX",
]


caminho_personagem = "C:/Users/endhy/OneDrive/Área de Trabalho/momo/baixados (2).jpg"
caminho_imagem_final = "C:/Users/endhy/OneDrive/Área de Trabalho/momo/baixados (1).jpg"
caminho_imagem_mensagem = "C:/Users/endhy/OneDrive/Área de Trabalho/momo/602a50cd54296ae5a5d539b0699cf452.jpg"
caminho_fundo = "C:/Users/endhy/OneDrive/Área de Trabalho/momo/zelda-wallpapers-1.jpg"

pygame.init()


tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Zelda Maze")

personagem_img = pygame.image.load(caminho_personagem)
imagem_final = pygame.image.load(caminho_imagem_final)
imagem_mensagem = pygame.image.load(caminho_imagem_mensagem)
fundo = pygame.image.load(caminho_fundo)
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))


personagem_img = pygame.transform.scale(personagem_img, (tamanho_bloco, tamanho_bloco))
imagem_final = pygame.transform.scale(imagem_final, (tamanho_bloco, tamanho_bloco))
imagem_mensagem = pygame.transform.scale(imagem_mensagem, (largura_tela, altura_tela))

posicao_personagem = [1, 1]

posicao_saida = [len(labirinto[0])-2, len(labirinto)-2]

def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            if labirinto[linha][coluna] == "X":
                pygame.draw.rect(tela, cor_fundo, (coluna*tamanho_bloco, linha*tamanho_bloco, tamanho_bloco, tamanho_bloco))
            elif labirinto[linha][coluna] == "F":
                tela.blit(imagem_final, (coluna*tamanho_bloco, linha*tamanho_bloco))

def desenhar_personagem():
    tela.blit(personagem_img, (posicao_personagem[0]*tamanho_bloco, posicao_personagem[1]*tamanho_bloco))

def mover_personagem(direcao):
    if direcao == "esquerda" and labirinto[posicao_personagem[1]][posicao_personagem[0]-1] != "X":
        posicao_personagem[0] -= 1
    elif direcao == "direita" and labirinto[posicao_personagem[1]][posicao_personagem[0]+1] != "X":
        posicao_personagem[0] += 1
    elif direcao == "cima" and labirinto[posicao_personagem[1]-1][posicao_personagem[0]] != "X":
        posicao_personagem[1] -= 1
    elif direcao == "baixo" and labirinto[posicao_personagem[1]+1][posicao_personagem[0]] != "X":
        posicao_personagem[1] += 1

def exibir_mensagem_final():
    tela.fill(cor_fundo)
    tela.blit(imagem_mensagem, (0, 0))
    pygame.display.update()
    pygame.time.delay(3000) 
    exibir_popup_mensagem("Agora estamos juntinhos hihih (p sempre ><)Eu te amo")
    pygame.quit()  


def exibir_popup_mensagem(mensagem):
    Tk().wm_withdraw()
    messagebox.showinfo("Mensagem", mensagem)

exibir_popup_mensagem("Venha me encontrar, momo <3")

jogo_ativo = True
while jogo_ativo:
    tela.fill(cor_fundo)

    tela.blit(fundo, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            jogo_ativo = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                mover_personagem("esquerda")
            elif event.key == K_RIGHT:
                mover_personagem("direita")
            elif event.key == K_UP:
                mover_personagem("cima")
            elif event.key == K_DOWN:
                mover_personagem("baixo")

    if posicao_personagem == posicao_saida:
        exibir_mensagem_final()

    desenhar_labirinto()
    desenhar_personagem()

    pygame.display.update()


pygame.quit()
