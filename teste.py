import sys, pygame, time
pygame.init()

#constantes iniciais
tamanho = largura, altura = 600, 600
inicio = [-2,5]
preto = 0, 255, 255

tela = pygame.display.set_mode(tamanho)
bola = pygame.image.load("C:\\Users\\lleod\\OneDrive\\Área de Trabalho\\Projeto aula quinta\\galo.jpeg")
bolarect = bola.get_rect()

while 1:
    for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

    bolarect = bolarect.move(inicio)
    if bolarect.left < 0 or bolarect.right > largura:
            inicio[0] = -inicio[0]
    if bolarect.top < 0 or bolarect.bottom > altura:
            inicio[1] = -inicio[1]
    
#controla a velocidade da bola  
    time.sleep(0.05)

#cria o display e exibe na tela os objetos
    tela.fill(preto)
    tela.blit(bola, bolarect)
    pygame.display.flip()