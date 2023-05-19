import pygame, os, random

pygame.init()

#TELA
larg = 1100  
altu =  600
screen= pygame.display.set_mode((larg , altu))

move = pygame.image.load("C:\\Users\\lleod\\OneDrive\\Área de Trabalho\\Projeto aula quinta\\galo.png")
jump = pygame.image.load("C:\\Users\\lleod\\OneDrive\\Área de Trabalho\\Projeto aula quinta\\fly.png")
cerca = pygame.image.load("C:\\Users\\lleod\\OneDrive\\Área de Trabalho\\Projeto aula quinta\\cerca.png")
bg = pygame.image.load("C:\\Users\\lleod\\OneDrive\\Área de Trabalho\\Projeto aula quinta\\bg.png")
cloud = pygame.image.load("C:\\Users\\lleod\\OneDrive\\Área de Trabalho\\Projeto aula quinta\\Cloud.png")

class Galo:
    x = 40
    y = 310
    jumpV = 8.5


    def __init__(self):
        self.run_image = move
        self.jump_image = jump

        self.galo_run = True
        self.galo_jump = False


        self.image = self.run_image
        self.jump_vel = self.jumpV
        self.galo_rect = self.image.get_rect()
        self.galo_rect.x = self.x
        self.galo_rect.y = self.y

    def mudança (self, userInput):
        if self.galo_run:
            self.run()
        if self.galo_jump:
            self.jump()



        if userInput[pygame.K_UP] and not self.galo_jump: #se apertar o up muda a imagem e o personagem pula
            self.galo_run = False
            self.galo_jump = True
        
        elif not (self.galo_jump):  #se não prescionar nada mantem a imagem de movimento 
            self.galo_run = True
            self.galo_jump = False


    def run (self):
        self.image = self.run_image
        self.galo_rect = self.image.get_rect() # define a imagem de movimento
        self.galo_rect.x = self.x
        self.galo_rect.y = self.y


    
    def jump (self):
        self.image = self.jump_image # define a imagem de pulo
        if self.galo_jump:
            self.galo_rect.y -= self.jump_vel * 4 #aumenta a velocidade do personagem quando pula
            self.jump_vel -= 0.8 # diminui quando cai
        if self.jump_vel < - self.jumpV: # se a velocidade do pulo for menor q a de movimento significa q o não esta pulando
            self.galo_jump = False
            self.jump_vel = self.jumpV



    def tela (self , screen):
        screen.blit(self.image, (self.galo_rect.x,self.galo_rect.y))

class Obstaulo:
    def __init__(self) :
        self.image = cerca
        self.xcerca = 600
        self.ycerca = 314
        self.screenside= 1100
        self.cerca_rect = self.image.get_rect()
        

    def mudança(self):
        self.xcerca -= game_speed
        if self.xcerca < -self.screenside: 
            self.xcerca = larg + random.randint(100 , 1000)
            self.ycerca = self.ycerca
            

    def tela(self, screen):
        screen.blit(self.image,(self.xcerca, self.ycerca))
                



class Cloud:
    def __init__(self):
        self.xcloud = larg + random.randint(800 , 1000)
        self.ycloud = random.randint(30 , 60)
        self.image = cloud
        self.largura = self.image.get_width()

    def mudança(self):
        self.xcloud -= game_speed
        if self.xcloud < -self.largura: #se a posiçãoX da nuvem for menor q a largura do mapa uma nova nuvem aparece
            self.xcloud = larg + random.randint(2500 , 3000)
            self.ycloud = random.randint(50 , 100)
        
    def tela(self , screen):
        screen.blit(self.image , (self.xcloud , self.ycloud))


def main():
    global game_speed , x_bg , y_bg , points, obst
    run = True
    clock = pygame.time.Clock()
    player = Galo()
    nuvem = Cloud()
    obstaculo = Obstaulo()
    x_bg = 0
    y_bg = 329 # posição do background
    game_speed = 14
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20) #tamanho da fonte

    def score():
        global points , game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1   #aumentar a valocidade a cada 1000 pontos

        text = font.render("Pontos: " + str(points), True, (0 , 0 , 0))
        textRect = text.get_rect()
        textRect.center= (1000 , 40)
        screen.blit(text , textRect)


    #def colisão():
        #obstaculos = []
        
        #colisões = pygame.sprite.spritecollide(player.galo_rect, obstaculo.cerca_rect, False)
        #if colisões == True:
            #pygame.quit()


    def background():
        global x_bg , y_bg 
        image_larg = bg.get_width()
        screen.blit(bg, (x_bg , y_bg))
        screen.blit(bg, (image_larg + x_bg , y_bg)) #printar o bg
        if x_bg <= -image_larg:
            screen.blit (bg, (image_larg + x_bg , y_bg)) #um if para cada vez q a imagem do bg terminar, logo em seguida começar outra
            x_bg = 0  
        x_bg -= game_speed   



    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((255, 140, 0))
        userInput = pygame.key.get_pressed()

        player.tela(screen)
        player.mudança(userInput)

        background()
        score()
        #colisão()

        nuvem.tela(screen)
        nuvem.mudança()


        obstaculo.tela(screen)
        obstaculo.mudança()
        

        clock.tick(30)
        pygame.display.update()


        










main()