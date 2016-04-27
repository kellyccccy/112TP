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
    def init(self, stage=0):
        self.stage = stage

        self.blockSize = 20
        self.hitWall = False

        self.heroX = 50
        self.heroY = 350

        self.gameOver = False

        self.saved = False # if any save points were reached

        Tile.init()
        self.tiles = pygame.sprite.Group()

        Grass.init()
        self.grasses = pygame.sprite.Group()

        Hero.init()
        self.hero = Hero(self.heroX, self.heroY)
        self.heroGroup = pygame.sprite.GroupSingle(self.hero)

        Obstacle.init()
        self.obstacles = pygame.sprite.Group()

        LeftObstacle.init()
        self.leftObstacles = pygame.sprite.Group()

        RightObstacle.init()
        self.rightObstacles = pygame.sprite.Group()

        FlippedObstacle.init()
        self.flippedObstacles = pygame.sprite.Group()

        LeftBar.init()
        self.leftBars = pygame.sprite.Group()

        RightBar.init()
        self.rightBars = pygame.sprite.Group()

        RisingObstacle.init()
        self.risingObstacles = pygame.sprite.Group()

        FallingObstacle.init()
        self.fallingObstacles = pygame.sprite.Group()

        ZoomingObstacle.init()
        self.zoomingObstacles = pygame.sprite.Group()

        SuperObstacle.init()
        self.superObstacles = pygame.sprite.Group()

        BabyObstacle.init()
        self.babyObstacles = pygame.sprite.Group()

        Save.init()
        self.saveGroup = pygame.sprite.GroupSingle()
        # there would/can only be one save point on one map

        GreenSave.init()
        self.greenSaveGroup = pygame.sprite.GroupSingle()

        Button.init()
        self.buttons = pygame.sprite.Group()

        FakeTile.init()
        self.fakeTiles = pygame.sprite.Group()

        Zombie.init()
        self.zombies = pygame.sprite.Group()

        self.bullets = pygame.sprite.Group()

        Collision.init()
        self.collisions = pygame.sprite.Group()

        EnemyCollision.init()
        self.enemyCollisions = pygame.sprite.Group()

        if self.stage == 0:
            self.initStage0()
        

    def getX(self, n):
        return n * self.blockSize + self.blockSize/2

    def getY(self, n):
        return 400 - n * self.blockSize - self.blockSize/2

    def initStage0(self):
        self.bgColor = (255, 255, 255)
        # init tiles on map
        for i in range(30):
            x = self.getX(i)
            y = self.getY(0)
            self.tiles.add(Tile(x, y))

        for i in range(5, 30):
            x = self.getX(i)
            y = self.getY(5)
            self.tiles.add(Tile(x, y))

        for i in range(25):
            x = self.getX(i)
            y = self.getY(10)
            self.tiles.add(Tile(x, y))

        for i in range(5, 30):
            x = self.getX(i)
            y = self.getY(15)
            self.tiles.add(Tile(x, y))

        for j in range(20):
            x = self.getX(0)
            y = self.getY(j)
            self.tiles.add(Tile(x, y))

        for j in range(16):
            x = self.getX(29)
            y = self.getY(j)
            self.tiles.add(Tile(x, y))

        # init grasses on map
        for i in range(1, 29):
            x = self.getX(i)
            y = self.getY(1)
            self.grasses.add(Grass(x, y))

        for i in range(5, 29):
            x = self.getX(i)
            y = self.getY(6)
            self.grasses.add(Grass(x, y))

        for i in range(1, 25):
            x = self.getX(i)
            y = self.getY(11)
            self.grasses.add(Grass(x, y))

        for i in range(5, 30):
            x = self.getX(i)
            y = self.getY(16)
            self.grasses.add(Grass(x, y))

        # init obstacles on map
        for i in range(4, 25, 6):
            x = self.getX(i)
            y = self.getY(12)
            self.obstacles.add(Obstacle(x, y))

        # init flipped obstacles on map
        for i in range(7, 29, 6):
            x = self.getX(i)
            y = self.getY(4)
            self.flippedObstacles.add(FlippedObstacle(x, y))

        for i in range(7, 23, 6):
            x = self.getX(i)
            y = self.getY(14)
            self.flippedObstacles.add(FlippedObstacle(x, y))

        # init left obstacles on map
        # for j in range(5, 7):
        #     x = self.getX(4)
        #     y = self.getY(j)
        #     self.leftObstacles.add(LeftObstacle(x, y))

        # for j in range(15, 17):
        #     x = self.getX(4)
        #     y = self.getY(j)
        #     self.leftObstacles.add(LeftObstacle(x, y))

        # init right obstacles on map
        # for j in range(10, 12):
        #     x = self.getX(25)
        #     y = self.getY(j)
        #     self.rightObstacles.add(RightObstacle(x, y))

        # init left bars on map
        # self.leftBars.add(LeftBar(600, 140))

        # init right bars on map
        # self.rightBars.add(RightBar(0, 240))

        # init rising obstacles on map
        # for i in range(4, 27, 6):
        #     x = self.getX(i)
        #     y = self.getY(2)
        #     self.risingObstacles.add(RisingObstacle(x, y))

        # init falling obstacle on map
        # self.fallingObstacles.add(FallingObstacle(self.getX(19), self.getY(14)))

        # init super obstacle on map
        # self.superObstacles.add(SuperObstacle(self.getX(16), self.getY(12)))

        # init zombies on map
        for n in range(5):
            x = random.randint(150, 550)
            y = 264
            self.zombies.add(Zombie(x, y))

        # init button on map
        self.button = Button(self.getX(28), self.getY(3), False)
        self.buttons.add(self.button)

        # init fake tiles on map
        for j in range(16, 20):
            x = self.getX(29)
            y = self.getY(j)
            self.fakeTiles.add(FakeTile(x, y))


        # init saves on map
        self.save = Save(self.getX(23), self.getY(12))
        self.saveGroup.add(self.save)


    def initStage1(self):
        self.bgColor = (255, 255, 255)
        # init tiles on map
        for i in range(30):
            x = self.getX(i)
            y = self.getY(0)
            self.tiles.add(Tile(x, y))
        for i in range(5):
            x = self.getX(i)
            y1 = self.getY(1)
            y2 = self.getY(2)
            self.tiles.add(Tile(x, y1))
            self.tiles.add(Tile(x, y2))
        for i in range(24, 30):
            x = self.getX(i)
            y1 = self.getY(1)
            y2 = self.getY(2)
            self.tiles.add(Tile(x, y1))
            self.tiles.add(Tile(x, y2))
        for i in range(4):
            x = self.getX(i)
            y1 = self.getY(3)
            y2 = self.getY(4)
            y3 = self.getY(5)
            self.tiles.add(Tile(x, y1))
            self.tiles.add(Tile(x, y2))
            self.tiles.add(Tile(x, y3))
        for i in range(25, 30):
            x = self.getX(i)
            y1 = self.getY(3)
            y2 = self.getY(4)
            self.tiles.add(Tile(x, y1))
            self.tiles.add(Tile(x, y2))
        for i in range(26, 30):
            for j in range(5, 17):
                x = self.getX(i)
                y = self.getY(j)
                self.tiles.add(Tile(x, y))
        for i in range(7, 22):
            x = self.getX(i)
            y = self.getY(4)
            self.tiles.add(Tile(x, y))
        for i in range(9, 21):
            x = self.getX(i)
            y = self.getY(5)
            self.tiles.add(Tile(x, y))
        for i in range(13, 15):
            x = self.getX(i)
            y1 = self.getY(6)
            y2 = self.getY(7)
            self.tiles.add(Tile(x, y1))
            self.tiles.add(Tile(x, y2))
        self.tiles.add(Tile(self.getX(13), self.getY(8)))
        self.tiles.add(Tile(self.getX(8), self.getY(10)))
        self.tiles.add(Tile(self.getX(9), self.getY(10)))
        for i in range(14, 16):
            x = self.getX(i)
            y = self.getY(13)
            self.tiles.add(Tile(x, y))
        self.tiles.add(Tile(self.getX(25), self.getY(10)))
        self.tiles.add(Tile(self.getX(24), self.getY(11)))
        self.tiles.add(Tile(self.getX(25), self.getY(11)))
        self.tiles.add(Tile(self.getX(25), self.getY(20)))

        # init grass on map
        for i in range(5, 24):
            x = self.getX(i)
            y = self.getY(0)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(4), self.getY(3)))
        for i in range(4):
            x = self.getX(i)
            y = self.getY(6)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(24), self.getY(3)))
        self.grasses.add(Grass(self.getX(25), self.getY(5)))
        for i in range(7, 9):
            x = self.getX(i)
            y = self.getY(5)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(21), self.getY(5)))
        for i in range(9, 13):
            x = self.getX(i)
            y = self.getY(6)
            self.grasses.add(Grass(x, y))
        for i in range(15, 21):
            x = self.getX(i)
            y = self.getY(6)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(13), self.getY(9)))
        self.grasses.add(Grass(self.getX(14), self.getY(8)))
        self.grasses.add(Grass(self.getX(7), self.getY(10)))
        self.grasses.add(Grass(self.getX(8), self.getY(11)))
        self.grasses.add(Grass(self.getX(9), self.getY(11)))
        self.grasses.add(Grass(self.getX(10), self.getY(10)))
        for i in range(13, 17):
            x = self.getX(i)
            y = self.getY(14)
            self.grasses.add(Grass(x, y))
        for i in range(23, 26):
            x = self.getX(i)
            y = self.getY(12)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(25), self.getY(15)))
        self.grasses.add(Grass(self.getX(25), self.getY(17)))
        for i in range(26, 30):
            x = self.getX(i)
            y = self.getY(17)
            self.grasses.add(Grass(x, y))

        # init obstacles on map
        for i in range(9, 22, 6):
            x = self.getX(i)
            y = self.getY(1)
            self.obstacles.add(Obstacle(x, y))
        for i in range(7, 9):
            x = self.getX(i)
            y = self.getY(6)
            self.obstacles.add(Obstacle(x, y))
        for i in range(9, 13):
            x = self.getX(i)
            y = self.getY(7)
            self.obstacles.add(Obstacle(x, y))
        self.obstacles.add(Obstacle(self.getX(15), self.getY(7)))
        self.obstacles.add(Obstacle(self.getX(18), self.getY(7)))
        self.obstacles.add(Obstacle(self.getX(20), self.getY(7)))
        self.obstacles.add(Obstacle(self.getX(7), self.getY(11)))
        self.obstacles.add(Obstacle(self.getX(8), self.getY(12)))
        self.obstacles.add(Obstacle(self.getX(10), self.getY(11)))
        self.obstacles.add(Obstacle(self.getX(15), self.getY(15)))

        # init flipped obstacles on map
        for i in range(12, 25, 6):
            x = self.getX(i)
            y = self.getY(3)
            self.flippedObstacles.add(FlippedObstacle(x, y))
        self.flippedObstacles.add(FlippedObstacle(self.getX(7), self.getY(9)))
        self.flippedObstacles.add(FlippedObstacle(self.getX(8), self.getY(9)))
        self.flippedObstacles.add(FlippedObstacle(self.getX(13), self.getY(13)))
        self.flippedObstacles.add(FlippedObstacle(self.getX(15), self.getY(12)))
        self.flippedObstacles.add(FlippedObstacle(self.getX(16), self.getY(13)))

        # init left obstacles on map
        for j in range(6, 10):
            x = self.getX(25)
            y = self.getY(j)
            self.leftObstacles.add(LeftObstacle(x, y))

        # init saving points on map
        self.save = Save(self.getX(24), self.getY(4))
        self.saveGroup.add(self.save)


    def initStage2(self):
        self.bgColor = (255, 255, 255)
        # init tiles on map
        for i in range(30):
            for j in range(10):
                x = self.getX(i)
                y = self.getY(j)
                self.tiles.add(Tile(x, y))

        # init grasses on map
        for i in range(30):
            x = self.getX(i)
            y = self.getY(10)
            self.grasses.add(Grass(x, y))

        # init zooming obstacles on map
        for i in range(6, 30, 4):
            x = self.getX(i)
            y = self.getY(12) - 10
            self.zoomingObstacles.add(ZoomingObstacle(x, y))

        # init saving points on map
        self.save = Save(30, 100)
        self.saveGroup.add(self.save)

        
    def keyPressed(self, code, mod):
        if code == pygame.K_SPACE:
            hero = self.heroGroup.sprites()[0]
            self.bullets.add(Bullet(hero.x + hero.width/2 * hero.direction + 2, 
                hero.y, hero.direction))

        if code == pygame.K_r:
            self.gameOver = False
            if self.saved == True and self.stage == self.greenSave.stage:
                # if there is already a saving point on the same stage
                self.hero = Hero(self.heroX, self.heroY)
                self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                self.resetMovingObstacles()
            elif self.saved == True and self.stage != self.greenSave.stage:
                # if there has been a saving point but not on the stage
                self.stage = self.greenSave.stage
                self.hero = Hero(self.greenSave.x, self.greenSave.y)
                self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                self.resetMovingObstacles()
                if self.stage == 0:
                    self.initStage0()
                elif self.stage == 1:
                    self.initStage1()
                elif self.stage == 2:
                    self.initStage2()
            else: # if the game has not yet been saved
                self.hero = Hero(self.heroX, self.heroY)
                self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                self.resetMovingObstacles()
                if self.stage == 0:
                    self.initStage0()




    def resetMovingObstacles(self):
        self.bullets = pygame.sprite.Group()
        self.collisions = pygame.sprite.Group()
        self.zombies = pygame.sprite.Group()
        for risingObstacle in self.risingObstacles:
            risingObstacle.move = False
        for fallingObstacle in self.fallingObstacles:
            fallingObstacle.move = False
        for leftBar in self.leftBars:
            leftBar.move = False
        for rightBar in self.rightBars:
            rightBar.move = False
        for superObstacle in self.superObstacles:
            superObstacle.activated = False
        self.babyObstacles = pygame.sprite.Group() # clear all activated babies


    def touchObstacle(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        # print(heroX, heroY, heroW, heroH)
        for obstacle in self.obstacles:
            # print(obstacle.x, obstacle.y)
            if (abs(heroX - obstacle.x) <= (heroW/2 + obstacle.blockSize/2) 
                and abs(heroY - obstacle.y) <= (heroH/2 + obstacle.blockSize/2)
                and (abs(heroX - obstacle.x) < heroW/2 + 
                    (heroY + heroH/2 - (obstacle.y - obstacle.blockSize/2))/2)):
                return True
        return False

    def touchFlippedObstacle(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        # print(heroX, heroY, heroW, heroH)
        for flipped in self.flippedObstacles:
            if (abs(heroX - flipped.x) <= (heroW/2 + flipped.blockSize/2) 
                and abs(heroY - flipped.y) <= (heroH/2 + flipped.blockSize/2)
                and (abs(heroX - flipped.x) < heroW/2 + 
                    (flipped.y + flipped.blockSize/2 - (heroY - heroH/2))/2)):
                return True
        return False

    def touchLeftObstacle(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        for left in self.leftObstacles:
            if (abs(heroX - left.x) <= (heroW/2 + left.blockSize/2) 
                and abs(heroY - left.y) <= (heroH/2 + left.blockSize/2)
                and (abs(heroY - left.y) < heroH/2 + 
                    (heroX + heroW/2 - (left.x - left.blockSize/2))/2)):
                return True
        return False

    def touchRightObstacle(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        for right in self.rightObstacles:
            if (abs(heroX - right.x) <= (heroW/2 + right.blockSize/2) 
                and abs(heroY - right.y) <= (heroH/2 + right.blockSize/2)
                and (abs(heroY - right.y) < heroH/2 + 
                    (right.x + right.blockSize/2 - (heroX - heroW/2))/2)):
                return True
        return False


    def touchZoomingObstacle(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        for zooming in self.zoomingObstacles:
            if (abs(heroX - zooming.x) <= (heroW/2 + zooming.size/2) 
                and abs(heroY - zooming.y) <= (heroH/2 + zooming.size/2)
                and (abs(heroX - zooming.x) < heroW/2 + 
                    (heroY + heroH/2 - (zooming.y - zooming.size/2))/2)):
                return True
        return False


    def touchSuperObstacle(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        for superO in self.superObstacles:
            if (abs(heroX - superO.x) <= (heroW/2 + superO.blockSize/2) 
                and abs(heroY - superO.y) <= (heroH/2 + superO.blockSize/2)
                and (abs(heroX - superO.x) < heroW/2 + 
                    (heroY + heroH/2 - (superO.y - superO.blockSize/2))/2)):
                return True
        return False


    def touchBabyObstacle(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        for baby in self.babyObstacles:
            if (abs(heroX - baby.x) <= (heroW/2 + baby.blockSize/2) 
                and abs(heroY - baby.y) <= (heroH/2 + baby.blockSize/2)
                and (abs(heroX - baby.x) < heroW/2 + 
                    (heroY + heroH/2 - (baby.y - baby.blockSize/2))/2)):
                return True
        return False


    def timerFired(self, dt):
        if self.gameOver == False:
            self.heroGroup.update(self.isKeyPressed, self.width, self.height)
            hero = self.heroGroup.sprite

            self.zombies.update(self.width, self.height)

            self.bullets.update(self.width, self.height)

            self.zoomingObstacles.update(self.width, self.height)

            self.superObstacles.update(self.width, self.height)
            self.babyObstacles.update(self.width, self.height)

            self.fakeTiles.update(self.width, self.height)

            if self.stage == 0:
                self.timerFired0(dt)

            # if player hits nextStage, then next stage
            if self.hero.x + self.hero.width/2 >= 590:
                self.stage += 1
                if self.stage == 1:
                    self.init(self.stage)
                    self.hero = Hero(30, 230)
                    self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                    self.initStage1()
                elif self.stage == 2:
                    self.init(self.stage)
                    self.hero = Hero(20, 150)
                    self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                    self.initStage2()
                # elif self.stage == 3:
                #     self.initStage3()
                # else:
                #     self.initBoss()

            # if hits an obstacle (a triangle spike)
            if self.touchObstacle():
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            elif self.touchFlippedObstacle():
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            elif self.touchLeftObstacle():
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            elif self.touchRightObstacle():
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            elif self.touchZoomingObstacle():
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            elif self.touchSuperObstacle():
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            elif self.touchBabyObstacle():
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True
            

            # if bars come and hit player, game over
            if pygame.sprite.groupcollide(self.heroGroup, self.leftBars, 
                False, True, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            if pygame.sprite.groupcollide(self.heroGroup, self.rightBars, 
                False, True, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            # if moving obstacles come and hit player, game over
            if pygame.sprite.groupcollide(self.heroGroup, self.risingObstacles, 
                False, True, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            if pygame.sprite.groupcollide(self.heroGroup, self.fallingObstacles, 
                False, True, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            # if player hits save, then save (green save)
            if pygame.sprite.groupcollide(self.heroGroup, self.saveGroup, 
                False, True, pygame.sprite.collide_circle):
                self.heroX = self.save.x
                self.heroY = self.save.y
                self.greenSave = GreenSave(self.heroX, self.heroY,
                    self.save.stage)
                self.greenSaveGroup.add(self.greenSave)

            # if player hits button, then activate
            if pygame.sprite.groupcollide(self.heroGroup, self.buttons,
                False, True, pygame.sprite.collide_circle):
                self.buttons.add(Button(self.button.x+5, self.button.y, True))
                self.buttons.update(self.width, self.height)

            # if enemy collides with bullet, enemy dies
            if pygame.sprite.groupcollide(self.zombies, self.bullets,
                True, True, pygame.sprite.collide_circle):
                pass

            # if player collides with enemy, hero dies
            if pygame.sprite.groupcollide(self.heroGroup, self.zombies, 
                False, False, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            # players cannot touch fake tiles or be hit by them
            if pygame.sprite.groupcollide(self.heroGroup, self.fakeTiles,
                False, False, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

        # if player dies, game over, press r, and reborn at saving point


    def timerFired0(self, dt): # activation points for stage 0

        # update bars when hero moves to some range of x and y
        for rightBar in self.rightBars:
            if (self.hero.y <= 260 and self.hero.x >= 500):
                rightBar.move = True
            if rightBar.move == True:
                rightBar.update(self.width, self.height)

        for leftBar in self.leftBars:
            if (self.hero.y <= 160 and self.hero.x <= 100):
                leftBar.move = True
            if leftBar.move == True:
                leftBar.update(self.width, self.height)

        # update moving obstacles when hero moves to some range of x and y
        for fallingObstacle in self.fallingObstacles:
            if (self.hero.y <= 260 and self.hero.x >= 380):
                fallingObstacle.move = True
            if fallingObstacle.move == True:
                fallingObstacle.update(self.width, self.height)

        for risingObstacle in self.risingObstacles:
            if (self.hero.y <= 60 and risingObstacle.x - self.hero.x <= 20):
                risingObstacle.move = True
            if risingObstacle.move == True:
                risingObstacle.update(self.width, self.height)

        # update zombies when hero moves near
        for zombie in self.zombies:
            if (zombie.x - self.hero.x <= 150 and 
                abs(zombie.y - self.hero.y) <= 30):
                zombie.activated = True
            if zombie.activated == True and dt%3 == 0:
                zombie.upgrade()

        # update superObstacles when hero moves near
        for superObstacle in self.superObstacles:
            if (abs(superObstacle.x - self.hero.x) <= 50 and
                abs(superObstacle.y - self.hero.y) <= 20):
                superObstacle.activated = True


    # def getXStatus(self): # check whether the hero hits the wall
    #     return self.hitWall

    def redrawAll(self, screen):
        self.obstacles.draw(screen)
        self.flippedObstacles.draw(screen)
        self.leftObstacles.draw(screen)
        self.rightObstacles.draw(screen)
        self.risingObstacles.draw(screen)
        self.fallingObstacles.draw(screen)
        self.superObstacles.draw(screen)
        self.babyObstacles.draw(screen)
        self.buttons.draw(screen)
        self.zombies.draw(screen)
        self.leftBars.draw(screen)
        self.rightBars.draw(screen)
        self.tiles.draw(screen)
        self.grasses.draw(screen)
        self.saveGroup.draw(screen)
        self.greenSaveGroup.draw(screen)
        self.fakeTiles.draw(screen)
        self.zoomingObstacles.draw(screen)
        self.collisions.draw(screen)
        self.heroGroup.draw(screen)
        self.bullets.draw(screen)
        self.enemyCollisions.draw(screen)
        if self.gameOver:
            gameOverImage = pygame.image.load("gameOver.png").convert()
            transformed = pygame.transform.scale(gameOverImage, (400, 100))
            screen.blit(transformed, (100, 150, 400, 300))



class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, radius):
        super(GameObject, self).__init__()
        # x, y define the center of the object
        self.x, self.y, self.image, self.radius = x, y, image, radius
        self.baseImage = image.copy()
        w, h = image.get_size()
        self.updateRect()
        self.xSpeed = 0
        self.ySpeed = 0
        self.blockSize = IWANNA.blockSize

    def updateRect(self):
        # update the object's rect attributes with the new x, y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w/2, self.y - h/2, w, h)

    def update(self, screenWidth, screenHeight):
        self.x += self.xSpeed
        self.y += self.ySpeed
        self.updateRect()



class Hero(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("hero.png").convert()
        Hero.heroImage = pygame.transform.scale(image, (20, 20))

    def flipImage(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def __init__(self, x, y):
        super(Hero, self).__init__(x, y, Hero.heroImage, 10)
        self.size = 20
        self.image = Hero.heroImage
        self.flipped = False
        self.maxSpeed = 5
        self.maxYSpeed = 5
        self.gravity = 0.5
        self.jump = -3
        self.direction = 1
        # 2 directions: 1 for to right, -1 for to left
        self.yStatus = 1
        # 2 states: 1 for on ground, 0 for in air
        # self.jumpTime = 0
        # self.jumpCount = 0
        self.deltaX = 0
        self.deltaY = 0

    def yInRange(self, block): # block can be a tile or a grass
        if ((block.y - block.blockSize/2 > self.y - self.height/2) and
            (block.y - block.blockSize/2 < self.y + self.height/2)):
            return True
        elif ((block.y + block.blockSize/2 >= self.y - self.height/2) and
            (block.y + block.blockSize/2 <= self.y + self.height/2)):
            return True
        return False

    def xInRange(self, block): # block can be a tile or a grass
        if ((block.x - block.blockSize/2 >= self.x - self.width/2) and
            (block.x - block.blockSize/2 <= self.x + self.width/2)):
            return True
        elif ((block.x + block.blockSize/2 >= self.x - self.width/2) and
            (block.x + block.blockSize/2 <= self.x + self.width/2)):
            return True
        return False

    def isLegalMoveLeft(self):
        if self.x - self.width/2 - self.xSpeed < 0: # out of the screen
            return False
        else:
            for tile in IWANNA.tiles:
                # check every tile's relative position to the hero
                # first check if the tile's y is in range
                # print("left, tile", self.yInRange(tile))
                if (self.yInRange(tile) and 
                    # the hero was to the right of the block
                    self.x > tile.x and
                    # check if in the next frame, hero will collide with block
                    (self.x-self.width/2-self.xSpeed<=tile.x+tile.blockSize/2)):
                    self.deltaX = tile.x+tile.blockSize/2-(self.x-self.width/2)
                    # print("move left, hit tile", tile.x, tile.y)
                    return False
            for grass in IWANNA.grasses:
                # check every grass's relative position to the hero
                # print("left, grass", self.yInRange(grass))
                if (self.yInRange(grass) and
                    self.x > grass.x and 
                    (self.x-self.width/2-self.xSpeed<=grass.x+grass.blockSize/2)):
                    self.deltaX = self.x-self.width/2-(grass.x+grass.blockSize/2)
                    # print("move left, hit grass", grass.x, grass.y)
                    return False
        # if within screen and will not collide, return True
        # print("isLegalMoveLeft")
        return True

    def isLegalMoveRight(self):
        if self.x + self.width/2 + self.xSpeed > 600: # out of the screen
            return False
        else:
            # similar to isLegalMoveLeft method
            for tile in IWANNA.tiles:
                # print("right, tile", self.yInRange(tile))
                if (self.yInRange(tile) and
                    self.x < tile.x and
                    self.x+self.width/2+self.xSpeed>=tile.x-tile.blockSize/2):
                    self.xSpeed = tile.x+tile.blockSize/2-(self.x-self.width/2)
                    # print("move right, hit tile", tile.x, tile.y)
                    return False
            for grass in IWANNA.grasses:
                # print("right, grass", self.yInRange(grass))
                if (self.yInRange(grass) and
                    self.x < grass.x and
                    self.x+self.width/2+self.xSpeed>=grass.x-grass.blockSize/2):
                    self.xSpeed = grass.x+grass.blockSize/2-(self.x-self.width/2)
                    # print("move right, hit grass", grass.x, grass.y)
                    return False
        # print("isLegalMoveRight")
        return True

    def isLegalJump(self):
        # print("checking moving up")
        if self.y - self.height/2 + self.ySpeed < 0: # out of screen
            # print("out of screen", self.y, self.ySpeed)
            return False
        else:
            # similar to isLegalMoveLeft and isLegalMoveRight methods
            for tile in IWANNA.tiles:
                # print("inrange", self.xInRange(tile))
                if (self.xInRange(tile) and (self.y > tile.y) and
                    # check if hero's top will collide with a tile's bottom
                    self.y-self.height/2+self.ySpeed<=tile.y+tile.blockSize/2):
                    self.deltaY = tile.y+tile.blockSize/2-(self.y-self.height/2)
                    # print("jump, hit tile", tile.x, tile.y, self.deltaY)
                    return False
            # for grass in IWANNA.grasses:
            #     if (self.xInRange(grass) and (self.y > grass.y) and
            #         self.y-self.height/2+self.ySpeed<grass.y+grass.blockSize/2):
            #         self.deltaY=grass.y+grass.blockSize/2-(self.y-self.height/2)
            #         print("jump, hit grass", grass.x, grass.y, self.deltaY)
            #         return False
        # print("isLegalJump", self.y, self.ySpeed)
        return True

    def isLegalFall(self):
        for grass in IWANNA.grasses:
            if (self.xInRange(grass) and self.y < grass.y and
                self.y+self.height/2+self.ySpeed>=grass.y-grass.blockSize/2):
                self.deltaY = grass.y-grass.blockSize/2-(self.y+self.height/2)
                # print("fall, hit grass", grass.x, grass.y, self.deltaY)
                return False
        # print("isLegalFall")
        return True

    def moveLeft(self):
        # print("moving left")
        self.xSpeed = self.maxSpeed
        if self.isLegalMoveLeft():
            self.xSpeed = self.xSpeed * self.direction
        else:
            self.xSpeed = self.deltaX

    def moveRight(self):
        # print("moving right")
        self.xSpeed = self.maxSpeed
        if self.isLegalMoveRight():
            self.xSpeed = self.xSpeed * self.direction
        else:
            self.xSpeed = self.deltaX

    def moveUp(self):
        # print("moving up")
        self.yStatus = 0 # in air
        self.ySpeed += self.jump
        if self.isLegalJump():
            # print("legal jump", self.x, self.y, self.ySpeed)
            if abs(self.ySpeed) >= self.maxYSpeed:
                self.ySpeed = -self.maxYSpeed
        else:
            self.ySpeed = self.deltaY
            # print("moving up", self.y, self.ySpeed)
        # print("yspeed", self.ySpeed)

    def update(self, keysDown, screenWidth, screenHeight):
        # print("position", self.x, self.y, "direction", self.direction)
        if keysDown(pygame.K_LEFT): # try to move left
            if self.direction == 1:
                self.flipped = True
            else: self.flipped = False
            self.direction = -1
            self.moveLeft()

        elif keysDown(pygame.K_RIGHT): # try to move right
            if self.direction == -1:
                self.flipped = True
            else: self.flipped = False
            self.direction = 1
            self.moveRight()

        else:
            self.xSpeed = 0

        if keysDown(pygame.K_UP): # try to jump
            self.moveUp()

            # self.yStatus = 0 # in air
            # self.jumpTime += 1
            # self.ySpeed += self.jump
            # if self.jumpTime > 30:
            #     self.ySpeed = 0
            #     self.jumpCount += 1
        
        elif self.isLegalFall(): # in air but not jumping, i.e. free fall
            # print("falling")
            self.ySpeed += self.gravity
            if not self.isLegalJump():
                self.ySpeed = self.deltaY

        else: # hit the ground
            self.yStatus = 1
            # print("deltaY", self.deltaY)
            self.jumpCount = 0
            self.jumpTime = 0
            self.ySpeed = self.deltaY

        if self.flipped == True:
            self.flipImage()

        self.deltaX = 0
        self.deltaY = 0
        super(Hero, self).update(screenWidth, screenHeight)



class Tile(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("tile.png").convert()
        Tile.tileImage = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Tile, self).__init__(x, y, Tile.tileImage, 10)


class Grass(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("grass.png").convert()
        Grass.grassImage = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Grass, self).__init__(x, y, Grass.grassImage, 10)


class Save(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("save.png").convert()
        Save.saveImage = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Save, self).__init__(x, y, Save.saveImage, 10)
        self.stage = IWANNA.stage


class GreenSave(GameObject): # for save points that have been reached
    @staticmethod
    def init():
        image = pygame.image.load("greenSave.png").convert()
        GreenSave.saveImage = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y, stage):
        super(GreenSave, self).__init__(x, y, GreenSave.saveImage, 10)
        self.stage = stage


class Button(GameObject):
    @staticmethod
    def init():
        # icon for not activated button
        image0 = pygame.image.load("button1.png").convert_alpha()
        Button.image0 = pygame.transform.scale(image0, (20, 20))
        # icon for activated button
        image1 = pygame.image.load("button2.png").convert_alpha()
        Button.image1 = pygame.transform.scale(image1, (10, 20))

    def __init__(self, x, y, activated):
        self.activated = activated
        if self.activated == False:
            super(Button, self).__init__(x, y, Button.image0, 10)
        else:
            super(Button, self).__init__(x, y, Button.image1, 5)

    def activate(self):
        for fake in IWANNA.fakeTiles:
            fake.collapsing = True

    def update(self, screenWidth, screenHeight):
    #     # print(self.activated)
        if self.activated == True:
            self.activate()
        super(Button, self).update(screenWidth, screenHeight)


class FakeTile(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("fakeTile.png").convert_alpha()
        FakeTile.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(FakeTile, self).__init__(x, y, FakeTile.image, 10)
        self.original = FakeTile.image
        self.image = self.original
        self.angle = 0
        self.collapsing = False
        self.initXSpeed = -1.5
        self.initYSpeed = -1
        self.gravity = 0.5

    def collapse(self):
        # when a fake tile collapses, it rises at first and then falls 
        # (with gravitation acceleration) while rotating
        self.xSpeed = self.initXSpeed
        if self.angle == 0:
            self.ySpeed = self.initYSpeed
        self.angle += 5
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.ySpeed += self.gravity
        
    def update(self, screenWidth, screenHeight):
        if self.collapsing == True:
            self.collapse()
        if self.y > 410:
            self.kill()
        super(FakeTile, self).update(screenWidth, screenHeight)


class Obstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("spike.png").convert_alpha()
        Obstacle.obstacleImage = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Obstacle, self).__init__(x, y, Obstacle.obstacleImage, 10)


class FlippedObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("flipped.png").convert_alpha()
        FlippedObstacle.obstacleImage = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(FlippedObstacle, self).__init__(
            x, y, FlippedObstacle.obstacleImage, 10)


class LeftObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("left.png").convert_alpha()
        LeftObstacle.obstacleImage = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(LeftObstacle, self).__init__(
            x, y, LeftObstacle.obstacleImage, 10)


class RightObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("right.png").convert_alpha()
        RightObstacle.obstacleImage = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(RightObstacle, self).__init__(
            x, y, RightObstacle.obstacleImage, 10)


class RisingObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("risingO.png").convert_alpha()
        RisingObstacle.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(RisingObstacle, self).__init__(x, y, RisingObstacle.image, 10)
        self.ySpeed = -60
        self.move = False


class FallingObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("fallingO.png").convert_alpha()
        FallingObstacle.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(FallingObstacle, self).__init__(x, y, FallingObstacle.image, 10)
        self.ySpeed = 20
        self.move = False


class ZoomingObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("zooming.png").convert()
        ZoomingObstacle.image = pygame.transform.scale(image, (80, 80))

    def __init__(self, x, y):
        super(ZoomingObstacle, self).__init__(x, y, ZoomingObstacle.image, 40)
        self.original = ZoomingObstacle.image
        self.image = ZoomingObstacle.image
        self.size = 80
        self.minSize = 20
        self.maxSize = 80
        self.addSize = 2 # size grow 2 at a time
        self.addY = 1 # self.y change 1 at a time
        self.enlarge = False # become larger if True, smaller if False

    def setEnlarge(self):
        if self.size == self.minSize:
            self.enlarge = True # begin to grow
        elif self.size == self.maxSize:
            self.enlarge = False # begin to shrink

    def zoom(self):
        self.setEnlarge()
        if self.enlarge == True:
            self.size += self.addSize
            self.ySpeed = 0 - self.addY
        else:
            self.size -= self.addSize
            self.ySpeed = self.addY
        self.image = pygame.transform.scale(self.original, (self.size, self.size))

    def update(self, screenWidth, screenHeight):
        self.zoom()
        super(ZoomingObstacle, self).update(screenWidth, screenHeight)


class SuperObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("super.png").convert_alpha()
        SuperObstacle.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(SuperObstacle, self).__init__(x, y, SuperObstacle.image, 10)
        self.activated = False

    def split(self):
        for xdirection in (-1, 0, 1):
            for ydirection in (-1, 1):
                IWANNA.babyObstacles.add(BabyObstacle(
                    self.x, self.y, xdirection, ydirection))

    def update(self, screenWidth, screenHeight):
        if self.activated == True:
            self.split()
            self.kill()
        else:
            super(SuperObstacle, self).update(screenWidth, screenHeight)


class BabyObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("spike.png").convert_alpha()
        BabyObstacle.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y, xdirection, ydirection):
        super(BabyObstacle, self).__init__(x, y, BabyObstacle.image, 10)
        self.xdirection = xdirection # 1 for right, -1 for left
        self.ydirection = ydirection # 1 for down, -1 for up
        self.initXSpeed1 = 3 # initial x speed when beginning to move
        self.initXSpeed2 = 10
        self.initYSpeed1 = 15 # initial y speed when beginning to move
        self.initYSpeed2 = 20
        self.gravity = 1 # baby obstacles rise and fall with gravity
        self.isMoving = True
        if self.ydirection == 1:
            self.xSpeed = self.xdirection * self.initXSpeed2
            self.ySpeed = self.ydirection * self.initYSpeed2
        elif self.ydirection == -1:
            self.xSpeed = self.xdirection * self.initXSpeed1
            self.ySpeed = self.ydirection * self.initYSpeed1
        self.deltaY = 0
        self.bufferLevel = 0

    def xInRange(self, block): # block can be a tile or a grass
        if ((block.x - block.blockSize/2 >= self.x - self.width/2) and
            (block.x - block.blockSize/2 <= self.x + self.width/2)):
            return True
        elif ((block.x + block.blockSize/2 >= self.x - self.width/2) and
            (block.x + block.blockSize/2 <= self.x + self.width/2)):
            return True
        return False

    def isLegalFall(self):
        for grass in IWANNA.grasses:
            if (self.xInRange(grass) and self.y < grass.y and
                self.y+self.height/2+self.ySpeed >= grass.y-grass.blockSize/2):
                self.deltaY = grass.y-grass.blockSize/2-(self.y+self.height/2)
                return False
        return True

    def move(self):
        if self.ydirection == -1:
            if self.ySpeed <= 0: # when the baby obstacle is rising up
                self.ySpeed += self.gravity

            elif self.ySpeed > 0: # when the baby obstacle is falling
                if self.isLegalFall():
                    self.ySpeed += self.gravity
                else:
                    self.ySpeed = self.deltaY
                    self.isMoving = False

        else: # if the baby obstacle is initially falling
            if self.bufferLevel == 0:
                self.ySpeed += self.gravity
                self.bufferLevel += 1
            elif self.isLegalFall():
                self.ySpeed += self.gravity
            else:
                self.ySpeed = self.deltaY
                self.isMoving = False


    def update(self, screenWidth, screenHeight):
        if self.isMoving == True:
            self.move()
        else: # if fell on grass, stop moving
            self.xSpeed = 0
            self.ySpeed = 0

        self.deltaY = 0
        super(BabyObstacle, self).update(screenWidth, screenHeight)


class LeftBar(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("leftBar.png").convert()
        LeftBar.barImage = pygame.transform.scale(image, (10, 40))

    def __init__(self, x, y):
        super(LeftBar, self).__init__(x, y, LeftBar.barImage, 5)
        self.xSpeed = -40
        self.move = False


class RightBar(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("rightBar.png").convert()
        RightBar.barImage = pygame.transform.scale(image, (10, 40))

    def __init__(self, x, y):
        super(RightBar, self).__init__(x, y, RightBar.barImage, 5)
        self.xSpeed = 40
        self.move = False


class Zombie(GameObject):
    @staticmethod
    def init():
        image0 = pygame.image.load("zombie0.png").convert_alpha()
        Zombie.image0 = pygame.transform.scale(image0, (20, 2))
        image1 = pygame.image.load("zombie1.png").convert_alpha()
        Zombie.image1 = pygame.transform.scale(image1, (20, 8))
        image2 = pygame.image.load("zombie2.png").convert_alpha()
        Zombie.image2 = pygame.transform.scale(image2, (20, 24))
        image3 = pygame.image.load("zombie3.png").convert_alpha()
        Zombie.image3 = pygame.transform.scale(image3, (20, 36))

    def flipImage(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def __init__(self, x, y):
        super(Zombie, self).__init__(x, y, Zombie.image1, 10)
        self.status = 0
        self.direction = random.choice([-1, 1])
        self.xSpeed = self.direction * random.randint(1, 2)
        self.xMin = 140
        self.xMax = 550
        self.activated = False
        # print(self.xSpeed, self.direction)

    def upgrade(self):
        if self.status == 0:
            self.y -= 2
            self.image = Zombie.image0
        elif self.status == 1:
            self.y -= 8
            self.image = Zombie.image1
        elif self.status == 2:
            self.y -= 4
            self.image = Zombie.image2
        elif self.status == 3:
            self.y -= 6
            self.image = Zombie.image3
            if self.direction == -1:
                self.flipImage()
        self.status += 1
        # print(self.xSpeed)

    def update(self, screenWidth, screenHeight):
        if self.x <= self.xMin or self.x >= self.xMax:
            self.direction = 0 - self.direction
            self.xSpeed = 0 - self.xSpeed
            self.flipImage()
        # print(self.xSpeed, self.direction)
        super(Zombie, self).update(screenWidth, screenHeight)


class Collision(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("die.png").convert_alpha()
        Collision.collisionImage = pygame.transform.scale(image, (40, 50))

    def __init__(self, x, y):
        super(Collision, self).__init__(x, y, Collision.collisionImage, 20)


class EnemyCollision(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("collision.png").convert_alpha()
        EnemyCollision.image = pygame.transform.scale(image, (10, 10))

    def __init__(self, x, y):
        super(EnemyCollision, self).__init__(x, y, EnemyCollision.image, 5)


class Bullet(GameObject):
    speed = 10
    size = 5

    def __init__(self, x, y, direction):
        size = Bullet.size
        image = pygame.Surface((Bullet.size, Bullet.size), pygame.SRCALPHA)
        pygame.draw.circle(image, (0, 0, 0), (size//2, size//2), size//2)
        super(Bullet, self).__init__(x, y, image, size//2)
        self.direction = direction
        self.xSpeed = Bullet.speed

    def update(self, screenWidth, screenHeight):
        self.xSpeed = Bullet.speed * self.direction
        super(Bullet, self).update(screenWidth, screenHeight)


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()

IWANNA = Game(600, 400)
IWANNA.run()