import pygame


class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y
        self.frame = 1
        self.tick = 0


    def drawing(self, window):
        self.group.draw(window)


    def anim(self,image,tick,frames):
        self.tick+=1
        if self.tick >= tick:
            self.tick = 0
            self.frame += 1


        if self.frame > frames:
            self.frame = 1

        self.sprite.image = pygame.image.load('assets/'+image+ str(self.frame)+'.png')





class Bee(Obj):
    def __init__(self,image,x,y):
        super(Bee, self).__init__(image,x,y)
        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound('assets/sounds/score.wav')
        self.sound_bateu = pygame.mixer.Sound('assets/sounds/bateu.wav')


        self.life = 3
        self.pts= 0

    def move_bee(self,event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] -35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    def colision(self,group,name):
        name = name
        colison = pygame.sprite.spritecollide(self.sprite,group,True)

        if name == 'Flower' and colison:
            self.pts+=1
            self.sound_pts.play()
        elif name == 'Spider' and colison:
            self.life -= 1
            self.sound_bateu.play()



class Text:

    def __init__(self, size, txt):

        self.font= pygame.font.SysFont('Arial',size, True, True)
        self.render = self.font.render(txt, False, (255,255,255))



    def draw(self, window, x, y):

        window.blit(self.render,(x,y))


    def update_text(self,txt):
        self.render = self.font.render(txt, False, (255, 255, 255))

