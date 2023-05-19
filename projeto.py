import pygame as pg
import sys, time
pg.init()

tamanho = altura , largura = 300 , 300
inicio = [-2,5]
azul = 255, 255, 0 

## metodo utilizado para definir tamanho da tela usada na aplicação.
screen = pg.display.set_mode(tamanho)

#importar imagem
bola = pg.image.load("C:\\Users\\lleod\\OneDrive\\Área de Trabalho\\Projeto aula quinta\\cerca.png")
bolarect = bola.get_rect()

while 1:
    for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()

    bolarect = bolarect.move(inicio)
    if bolarect.left < 0 or bolarect.right > largura:
            inicio[0] = -inicio[0]
    if bolarect.top < 0 or bolarect.bottom > altura:
            inicio[1] = -inicio[1]

    time.sleep(0.05)


    screen.fill(azul)
    screen.blit(bola, bolarect)
    pg.display.flip()
