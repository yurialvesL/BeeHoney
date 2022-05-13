import pygame
from menu import Menu,GameOver
from game import Game


class Main:

    def __init__(self, sizex, sizey, title):
        pygame.mixer.init()
        pygame.mixer.music.load('assets/sounds/bg.wav')
        pygame.mixer.music.play(-1)


        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu('assets/start.png')
        self.game = Game()
        self.game_over = GameOver('assets/gameover.png')

        self.loop = True
        self.fps = pygame.time.Clock()






    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if not self.menu.change_scene:
                self.menu.events(events)
            elif not self.game.change_scene:
                self.game.bee.move_bee(events)
            else:
                self.game_over.events(events)





    def draw(self):
        self.window.fill([0,0,0])
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.game_over.change_scene:
            self.game_over.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.game_over.change_scene = False
            self.game.bee.life = 3
            self.game.bee.pts = 0


    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()



if __name__ == '__main__':
    pygame.init()
    game = Main(360, 640, "BeeHoney")
    game.update()
