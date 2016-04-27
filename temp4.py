import pygame
import random

class PygameGame(object):
    # cited from pygamegame.py by Lukas Peraza
    # for 15-112 F15 Pygame Optional Lecture, 11/11/15

    def init(self):
        pass

    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        pass

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=400, fps=30, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()

class Game(PygameGame):
    def init(self, stage=7, saved=False):
        self.stage = stage

        self.heroX = 200
        self.heroY = 300

        Hero.init()
        self.hero = Hero(self.heroX, self.heroY)
        self.heroGroup = pygame.sprite.GroupSingle(self.hero)

        self.gameOver = False

        self.temp = False

        self.saved = saved # if any save points were reached

        if self.stage == 7:
            self.initBoss1()

        self.key = True

    

    def keyPressed(self, code, mod):
        if code == pygame.K_SPACE:
            hero = self.heroGroup.sprites()[0]
            self.bullets.add(Bullet(hero.x + hero.width/2 * hero.direction + 2, 
                hero.y, hero.direction))

        if code == pygame.K_r:
            self.gameOver = False
            self.reborn()
            
    def reborn(self):
        self.bossTime = 0
        self.initBoss1()


    def resetMovingObstacles(self):
        



    def timerFired(self, dt):
        if self.gameOver == False or self.key == True:
            self.heroGroup.update(self.isKeyPressed, self.width, self.height)
            hero = self.heroGroup.sprite




    def redrawAll(self, screen):
        
        if self.key == False:
            self.collisions.draw(screen)
        self.heroGroup.draw(screen)
        
        if self.gameOver and self.key == False:
            gameOverImage = pygame.image.load("gameOver.png").convert_alpha()
            transformed = pygame.transform.scale(gameOverImage, (400, 100))
            screen.blit(transformed, (100, 150, 400, 300))