import pygame
import random
import math

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
    def init(self, stage=5, saved=False):
        self.stage = stage

        self.blockSize = 20
        self.hitWall = False

        self.heroX = 300
        self.heroY = 200

        self.gameOver = False

        self.temp = False

        self.bossBullet = True
        self.bossTime = 0

        self.saved = saved # if any save points were reached

        Background.init()
        Background2.init()
        self.backgrounds = pygame.sprite.Group()

        Bar.init()
        Bar2.init()
        self.bars = pygame.sprite.Group()

        Column.init()
        Column2.init()
        self.columns = pygame.sprite.Group()

        Block.init()
        Block2.init()
        self.blocks = pygame.sprite.Group()

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

        ThornUp.init()
        self.thornUps = pygame.sprite.Group()

        ThornDown.init()
        self.thornDowns = pygame.sprite.Group()

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

        LongUp.init()
        self.longUps = pygame.sprite.Group()

        LongDown.init()
        self.longDowns = pygame.sprite.Group()

        SuperObstacle.init()
        self.superObstacles = pygame.sprite.Group()

        BabyObstacle.init()
        self.babyObstacles = pygame.sprite.Group()

        Tree.init()
        self.trees = pygame.sprite.Group()

        Apple.init()
        self.apples = pygame.sprite.Group()
        self.fallingApples = pygame.sprite.Group()
        self.movingApples = pygame.sprite.Group()

        Plank.init()
        self.planks = pygame.sprite.Group()
        self.elevators = pygame.sprite.Group()
        # elevators are planks that move vertically

        Save.init()
        self.saveGroup = pygame.sprite.GroupSingle()
        # there would/can only be one save point on one map

        GreenSave.init()
        self.greenSaveGroup = pygame.sprite.GroupSingle()

        Button.init()
        self.buttons = pygame.sprite.Group()

        FakeTile.init()
        self.fakeTiles = pygame.sprite.Group()
        self.randomFakeTiles = pygame.sprite.Group()

        FakeGrass.init()
        self.fakeGrasses = pygame.sprite.Group()

        GiantObstacle.init()
        self.giantObstacles = pygame.sprite.Group()

        Zombie.init()
        self.zombies = pygame.sprite.Group()

        self.bullets = pygame.sprite.Group()

        Collision.init()
        self.collisions = pygame.sprite.Group()

        EnemyCollision.init()
        self.enemyCollisions = pygame.sprite.Group()

        Guy.init()
        self.guyGroup = pygame.sprite.GroupSingle()

        GuySign.init()
        self.guySigns = pygame.sprite.Group()

        GuyHealthGreen.init()
        self.guyHealthGreens = pygame.sprite.Group()

        GuyHealthRed.init()
        self.guyHealthReds = pygame.sprite.Group()

        GuyBullet.init()
        self.guyBullets = pygame.sprite.Group()

        Portal.init()
        self.portalGroup = pygame.sprite.GroupSingle()

        BlackFrame.init()
        self.blackFrameGroup = pygame.sprite.GroupSingle()

        Frame.init()
        self.frameGroup = pygame.sprite.GroupSingle()

        BossBg.init()
        self.bossBgGroup = pygame.sprite.GroupSingle()

        BgBox.init()
        self.bgBoxes = pygame.sprite.Group()

        Boss.init()
        self.bossGroup = pygame.sprite.GroupSingle()

        Box.init()
        self.boxes = pygame.sprite.Group()
        self.bouncingBoxes = pygame.sprite.Group()
        self.circleBoxes = pygame.sprite.Group()
        self.tracingBoxes = pygame.sprite.Group()
        self.xBoxes = pygame.sprite.Group()
        self.groupBoxes = pygame.sprite.Group()

        if self.stage == 5:
            self.initBoss0()

        self.key = True
        

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
        for j in range(5, 7):
            x = self.getX(4)
            y = self.getY(j)
            self.leftObstacles.add(LeftObstacle(x, y))

        for j in range(15, 17):
            x = self.getX(4)
            y = self.getY(j)
            self.leftObstacles.add(LeftObstacle(x, y))

        # init right obstacles on map
        for j in range(10, 12):
            x = self.getX(25)
            y = self.getY(j)
            self.rightObstacles.add(RightObstacle(x, y))

        # init left bars on map
        self.leftBars.add(LeftBar(600, 140))

        # init right bars on map
        self.rightBars.add(RightBar(0, 240))

        # init rising obstacles on map
        for i in range(4, 27, 6):
            x = self.getX(i)
            y = self.getY(2)
            self.risingObstacles.add(RisingObstacle(x, y))

        # init falling obstacle on map
        self.fallingObstacles.add(FallingObstacle(self.getX(19), self.getY(14)))

        # init super obstacle on map
        self.superObstacles.add(SuperObstacle(self.getX(16), self.getY(12)))

        # init zombies on map
        for n in range(5):
            x = random.randint(150, 550)
            y = 264
            self.zombies.add(Zombie(x, y, 140, 550))

        # init button on map
        self.button = Button(self.getX(28)+5, self.getY(3), False)
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
        self.tiles.add(Tile(self.getX(25), self.getY(15)))

        # init grass on map
        for i in range(5, 24):
            x = self.getX(i)
            y = self.getY(0) - self.blockSize/2
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(4), self.getY(3)))
        for i in range(4):
            x = self.getX(i)
            y = self.getY(6)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(24), self.getY(2)))
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
        self.grasses.add(Grass(self.getX(25), self.getY(16)))
        for i in range(26, 30):
            x = self.getX(i)
            y = self.getY(16)
            self.grasses.add(Grass(x, y))

        # init obstacles on map
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

        # init long upward obstacles on map
        for i in range(9, 22, 6):
            x = self.getX(i)
            y = self.getY(1)
            self.longUps.add(LongUp(x, y))

        # init long downward obstacles on map
        for i in range(12, 20, 6):
            x = self.getX(i)
            y = self.getY(2) - 10
            self.longDowns.add(LongDown(x, y))

        # init flipped obstacles on map
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

        # init trees on map
        x = self.getX(17)
        y = self.getY(10) + 10
        self.trees.add(Tree(x, y))

        # init apples on map
        x = self.getX(16)
        y = self.getY(11)
        self.apples.add(Apple(x, y))

        x = self.getX(17)
        y = self.getY(11)
        self.apples.add(Apple(x, y))

        # x = self.getX(18)
        # y = self.getY(11)
        # self.movingApples.add(MovingApple(x, y))

        # init saving points on map
        self.save = Save(self.getX(24), self.getY(3))
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


    def initStage3(self):
        self.bgColor = (255, 255, 255)
        # init tiles
        for j in range(6):
            for i in range(2):
                x = self.getX(i)
                y = self.getY(j)
                self.tiles.add(Tile(x, y))
        self.tiles.add(Tile(self.getX(2), self.getY(2)))
        self.tiles.add(Tile(self.getX(3), self.getY(2)))
        for i in range(27, 30):
            for j in range(9):
                x = self.getX(i)
                y = self.getY(j)
                self.tiles.add(Tile(x, y))   
        for i in range(7, 20):
            x = self.getX(i)
            y = self.getY(1)
            self.tiles.add(Tile(x, y))
        self.tiles.add(Tile(self.getX(8), self.getY(2)))
        self.tiles.add(Tile(self.getX(18), self.getY(2)))
        self.tiles.add(Tile(self.getX(8), self.getY(9)))
        self.tiles.add(Tile(self.getX(20), self.getY(9)))
        self.tiles.add(Tile(self.getX(18), self.getY(8)))

        # init grasses
        for i in range(2):
            x = self.getX(i)
            y = self.getY(6)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(2), self.getY(3)))
        self.grasses.add(Grass(self.getX(3), self.getY(3)))
        self.grasses.add(Grass(self.getX(4), self.getY(2)))
        self.grasses.add(Grass(self.getX(26), self.getY(0)))
        for i in range(27, 30):
            x = self.getX(i)
            y = self.getY(9)
            self.grasses.add(Grass(x, y))
        for i in range(22, 24):
            x = self.getX(i)
            y = self.getY(1)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(8), self.getY(3)))
        self.grasses.add(Grass(self.getX(18), self.getY(3)))
        self.grasses.add(Grass(self.getX(7), self.getY(9)))
        for i in range(9, 20):
            x = self.getX(i)
            y = self.getY(9)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(8), self.getY(10)))
        self.grasses.add(Grass(self.getX(20), self.getY(10)))

        # init obtacles
        self.obstacles.add(Obstacle(self.getX(7), self.getY(2)))
        self.obstacles.add(Obstacle(self.getX(8), self.getY(4)))
        for i in range(10, 18):
            x = self.getX(i)
            y = self.getY(2)
            self.obstacles.add(Obstacle(x, y))
        self.obstacles.add(Obstacle(self.getX(18), self.getY(4)))
        self.obstacles.add(Obstacle(self.getX(19), self.getY(2)))

        # init flipped obstacles
        for i in range(7, 11):
            x = self.getX(i)
            y = self.getY(8)
            self.flippedObstacles.add(FlippedObstacle(x, y))
        for i in range(12, 17):
            x = self.getX(i)
            y = self.getY(8)
            self.flippedObstacles.add(FlippedObstacle(x, y))
        for i in range(19, 21):
            x = self.getX(i)
            y = self.getY(8)
            self.flippedObstacles.add(FlippedObstacle(x, y))
        self.flippedObstacles.add(FlippedObstacle(self.getX(18), self.getY(7)))

        # init upward thorns
        for i in range(3, 26, 2):
            x = self.getX(i)-10
            y = self.getY(0)+5
            self.thornUps.add(ThornUp(x, y))

        # init rising obstacles
        self.risingObstacles.add(RisingObstacle(self.getX(9), self.getY(2), -10))

        # init falling obstacles
        self.fallingObstacles.add(FallingObstacle(self.getX(11), self.getY(8), 10))
        self.fallingObstacles.add(FallingObstacle(self.getX(17), self.getY(8), 10))

        # init zombies
        for n in range(5):
            x = random.randint(self.getX(11), self.getX(17))
            y = 204
            self.zombies.add(Zombie(x, y, self.getX(10)+10, self.getX(18)-10))

        # init trees
        self.trees.add(Tree(self.getX(0), self.getY(10) + 10))
        self.trees.add(Tree(self.getX(3)-10, self.getY(7) + 10))
        self.trees.add(Tree(self.getX(8)+10, self.getY(13) + 20))
        self.trees.add(Tree(self.getX(11)+10, self.getY(13) + 10))
        self.trees.add(Tree(self.getX(15)+10, self.getY(13) + 10))
        self.trees.add(Tree(self.getX(18)+10, self.getY(13) + 10))

        # init apples
        self.apple_10 = FallingApple(165, 115)
        self.fallingApples.add(self.apple_10)
        self.apple_04 = FallingApple(190, 115)
        self.fallingApples.add(self.apple_04)
        self.apple_03 = FallingApple(190, 140)
        self.fallingApples.add(self.apple_03)
        self.apple_11 = FallingApple(225, 110)
        self.fallingApples.add(self.apple_11)
        self.apple_12 = FallingApple(235, 140)
        self.fallingApples.add(self.apple_12)
        self.apple_02 = FallingApple(260, 120)
        self.fallingApples.add(self.apple_02)
        self.apple_13 = FallingApple(290, 140)
        self.fallingApples.add(self.apple_13)
        self.apple_01 = FallingApple(325, 140)
        self.fallingApples.add(self.apple_01)
        self.apple_00 = FallingApple(310, 115)
        self.fallingApples.add(self.apple_00)
        self.apple_14 = FallingApple(360, 120)
        self.fallingApples.add(self.apple_14)
        self.apple_20 = MovingApple(405, 120)
        self.movingApples.add(self.apple_20)
        self.apple_21 = MovingApple(385, 100)
        self.movingApples.add(self.apple_21)
        self.apple_22 = MovingApple(375, 140)
        self.movingApples.add(self.apple_22)

        # init save points
        self.save = Save(self.getX(22), self.getY(3))
        self.saveGroup.add(self.save)

        # init planks
        self.plank = Plank(self.getX(9), self.getY(3)-10, 
            self.getX(9)+5, self.getX(17)-5)
        self.planks.add(self.plank)


    def initStage4(self):
        # init tiles
        for i in range(13):
            for j in range(5):
                x = self.getX(i)
                y = self.getY(j)
                self.tiles.add(Tile(x, y))
        for i in range(18, 30):
            x = self.getX(i)
            y = self.getY(3)
            self.tiles.add(Tile(x, y))
        for i in range(17, 30):
            x = self.getX(i)
            y = self.getY(4)
            self.tiles.add(Tile(x, y))
        for j in range(5, 16):
            x = self.getX(0)
            y = self.getY(j)
            self.tiles.add(Tile(x, y))
        for j in range(5, 20):
            x = self.getX(29)
            y = self.getY(j)
            self.tiles.add(Tile(x, y))
        for i in range(29):
            x = self.getX(i)
            y = self.getY(19)
            self.tiles.add(Tile(x, y))

        # init grasses
        for i in range(17, 30):
            x = self.getX(i)
            y = self.getY(0)
            self.grasses.add(Grass(x, y))
        self.grasses.add(Grass(self.getX(0), self.getY(16)))
        self.grasses.add(Grass(self.getX(13), self.getY(1)))
        self.grasses.add(Grass(self.getX(14), self.getY(1)))

        # init fake grasses
        step = -33
        for i in range(1, 13):
            x = self.getX(i)
            y = self.getY(5)
            step += 3
            self.fakeGrasses.add(FakeGrass(x, y, step)) # -1 for left
        step = 0
        for i in range(17, 29):
            x = self.getX(i)
            y = self.getY(5)
            step -= 3
            self.fakeGrasses.add(FakeGrass(x, y, step)) # 1 for right

        # init fake tiles
        for i in range(13, 17):
            for j in range(6):
                x = self.getX(i)
                y = self.getY(j)
                self.randomFakeTiles.add(RandomFakeTile(x, y))
        for i in range(17, 30):
            for j in range(4):
                x = self.getX(i)
                y = self.getY(j)
                self.fakeTiles.add(FakeTile(x, y))

        # init obstacles
        for i in range(13, 17):
            x = self.getX(i)
            y = self.getY(0)
            self.obstacles.add(Obstacle(x, y))

        # init button
        self.button = Button(self.getX(28)+5, self.getY(6), False)
        self.buttons.add(self.button)

        # init save point
        self.save = Save(self.getX(0), self.getY(17))
        self.saveGroup.add(self.save)

        # init giant obstacle
        self.giantObstacle = GiantObstacle(300, 240)
        self.giantObstacles.add(self.giantObstacle)


    def initBoss0(self):
        self.bgColor = (76, 11, 2)
        
        self.guy = Guy(520, 340)
        self.guyGroup.add(self.guy)

        # init tiles
        for j in range(5):
            x = self.getX(0)
            y = self.getY(j)
            self.tiles.add(Tile(x, y))
        for j in range(5):
            x = self.getX(29)
            y = self.getY(j)
            self.tiles.add(Tile(x, y))

        # init grasses
        self.grasses.add(Grass(self.getX(0), self.getY(5)))
        self.grasses.add(Grass(self.getX(29), self.getY(5)))
        for i in range(1, 29):
            x = self.getX(i)
            y = self.getY(0)
            self.grasses.add(Grass(x, y))

        # init obstacles
        self.obstacles.add(Obstacle(self.getX(0), self.getY(6)))
        self.obstacles.add(Obstacle(self.getX(29), self.getY(6)))

        # init right obstacles
        for j in range(1, 6):
            x = self.getX(1)
            y = self.getY(j)
            self.rightObstacles.add(RightObstacle(x, y))

        # init guy sign
        self.guySigns.add(GuySign(140, 50))

        # init guy health bars
        self.guyHealthGreen = GuyHealthGreen(300, 100)
        self.guyHealthGreens.add(self.guyHealthGreen)
        self.guyHealthRed = GuyHealthRed(550, 100)
        self.guyHealthReds.add(self.guyHealthRed)

        # init portal
        self.portal = Portal(540, 370)
        self.portalGroup.add(self.portal)


    def initStage6(self):
        self.bgColor = (255, 255, 255)
        # init background
        for i in range(30):
            for j in range(20):
                x = self.getX(i)
                y = self.getY(j)
                self.backgrounds.add(Background(x, y))

        # init bars
        for i in range(1, 29):
            x = self.getX(i)
            y = self.getY(0)
            self.bars.add(Bar(x, y))
        for i in range(1, 29):
            x = self.getX(i)
            y = self.getY(19)
            self.bars.add(Bar(x, y))

        # init columns
        for j in range(1, 9):
            x = self.getX(0)
            y = self.getY(j)
            self.columns.add(Column(x, y))
        for j in range(13, 19):
            x = self.getX(0)
            y = self.getY(j)
            self.columns.add(Column(x, y))
        for j in range(1, 8):
            x = self.getX(29)
            y = self.getY(j)
            self.columns.add(Column(x, y))
        for j in range(12, 19):
            x = self.getX(29)
            y = self.getY(j)
            self.columns.add(Column(x, y))

        # init blocks
        self.blocks.add(Block(self.getX(0), self.getY(9)))
        self.blocks.add(Block(self.getX(0), self.getY(12)))
        self.blocks.add(Block(self.getX(0), self.getY(0)))
        self.blocks.add(Block(self.getX(29), self.getY(0)))
        self.blocks.add(Block(self.getX(0), self.getY(19)))
        self.blocks.add(Block(self.getX(29), self.getY(19)))
        self.blocks.add(Block(self.getX(29), self.getY(11)))
        self.blocks.add(Block(self.getX(29), self.getY(8)))

        # init obstacle
        for i in range(1, 29):
            x = self.getX(i)
            y = self.getY(1)
            self.obstacles.add(Obstacle(x, y))

        # init left obstacles
        for j in range(2, 8):
            x = self.getX(28)
            y = self.getY(j)
            self.leftObstacles.add(LeftObstacle(x, y))
        for j in range(12, 18):
            x = self.getX(28)
            y = self.getY(j)
            self.leftObstacles.add(LeftObstacle(x, y))

        # init right obstacles
        for j in range(2, 10):
            x = self.getX(1)
            y = self.getY(j)
            self.rightObstacles.add(RightObstacle(x, y))
        for j in range(12, 18):
            x = self.getX(1)
            y = self.getY(j)
            self.rightObstacles.add(RightObstacle(x, y))

        # init flipped obstacles
        for i in range(1, 29):
            x = self.getX(i)
            y = self.getY(18)
            self.flippedObstacles.add(FlippedObstacle(x, y))

        # init planks
        self.planks.add(Plank(35, 205, 35, 65))

        # init elevators
        self.xStart = 65
        self.elevator1 = self.getNextElevator(1)
        self.elevators.add(self.elevator1)
        self.elevator2 = self.getNextElevator(2)
        self.elevators.add(self.elevator2)
        self.elevator3 = self.getNextElevator(3)
        self.elevators.add(self.elevator3)
        self.elevator4 = self.getNextElevator(4)
        self.elevators.add(self.elevator4)

        # init save
        self.save = Save(10, 180)
        self.saveGroup.add(self.save)

    def getNextElevator(self, index):
        self.xStart += 105
        bound1 = random.randint(100, 350)
        bound2 = random.randint(100, 350)
        y = random.randint(100, 350)
        lowerBound = min(bound1, bound2)
        upperBound = max(bound1, bound2)
        legal1 = False # check whether the y is within bound
        legal2 = False # check whether the new elevator is reachable
        while not legal1:
            if self.isLegalElevator(lowerBound, upperBound, y):
                legal1 = True
            else:
                # y = random.randint(100, 350)
                self.xStart -= 105
                return self.getNextElevator(index)
        while not legal2:
            if self.isReachableElevator(lowerBound, upperBound, y, index):
                legal2 = True
            else:
                self.xStart -= 105 # undo the add xStart
                return self.getNextElevator(index)
        return Elevator(self.xStart, y, lowerBound, upperBound, index)


    def isLegalElevator(self, lower, upper, y):
        if lower <= y and upper >= y and lower + 100 < upper:
            return True
        else:
            return False

    def isReachableElevator(self, lower, upper, y, index):
        time = 55 / self.hero.maxSpeed # 11
        maxHeight = 3 + 5 + 4.5 + 4 + 3.5 + 3 + 2.5 + 2 + 1.5 + 1 + 0.5 # 30.5
        if index == 1:
            if upper >= 200 - maxHeight:
                return True
        for elevator in self.elevators:
            if elevator.index == index - 1:
                if elevator.yMin < upper:
                    return True
                elif elevator.yMin - upper < maxHeight:
                    return True
        return False


    def initBossFinal(self):
        self.bgColor = (0, 0, 0)

        self.blackFrame = BlackFrame(300, 200)
        self.blackFrameGroup.add(self.blackFrame)

        self.frame = Frame(300, 200)
        self.frameGroup.add(self.frame)

        self.bossBg = BossBg(300, 200)
        self.bossBgGroup.add(self.bossBg)



    def initFinal(self):
        for i in range(30):
            for j in range(20):
                x = self.getX(i)
                y = self.getY(j)
                self.backgrounds.add(Background2(x, y))

        # init bars
        for i in range(1, 29):
            x = self.getX(i)
            y = self.getY(0)
            self.bars.add(Bar2(x, y))
        for i in range(1, 29):
            x = self.getX(i)
            y = self.getY(19)
            self.bars.add(Bar2(x, y))

        # init columns
        for j in range(1, 19):
            x = self.getX(0)
            y = self.getY(j)
            self.columns.add(Column2(x, y))
        for j in range(1, 19):
            x = self.getX(29)
            y = self.getY(j)
            self.columns.add(Column2(x, y))

        # init blocks
        self.blocks.add(Block2(self.getX(0), self.getY(0)))
        self.blocks.add(Block2(self.getX(29), self.getY(0)))
        self.blocks.add(Block2(self.getX(0), self.getY(19)))
        self.blocks.add(Block2(self.getX(29), self.getY(19)))
        
        # write THANK YOU
        for i in range(2, 6):
            x = self.getX(i)
            y = self.getY(16)
            self.blocks.add(Block2(x, y))
        for j in range(12, 16):
            x = self.getX(4)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))

        for j in range(12, 17):
            x = self.getX(7)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))
        for j in range(12, 17):
            x = self.getX(10)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))
        for i in range(8, 10):
            x = self.getX(i)
            y = self.getY(14)
            self.blocks.add(Block2(x, y))

        for i in range(12, 16):
            x = self.getX(i)
            y = self.getY(13)
            self.blocks.add(Block2(x, y))
        self.blocks.add(Block2(self.getX(12), self.getY(12)))
        self.blocks.add(Block2(self.getX(13), self.getY(14)))
        self.blocks.add(Block2(self.getX(13), self.getY(15)))
        self.blocks.add(Block2(self.getX(15), self.getY(14)))
        self.blocks.add(Block2(self.getX(15), self.getY(15)))
        self.blocks.add(Block2(self.getX(14), self.getY(16)))
        self.blocks.add(Block2(self.getX(16), self.getY(12)))

        for j in range(12, 17):
            x = self.getX(18)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))
        for j in range(12, 17):
            x = self.getX(22)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))
        self.blocks.add(Block2(self.getX(19), self.getY(15)))
        self.blocks.add(Block2(self.getX(20), self.getY(14)))
        self.blocks.add(Block2(self.getX(21), self.getY(13)))

        for j in range(12, 17):
            x = self.getX(24)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))
        self.blocks.add(Block2(self.getX(25), self.getY(14)))
        self.blocks.add(Block2(self.getX(26), self.getY(13)))
        self.blocks.add(Block2(self.getX(26), self.getY(15)))
        self.blocks.add(Block2(self.getX(27), self.getY(16)))
        self.blocks.add(Block2(self.getX(27), self.getY(12)))

        # init YOU
        self.blocks.add(Block2(self.getX(4), self.getY(9)))
        self.blocks.add(Block2(self.getX(5), self.getY(8)))
        self.blocks.add(Block2(self.getX(7), self.getY(8)))
        self.blocks.add(Block2(self.getX(8), self.getY(9)))
        for j in range(5, 8):
            x = self.getX(6)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))

        for i in range(10, 14):
            x = self.getX(i)
            y = self.getY(9)
            self.blocks.add(Block2(x, y))
        for i in range(10, 14):
            x = self.getX(i)
            y = self.getY(5)
            self.blocks.add(Block2(x, y))
        for j in range(6, 9):
            x = self.getX(10)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))
        for j in range(6, 9):
            x = self.getX(13)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))

        for i in range(15, 19):
            x = self.getX(i)
            y = self.getY(5)
            self.blocks.add(Block2(x, y))
        for j in range(6, 10):
            x = self.getX(15)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))
        for j in range(6, 10):
            x = self.getX(18)
            y = self.getY(j)
            self.blocks.add(Block2(x, y))

        self.blocks.add(Block2(self.getX(20), self.getY(8)))
        self.blocks.add(Block2(self.getX(20), self.getY(7)))
        self.blocks.add(Block2(self.getX(21), self.getY(9)))
        self.blocks.add(Block2(self.getX(21), self.getY(6)))
        self.blocks.add(Block2(self.getX(22), self.getY(8)))
        self.blocks.add(Block2(self.getX(22), self.getY(5)))
        self.blocks.add(Block2(self.getX(23), self.getY(9)))
        self.blocks.add(Block2(self.getX(23), self.getY(6)))
        self.blocks.add(Block2(self.getX(24), self.getY(8)))
        self.blocks.add(Block2(self.getX(24), self.getY(7)))



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
        if self.saved == True and self.stage == self.greenSave.stage:
            # if there is already a saving point on the same stage
            self.hero = Hero(self.heroX, self.heroY)
            self.heroGroup = pygame.sprite.GroupSingle(self.hero)
            self.resetMovingObstacles()
            # print(self.temp)
            if self.stage == 0:
                self.initStage0()
            elif self.stage == 1:
                self.initStage1()
            elif self.stage == 2:
                self.initStage2()
            elif self.stage == 3:
                self.initStage3()
            elif self.stage == 4:
                self.initStage4()
            elif self.stage == 5:
                self.initBoss0()
            elif self.stage == 6:
                self.initStage6()
            elif self.stage == 7:
                self.initBossFinal()
            if self.temp == True:
                self.reactivateButton()
        elif self.saved == True and self.stage != self.greenSave.stage:
            # if there has been a saving point but not on the stage
            self.stage = self.greenSave.stage
            self.init(self.stage, self.saved)
            self.hero = Hero(self.greenSave.x, self.greenSave.y)
            self.heroGroup = pygame.sprite.GroupSingle(self.hero)
            self.resetMovingObstacles()
            if self.stage == 0:
                self.initStage0()
            elif self.stage == 1:
                self.initStage1()
            elif self.stage == 2:
                self.initStage2()
            elif self.stage == 3:
                self.initStage3()
            elif self.stage == 4:
                self.initStage4()
            elif self.stage == 5:
                self.initBoss0()
            elif self.stage == 6:
                self.initStage6()
            elif self.stage == 7:
                self.initBossFinal()
            if self.temp == True:
                self.reactivateButton()
        else: # if the game has not yet been saved
            self.hero = Hero(self.heroX, self.heroY)
            self.heroGroup = pygame.sprite.GroupSingle(self.hero)
            self.resetMovingObstacles()
            if self.stage == 0:
                self.initStage0()
            elif self.stage == 1:
                self.initStage1()
            elif self.stage == 2:
                self.initStage2()
            elif self.stage == 3:
                self.initStage3()
            elif self.stage == 4:
                self.initStage4()
            elif self.stage == 5:
                self.initBoss0()
            elif self.stage == 6:
                self.initStage6()
            elif self.stage == 7:
                self.initBossFinal()

    def reactivateButton(self):
        x = self.button.x + 5
        y = self.button.y
        self.button.kill()
        self.button = Button(x, y, True)
        self.buttons.add(self.button)
        self.buttons.update(self.width, self.height)

    def resetMovingObstacles(self):
        self.bullets.empty()
        self.collisions.empty()
        self.zombies.empty()
        self.risingObstacles.empty()
        self.fallingObstacles.empty()
        self.leftBars.empty()
        self.rightBars.empty()
        self.superObstacles.empty()
        self.babyObstacles.empty() # clear all activated babies
        self.buttons.empty()
        self.fallingApples.empty()
        self.movingApples.empty()
        self.zoomingObstacles.empty()
        self.longUps.empty()
        self.longDowns.empty()
        self.planks.empty()
        self.elevators.empty()
        self.fakeTiles.empty()
        self.fakeGrasses.empty()
        self.randomFakeTiles.empty()
        self.giantObstacles.empty()
        self.guyBullets.empty()
        self.guyHealthGreens.empty()
        self.guyHealthReds.empty()
        self.bgBoxes.empty()
        self.bossGroup.empty()
        self.bouncingBoxes.empty()
        self.xBoxes.empty()
        self.groupBoxes.empty()
        self.tracingBoxes.empty()
        self.circleBoxes.empty()


    def touchObstacle(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        # print(heroX, heroY, heroW, heroH)
        for obstacle in self.obstacles:
            # print(obstacle.x, obstacle.y)
            if (abs(heroX - obstacle.x) < (heroW/2 + obstacle.blockSize/2) 
                and abs(heroY - obstacle.y) < (heroH/2 + obstacle.blockSize/2)
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
            if (abs(heroX - flipped.x) < (heroW/2 + flipped.blockSize/2) 
                and abs(heroY - flipped.y) < (heroH/2 + flipped.blockSize/2)
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
            if (abs(heroX - left.x) < (heroW/2 + left.blockSize/2) 
                and abs(heroY - left.y) < (heroH/2 + left.blockSize/2)
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
            if (abs(heroX - right.x) < (heroW/2 + right.blockSize/2) 
                and abs(heroY - right.y) < (heroH/2 + right.blockSize/2)
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

    def touchLongUp(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        for longUp in self.longUps:
            if (heroY > longUp.y - heroH/2 and 
                heroY < longUp.y + heroH/2 + longUp.height/2):
                if (abs(heroX - longUp.x) < heroW/2 + longUp.width/2):
                    return True
            elif (heroY < longUp.y - heroH/2 and
                heroY > longUp.y - heroH/2 - longUp.height/2):
                if (abs(heroX - longUp.x) < heroW/2 + 
                    (heroY + heroH/2 - (longUp.y - longUp.height/2))/2):
                    return True
        return False

    def touchLongDown(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        for longDown in self.longDowns:
            if (heroY > longDown.y - longDown.height/2 - heroH/2 and 
                heroY < longDown.y + heroH/2):
                if (abs(heroX - longDown.x) < heroW/2 + longDown.width/2):
                    return True
            elif (heroY > longDown.y + heroH/2 and
                heroY < longDown.y + heroH/2 + longDown.height/2):
                if (abs(heroX - longDown.x) < heroW/2 + 
                    (longDown.y + longDown.height/2 - (heroY - heroH/2))/2):
                    return True
        return False

    def touchGiantObstacle(self):
        heroX = self.hero.x
        heroY = self.hero.y
        heroW = self.hero.width
        heroH = self.hero.height
        for giant in self.giantObstacles:
            if (abs(heroX - giant.x) < (heroW/2 + giant.width/2) 
                and abs(heroY - giant.y) < (heroH/2 + giant.height/2)
                and (abs(heroX - giant.x) < heroW/2 + 
                    (heroY + heroH/2 - (giant.y - giant.height/2))/2)):
                return True
        return False

    def touchReversedGiantObstacle(self, block):
        for reverse in self.giantObstacles:
            if (abs(block.x - reverse.x) < (block.width/2 + reverse.width/2) 
                and abs(block.y - reverse.y) < (block.height/2 + reverse.height/2)
                and (abs(block.x - reverse.x) < block.width/2 + 
                    (reverse.y + reverse.height/2 - (block.y - block.height/2))/2)):
                return True
        return False


    def timerFired(self, dt):
        if self.gameOver == False or self.key == True:
            self.heroGroup.update(self.isKeyPressed, self.width, self.height)
            hero = self.heroGroup.sprite

            self.zombies.update(self.width, self.height)

            self.bullets.update(self.width, self.height)

            self.longUps.update(self.width, self.height)
            self.longDowns.update(self.width, self.height)
            self.zoomingObstacles.update(self.width, self.height)

            self.superObstacles.update(self.width, self.height)
            self.babyObstacles.update(self.width, self.height)

            self.fakeTiles.update(self.width, self.height)
            self.fakeGrasses.update(self.width, self.height)
            self.randomFakeTiles.update(self.width, self.height)

            self.giantObstacles.update(self.width, self.height)

            self.planks.update(self.width, self.height)
            self.elevators.update(self.width, self.height)

            # update the pic and position of apples that would move
            self.movingApples.update(self.width, self.height)
            self.fallingApples.update(self.width, self.height)

            if self.stage == 0:
                self.timerFired0(dt)
            elif self.stage == 3:
                self.timerFired3(dt)
            elif self.stage == 4:
                self.timerFired4(dt)
            elif self.stage == 5:
                self.timerFired5(dt)
            elif self.stage == 7:
                self.timerFired7(dt)

            # if player hits nextStage, then next stage
            if self.hero.x + self.hero.width/2 >= 590:
                self.stage += 1
                self.temp = False
                if self.stage == 1:
                    self.init(self.stage, self.saved)
                    self.hero = Hero(30, 250)
                    self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                    self.initStage1()
                elif self.stage == 2:
                    self.init(self.stage, self.saved)
                    self.hero = Hero(20, 150)
                    self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                    self.initStage2()
                elif self.stage == 3:
                    self.init(self.stage, self.saved)
                    self.hero = Hero(530, 370)
                    self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                    self.initStage3()
                elif self.stage == 4:
                    self.init(self.stage, self.saved)
                    self.hero = Hero(10, 70)
                    self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                    self.initStage4()
                elif self.stage == 5:
                    self.init(self.stage, self.saved)
                    self.hero = Hero(60, 370)
                    self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                    self.initBoss0()
                elif self.stage == 6:
                    self.init(self.stage, self.saved)
                    self.hero = Hero(35, 190)
                    self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                    self.initStage6()
                else:
                    self.init(self.stage, self.saved)
                    self.hero = Hero(70, 50)
                    self.heroGroup = pygame.sprite.GroupSingle(self.hero)
                    self.initBossFinal()

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

            elif self.touchLongUp():
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            elif self.touchLongDown():
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            elif self.touchGiantObstacle():
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

            # if player touches a thorn, game over
            if pygame.sprite.groupcollide(self.heroGroup, self.thornUps, 
                False, False, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            if pygame.sprite.groupcollide(self.heroGroup, self.thornDowns, 
                False, False, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            # if player touches an apple, game over
            if pygame.sprite.groupcollide(self.heroGroup, self.apples, 
                False, True, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            if pygame.sprite.groupcollide(self.heroGroup, self.movingApples, 
                False, True, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            if pygame.sprite.groupcollide(self.heroGroup, self.fallingApples, 
                False, True, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            # if player hits save, then save (green save)
            if pygame.sprite.groupcollide(self.heroGroup, self.saveGroup, 
                False, True, pygame.sprite.collide_circle):
                self.saved = True
                self.heroX = self.save.x
                self.heroY = self.save.y
                self.greenSave = GreenSave(self.heroX, self.heroY,
                    self.save.stage)
                self.greenSaveGroup.add(self.greenSave)

            # if player hits button, then activate
            
            if pygame.sprite.groupcollide(self.heroGroup, self.buttons,
                False, False, pygame.sprite.collide_circle):
                if self.button.activated == False:
                    self.button.kill()
                    x = self.button.x + 3
                    y = self.button.y
                    self.button = Button(x, y, True)
                    self.buttons.add(self.button)
                    self.buttons.update(self.width, self.height)
                    # print("activate button")
                    self.temp = True

            # if enemy collides with bullet, enemy dies
            if pygame.sprite.groupcollide(self.zombies, self.bullets,
                True, True, pygame.sprite.collide_circle):
                pass

            # bullets cannot go across walls (tile) and grasses
            if pygame.sprite.groupcollide(self.tiles, self.bullets,
                False, True, pygame.sprite.collide_circle):
                pass

            if pygame.sprite.groupcollide(self.grasses, self.bullets,
                False, True, pygame.sprite.collide_circle):
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

            # players cannot touch fake grasses when they are activated
            for fakeGrass in self.fakeGrasses:
                if (pygame.sprite.collide_circle(fakeGrass, self.hero) 
                    and fakeGrass.activated == True):
                    fakeGrass.kill()
                    self.collisions.add(Collision(hero.x, hero.y))
                    self.gameOver = True

            # player need to avoid the boss and the bullets
            if pygame.sprite.groupcollide(self.heroGroup, self.guyGroup, 
                False, False, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True

            if pygame.sprite.groupcollide(self.heroGroup, self.guyBullets,
                False, False, pygame.sprite.collide_circle):
                self.collisions.add(Collision(hero.x, hero.y))
                self.gameOver = True


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


    def timerFired3(self, dt):
        # update moving obstacles when hero moves to some range of x and y
        for fallingObstacle in self.fallingObstacles:
            if (self.hero.y >= 300 and self.hero.y <= 320 and 
                abs(fallingObstacle.x - self.hero.x) <= 15):
                fallingObstacle.move = True
            if fallingObstacle.move == True:
                fallingObstacle.update(self.width, self.height)

        for risingObstacle in self.risingObstacles:
            if abs(risingObstacle.x - self.hero.x) <= 15:
                risingObstacle.move = True
            if risingObstacle.move == True:
                risingObstacle.update(self.width, self.height)

        # update zombies when hero moves near
        for zombie in self.zombies:
            if (abs(zombie.x - self.hero.x) <= 100 and 
                abs(zombie.y - self.hero.y) <= 30):
                zombie.activated = True
            if zombie.activated == True and dt%3 == 0:
                zombie.upgrade()

        # update apples when hero moves near
        if (self.hero.y >= 300 and self.hero.y <= 320 and
            abs(self.hero.x - self.apple_00.x) <= 20):
            self.apple_00.activated = True
        if (self.hero.y >= 300 and self.hero.y <= 320 and
            abs(self.hero.x - self.apple_01.x) <= 20):
            self.apple_01.activated = True
        if (self.hero.y >= 300 and self.hero.y <= 320 and
            abs(self.hero.x - self.apple_02.x) <= 20):
            self.apple_02.activated = True
        if (self.hero.y >= 300 and self.hero.y <= 320 and
            abs(self.hero.x - self.apple_03.x) <= 20):
            self.apple_03.activated = True
        if (self.hero.y >= 300 and self.hero.y <= 320 and
            abs(self.hero.x - self.apple_04.x) <= 20):
            self.apple_04.activated = True
        if (self.hero.y <= 200 and abs(self.hero.x - self.apple_10.x) < 5):
            self.apple_10.activated = True
        if (self.hero.y <= 200 and abs(self.hero.x - self.apple_11.x) < 5):
            self.apple_11.activated = True
        if (self.hero.y <= 200 and abs(self.hero.x - self.apple_12.x) < 5):
            self.apple_12.activated = True
        if (self.hero.y <= 200 and abs(self.hero.x - self.apple_13.x) < 5):
            self.apple_13.activated = True
        if (self.hero.y <= 200 and abs(self.hero.x - self.apple_14.x) < 5):
            self.apple_14.activated = True
        if (self.hero.y <= 180 and self.hero.x > 390):
            self.apple_20.activated = True
            self.apple_21.activated = True
            self.apple_22.activated = True


    def timerFired4(self, dt):
        for giant in self.giantObstacles:
            if abs(giant.y - self.hero.y) <= 30:
                giant.activated = True

        if pygame.sprite.groupcollide(self.giantObstacles, self.bullets,
            False, True, pygame.sprite.collide_circle):
            self.giantObstacle.shot = True

        for random in self.randomFakeTiles:
            if self.touchReversedGiantObstacle(random):
                random.activated = True

        for reverse in self.giantObstacles:
            if self.giantObstacle.shot == False and reverse.y > 300:
                for fakeGrass in self.fakeGrasses:
                    fakeGrass.activated = True

    def timerFired5(self, dt):
        self.guyGroup.update(self.width, self.height)

        if pygame.sprite.groupcollide(self.guyGroup, self.bullets,
            False, True, pygame.sprite.collide_circle) and self.guy.immuneTime == 0:
            self.guy.hit = True
            if self.guy.currHealth >= 5:
                self.guy.currHealth -= 5

        self.guyHealthGreens.update(self.width, self.height)
        self.guyHealthReds.update(self.width, self.height)

        self.bossTime += 1
        size = random.randrange(40, 80)
        if self.bossTime > 100 and self.bossTime % 50 == 0 and not self.guy.die:
            self.guyBullets.add(GuyBullet(450, 340, size, self.bossBullet))
            self.bossBullet = not self.bossBullet

        self.guyBullets.update(self.width, self.height)

        if pygame.sprite.groupcollide(self.heroGroup, self.portalGroup,
            False, False, pygame.sprite.collide_circle) and self.guy.die:
            self.stage += 1
            self.temp = False
            self.init(self.stage, self.saved)
            self.hero = Hero(10, 190)
            self.heroGroup = pygame.sprite.GroupSingle(self.hero)
            self.initStage6()


    def timerFired7(self, dt):
        hero = self.heroGroup.sprite
        self.bossGroup.update(self.width, self.height)
        self.boxes.update(self.width, self.height)
        self.bouncingBoxes.update(self.width, self.height)
        self.circleBoxes.update(self.width, self.height)
        self.tracingBoxes.update(self.width, self.height)
        self.xBoxes.update(self.width, self.height)
        self.groupBoxes.update(self.width, self.height)

        self.bossTime += 1
        self.frameGroup.update(self.width, self.height)
        self.bgBoxes.update(self.width, self.height)

        if pygame.sprite.groupcollide(self.heroGroup, self.boxes,
            False, False):
            self.collisions.add(Collision(hero.x, hero.y))
            self.gameOver = True

        if pygame.sprite.groupcollide(self.heroGroup, self.bouncingBoxes,
            False, False):
            self.collisions.add(Collision(hero.x, hero.y))
            self.gameOver = True

        if pygame.sprite.groupcollide(self.heroGroup, self.circleBoxes,
            False, False):
            self.collisions.add(Collision(hero.x, hero.y))
            self.gameOver = True

        if pygame.sprite.groupcollide(self.heroGroup, self.tracingBoxes,
            False, False):
            self.collisions.add(Collision(hero.x, hero.y))
            self.gameOver = True

        if pygame.sprite.groupcollide(self.heroGroup, self.xBoxes,
            False, False):
            self.collisions.add(Collision(hero.x, hero.y))
            self.gameOver = True

        if pygame.sprite.groupcollide(self.heroGroup, self.groupBoxes,
            False, False):
            self.collisions.add(Collision(hero.x, hero.y))
            self.gameOver = True

        if self.bossTime % 15 == 0:
            self.bgBoxes.add(BgBox(300, 200))

        if self.bossTime == 60:
            self.boss = Boss(300, 200)
            self.bossGroup.add(self.boss)
        
        elif self.bossTime >= 200 and self.bossTime <= 350:
            if self.bossTime % 5 == 0:
                self.tracingBoxes.add(TracingBox(300, 200, 0, 0))

        elif self.bossTime == 500:
            self.createXBoxes()

        elif self.bossTime == 760:
            self.xBoxes.empty()
            self.createCircleBoxes()

        elif self.bossTime == 830:
            self.createCircleBoxes()

        elif self.bossTime == 900:
            self.createCircleBoxes()

        elif self.bossTime == 1000:
            self.circleBoxes.empty()

        elif (self.bossTime >= 1000 and self.bossTime < 1400 and 
            self.bossTime % 50 == 0):
            speed = -4
            for y in range(37, 122, 24):
                self.groupBoxes.add(GroupBox(541, y, speed, 0))
            for y in range(363, 266, -24):
                self.groupBoxes.add(GroupBox(541, y, speed, 0))

        elif (self.bossTime >= 1400 and self.bossTime < 1800 and 
            self.bossTime % 20 == 0):
            xSpeed = (self.hero.x - 300) / 40
            ySpeed = (self.hero.y - 200) / 40
            self.bouncingBoxes.add(BouncingBox(300, 200, xSpeed, ySpeed))

        elif (self.bossTime >= 1800 and self.bossTime < 2100 and
            self.bossTime % 70 == 0):
            speed = -6
            for x in range(541, 733, 24):
                self.groupBoxes.add(GroupBox(x, 37, speed, 0))
                self.groupBoxes.add(GroupBox(x, 363, speed, 0))

        elif (self.bossTime >= 2200 and self.bossTime < 2500 and 
            self.bossTime % 20 == 0):
            xSpeed = (self.hero.x - 300) / 40
            ySpeed = (self.hero.y - 200) / 40
            self.bouncingBoxes.add(BouncingBox(300, 200, xSpeed, ySpeed))

        if self.bossTime == 2500:
            self.boss.die = True
            self.boss.goDie()

            self.portal = Portal(300, 200)
            self.portalGroup.add(self.portal)

        if pygame.sprite.groupcollide(self.heroGroup, self.portalGroup,
            False, False, pygame.sprite.collide_circle):
            self.stage += 1
            self.temp = False
            self.init(self.stage, self.saved)
            self.hero = Hero(450, 270)
            self.heroGroup = pygame.sprite.GroupSingle(self.hero)
            self.initFinal()


    def createXBoxes(self):
        for index in range(1, 11):
            xSpeed = 25 * index / 45
            ySpeed = 17 * index / 45
            self.xBoxes.add(XBox(300, 200, xSpeed, ySpeed, index))
            self.xBoxes.add(XBox(300, 200, -xSpeed, ySpeed, index))
            self.xBoxes.add(XBox(300, 200, xSpeed, -ySpeed, index))
            self.xBoxes.add(XBox(300, 200, -xSpeed, -ySpeed, index))

    def createCircleBoxes(self):
        angle = 0
        for i in range(18):
            self.createACircleBox(angle)
            angle += math.pi/9

    def createACircleBox(self, angle):
        xSpeed = 8 * math.cos(angle)
        ySpeed = 8 * math.sin(angle)
        self.circleBoxes.add(CircleBox(300, 200, xSpeed, ySpeed))


    def redrawAll(self, screen):
        self.backgrounds.draw(screen)
        self.bars.draw(screen)
        self.columns.draw(screen)
        self.blocks.draw(screen)
        self.bossBgGroup.draw(screen)
        self.bgBoxes.draw(screen)
        self.portalGroup.draw(screen)
        self.trees.draw(screen)
        self.planks.draw(screen)
        self.elevators.draw(screen)
        self.obstacles.draw(screen)
        self.flippedObstacles.draw(screen)
        self.longUps.draw(screen)
        self.longDowns.draw(screen)
        self.leftObstacles.draw(screen)
        self.rightObstacles.draw(screen)
        self.thornUps.draw(screen)
        self.thornDowns.draw(screen)
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
        self.fakeGrasses.draw(screen)
        self.randomFakeTiles.draw(screen)
        self.giantObstacles.draw(screen)
        self.zoomingObstacles.draw(screen)
        self.apples.draw(screen)
        self.fallingApples.draw(screen)
        self.movingApples.draw(screen)
        self.guyGroup.draw(screen)
        self.guyBullets.draw(screen)
        self.guySigns.draw(screen)
        self.guyHealthGreens.draw(screen)
        self.guyHealthReds.draw(screen)
        self.boxes.draw(screen)
        self.bouncingBoxes.draw(screen)
        self.circleBoxes.draw(screen)
        self.tracingBoxes.draw(screen)
        self.xBoxes.draw(screen)
        self.groupBoxes.draw(screen)
        self.bossGroup.draw(screen)
        self.blackFrameGroup.draw(screen)
        self.frameGroup.draw(screen)
        if self.key == False:
            self.collisions.draw(screen)
        self.heroGroup.draw(screen)
        self.bullets.draw(screen)
        self.enemyCollisions.draw(screen)
        if self.gameOver and self.key == False:
            gameOverImage = pygame.image.load("gameOver.png").convert_alpha()
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
        image = pygame.image.load("hero.png").convert_alpha()
        Hero.heroImage = pygame.transform.scale(image, (20, 20))

    def flipImage(self):
        self.image = pygame.transform.flip(self.image, True, False)

    def vFlipImage(self): # vertically flip image
        self.image = pygame.transform.flip(self.image, False, True)

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
        self.jumpStatus = 0
        self.jumpTime = 0
        self.deltaX = 0
        self.deltaY = 0
        self.rising = False
        # the following are for boss stage
        if IWANNA.stage == 7:
            self.onFloor = True # False for on ceiling and up side down
            self.vFlipped = False # if vertically flipped
            self.speed7 = 15
            self.ySpeed = 15
            self.maxSpeed = 10


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
        if IWANNA.stage == 7:
            if self.x <= 60:
                return False
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
        if IWANNA.stage == 7:
            if self.x >= 540:
                return False
        if self.x + self.width/2 + self.xSpeed > 600: # out of the screen
            return False
        else:
            # similar to isLegalMoveLeft method
            for tile in IWANNA.tiles:
                # print("right, tile", self.yInRange(tile))
                if (self.yInRange(tile) and
                    self.x < tile.x and
                    self.x+self.width/2+self.xSpeed>tile.x-tile.blockSize/2):
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
    
    # check whether the hero will hit the top when jumping
    def isLegalJump(self):
        # print("checking moving up", self.x, self.y)
        if self.y - self.height/2 + self.ySpeed < 0: # out of screen
            # print("out of screen", self.y, self.ySpeed)
            return False
        else:
            # similar to isLegalMoveLeft and isLegalMoveRight methods
            for tile in IWANNA.tiles:
                # print("inrange", self.xInRange(tile))
                if (self.xInRange(tile) and (self.y > tile.y) and
                    not abs(self.x-tile.x) == (self.width/2+tile.blockSize/2) and
                    # check if hero's top will collide with a tile's bottom
                    self.y-self.height/2+self.ySpeed<=tile.y+tile.blockSize/2):
                    self.deltaY = tile.y+tile.blockSize/2-(self.y-self.height/2)
                    # print("jump, hit tile", tile.x, tile.y, self.deltaY)
                    return False
            for grass in IWANNA.grasses:
                if (self.xInRange(grass) and (self.y > grass.y) and
                    not abs(self.x-grass.x) == (self.width/2+grass.blockSize/2) and
                    self.y-self.height/2+self.ySpeed<grass.y+grass.blockSize/2):
                    self.deltaY=grass.y+grass.blockSize/2-(self.y-self.height/2)
                    # print("jump, hit grass", grass.x, grass.y, self.deltaY)
                    return False
        # print("isLegalJump", self.y, self.ySpeed)
        return True

    def isLegalFall(self):
        for grass in IWANNA.grasses:
            if (self.xInRange(grass) and self.y < grass.y and
                self.y+self.height/2+self.ySpeed>=grass.y-grass.blockSize/2):
                if self.rising == True:
                    self.deltaY = grass.y-grass.blockSize/2-(self.y+self.height/2)
                # print("fall, hit grass", grass.x, grass.y, self.deltaY)
                return False
        for block in IWANNA.blocks:
            if (self.xInRange(block) and self.y < block.y and
                self.y+self.height/2+self.ySpeed>=block.y-block.blockSize/2):
                if self.rising == True:
                    self.deltaY = block.y-block.blockSize/2-(self.y+self.height/2)
                return False
        for fakeGrass in IWANNA.fakeGrasses:
            if (self.xInRange(fakeGrass) and self.y < fakeGrass.y and
                self.y + self.height/2 + self.ySpeed >= fakeGrass.y - 
                fakeGrass.blockSize/2 and fakeGrass.activated == False):
                if self.rising == True:
                    self.deltaY = (fakeGrass.y - fakeGrass.blockSize/2 - 
                        (self.y+self.height/2))
                # print("fall, hit grass", grass.x, grass.y, self.deltaY)
                return False
        for plank in IWANNA.planks:
            if (self.xInRange(plank) and self.y < plank.y and
                self.y+self.height/2+self.ySpeed>=plank.y-plank.height/2):
                self.deltaY = plank.y-plank.height/2-(self.y+self.height/2)
                self.xSpeed += plank.xSpeed
                return False
        for elevator in IWANNA.elevators:
            if (self.xInRange(elevator) and self.y < elevator.y and
                self.y+self.height/2+self.ySpeed>=elevator.y-elevator.height/2):
                self.deltaY = elevator.y-elevator.height/2-(self.y+self.height/2)
                self.ySpeed += elevator.ySpeed
                return False
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
            # print("legal jump", self.y, self.ySpeed)
            if abs(self.ySpeed) >= self.maxYSpeed:
                self.ySpeed = -self.maxYSpeed
        else:
            self.ySpeed = self.deltaY
            # print("moving up", self.y, self.ySpeed)
        # print("yspeed", self.ySpeed)


    # the following four functions are for stage 7 only
    def moveToTop(self):
        if self.canMoveUp():
            self.ySpeed = 0 - self.speed7
        else:
            self.ySpeed = 0

    def moveToBottom(self):
        if self.canMoveDown():
            self.ySpeed = self.speed7
        else:
            self.ySpeed = 0

    def canMoveUp(self):
        if self.y - self.height/2 - self.speed7 < 25:
            return False
        else:
            return True

    def canMoveDown(self):
        if self.y + self.height/2 + self.speed7 > 375:
            return False
        else:
            return True

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

        if IWANNA.stage != 7:
            if (keysDown(pygame.K_UP) and self.jumpStatus != 3 and self.jumpTime < 7): # try to jump
                # print("pressed Up")
                if(self.jumpStatus == 0):
                    self.moveUp()
                    self.jumpStatus += 1
                    self.jumpTime = 0
                elif(self.jumpStatus == 2):
                    self.moveUp()
                    self.jumpStatus += 1
                    self.jumpTime = 0
                self.jumpTime += 1
            elif self.isLegalFall(): # in air but not jumping, i.e. free fall
                # print("falling")
                if(self.jumpStatus == 1):
                    self.jumpStatus += 1
                self.jumpTime = 0
                self.ySpeed += self.gravity
                if self.ySpeed < 0:
                    self.rising = True
                if self.ySpeed <= -self.maxYSpeed:
                    self.ySpeed = -self.maxYSpeed
                if not self.isLegalJump():
                    self.ySpeed = self.deltaY

            else: # hit the ground
                self.yStatus = 1
                # print("deltaY", self.deltaY)
                self.jumpStatus = 0
                self.jumpTime = 0
                self.ySpeed = self.deltaY

        if self.flipped == True:
            self.flipImage()

        # in stage 7, there is no gravity, if player presses the Up button,
        # hero rises constant speed to the ceiling and stand / walk there;
        # if player presses the Down button, hero falls constant speed to
        # the bottom floor and stand / walk there.
        if IWANNA.stage == 7:
            # boss stage
            if keysDown(pygame.K_UP):
                if self.onFloor == True:
                    self.vFlipped = True
                else:
                    self.vFlipped = False
                self.onFloor = False
                self.moveToTop()

            elif keysDown(pygame.K_DOWN):
                if self.onFloor == False:
                    self.vFlipped = True
                else:
                    self.vFlipped = False
                self.onFloor = True
                self.moveToBottom()

            if self.onFloor == True:
                self.moveToBottom()
            else:
                self.moveToTop()

            if self.vFlipped == True:
                self.vFlipImage()


        self.deltaX = 0
        self.deltaY = 0
        super(Hero, self).update(screenWidth, screenHeight)


class Background(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("orangeBG.png").convert()
        Background.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Background, self).__init__(x, y, Background.image, 10)


class Background2(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("greenBG.png").convert()
        Background2.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Background2, self).__init__(x, y, Background2.image, 10)


class Block2(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("greenBlock.png").convert()
        Block2.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Block2, self).__init__(x, y, Block2.image, 10)


class Block(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("orangeBlock.png").convert()
        Block.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Block, self).__init__(x, y, Block.image, 10)


class Bar(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("orangeBar.png").convert()
        Bar.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Bar, self).__init__(x, y, Bar.image, 10)


class Bar2(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("greenBarBar.png").convert()
        Bar2.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Bar2, self).__init__(x, y, Bar2.image, 10)


class Column(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("orangeColumn.png").convert()
        Column.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Column, self).__init__(x, y, Column.image, 10)


class Column2(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("greenColumn.png").convert()
        Column2.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Column2, self).__init__(x, y, Column2.image, 10)


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
        Button.image0 = pygame.transform.scale(image0, (10, 20))
        # icon for activated button
        image1 = pygame.image.load("button2.png").convert_alpha()
        Button.image1 = pygame.transform.scale(image1, (4, 20))

    def __init__(self, x, y, activated):
        self.activated = activated
        if self.activated == False:
            super(Button, self).__init__(x, y, Button.image0, 5)
        else:
            super(Button, self).__init__(x, y, Button.image1, 2)

    def activate(self):
        for fake in IWANNA.fakeTiles:
            fake.activated = True

    def update(self, screenWidth, screenHeight):
        # print(self.activated)
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
        self.activated = False
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
        if self.activated == True:
            self.collapse()
        if self.y > 410:
            self.kill()
        super(FakeTile, self).update(screenWidth, screenHeight)


class RandomFakeTile(FakeTile):
    def __init__(self, x, y):
        super(RandomFakeTile, self).__init__(x, y)
        # self.activated = True
        self.initXSpeed = random.randrange(-3, 3)
        self.initYSpeed = random.randrange(-3, 0)


class FakeGrass(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("fakeGrass.png").convert_alpha()
        FakeGrass.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y, step):
        super(FakeGrass, self).__init__(x, y, FakeGrass.image, 10)
        self.original = FakeGrass.image
        self.image = self.original
        self.angle = 0
        self.activated = False
        self.initXSpeed = 0
        self.initYSpeed = -10
        self.gravity = 0.5
        self.step = step

    def collapse(self):
        # when a fake grass collapses, it rises at first and then falls 
        # (with gravitation acceleration) while rotating
        if self.angle == 0:
            self.ySpeed = self.initYSpeed
        self.angle += 5
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.ySpeed += self.gravity
        
    def update(self, screenWidth, screenHeight):
        if self.activated == True:
        # after activated, the step increases, and grasses collapse one by one
            self.step += 1
        if self.activated == True and self.step >= 0:
            self.collapse()
        if self.y > 410:
            self.kill()
        super(FakeGrass, self).update(screenWidth, screenHeight)


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

    def __init__(self, x, y, speed=-60):
        super(RisingObstacle, self).__init__(x, y, RisingObstacle.image, 10)
        self.ySpeed = speed
        self.move = False

    def update(self, screenWidth, screenHeight):
        if self.y < 0:
            self.kill()
        super(RisingObstacle, self).update(screenWidth, screenHeight)


class FallingObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("fallingO.png").convert_alpha()
        FallingObstacle.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y, speed=20):
        super(FallingObstacle, self).__init__(x, y, FallingObstacle.image, 10)
        self.ySpeed = speed
        self.move = False

    def update(self, screenWidth, screenHeight):
        if self.y > 400:
            self.kill()
        super(FallingObstacle, self).update(screenWidth, screenHeight)


class ZoomingObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("zooming.png").convert_alpha()
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
        if self.y > 400:
            self.kill()
        self.deltaY = 0
        super(BabyObstacle, self).update(screenWidth, screenHeight)


class LongUp(GameObject): # long obstacle pointing upward
    @staticmethod
    def init():
        image = pygame.image.load("longUpSpike.png").convert_alpha()
        LongUp.obstacleImage = pygame.transform.scale(image, (20, 40))

    def __init__(self, x, y):
        super(LongUp, self).__init__(x, y, LongUp.obstacleImage, 10)
        self.originalY = y
        self.minY = self.originalY - 20
        self.maxY = self.originalY
        self.initYSpeed = -0.5
        self.up = True
        self.height = 40
        self.width = 20

    def setDirection(self):
        if self.y == self.minY:
            self.up = False # begin to go down
        elif self.y == self.maxY:
            self.up = True # begin to go up

    def move(self):
        self.setDirection()
        if self.up == True:
            self.ySpeed = self.initYSpeed
        elif self.up == False:
            self.ySpeed = 0 - self.initYSpeed

    def update(self, screenWidth, screenHeight):
        self.move()
        super(LongUp, self).update(screenWidth, screenHeight)


class LongDown(GameObject): # long obstacle pointing downward
    @staticmethod
    def init():
        image = pygame.image.load("longDownSpike.png").convert_alpha()
        LongDown.obstacleImage = pygame.transform.scale(image, (20, 40))

    def __init__(self, x, y):
        super(LongDown, self).__init__(x, y, LongDown.obstacleImage, 10)
        self.originalY = y
        self.minY = self.originalY - 20
        self.maxY = self.originalY
        self.initYSpeed = 0.5
        self.up = True
        self.height = 40
        self.width = 20

    def setDirection(self):
        if self.y == self.minY:
            self.up = False # begin to go down
        elif self.y == self.maxY:
            self.up = True # begin to go up

    def move(self):
        self.setDirection()
        if self.up == True:
            self.ySpeed = 0 - self.initYSpeed
        elif self.up == False:
            self.ySpeed = self.initYSpeed

    def update(self, screenWidth, screenHeight):
        self.move()
        super(LongDown, self).update(screenWidth, screenHeight)


class LeftBar(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("leftBar.png").convert()
        LeftBar.barImage = pygame.transform.scale(image, (10, 40))

    def __init__(self, x, y):
        super(LeftBar, self).__init__(x, y, LeftBar.barImage, 5)
        self.xSpeed = -40
        self.move = False

    def update(self, screenWidth, screenHeight):
        if self.x < 0:
            self.kill()
        super(LeftBar, self).update(screenWidth, screenHeight)


class RightBar(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("rightBar.png").convert()
        RightBar.barImage = pygame.transform.scale(image, (10, 40))

    def __init__(self, x, y):
        super(RightBar, self).__init__(x, y, RightBar.barImage, 5)
        self.xSpeed = 40
        self.move = False

    def update(self, screenWidth, screenHeight):
        if self.x > 600:
            self.kill()
        super(RightBar, self).update(screenWidth, screenHeight)


class ThornUp(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("thornUp.png").convert()
        ThornUp.thornImage = pygame.transform.scale(image, (40, 10))

    def __init__(self, x, y):
        super(ThornUp, self).__init__(x, y, ThornUp.thornImage, 5)


class ThornDown(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("thornDown.png").convert()
        ThornDown.thornImage = pygame.transform.scale(image, (40, 10))

    def __init__(self, x, y):
        super(ThornDown, self).__init__(x, y, ThornDown.thornImage, 5)


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

    def __init__(self, x, y, xMin, xMax):
        super(Zombie, self).__init__(x, y, Zombie.image0, 10)
        self.status = 0
        self.direction = random.choice([-1, 1])
        self.xSpeed = self.direction * random.randint(1, 2)
        self.xMin = xMin
        self.xMax = xMax
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


class Tree(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("tree.png").convert_alpha()
        Tree.treeImage = pygame.transform.scale(image, (75, 120))

    def __init__(self, x, y):
        super(Tree, self).__init__(x, y, Tree.treeImage, 37)

    def isLeaf(self, x, y): # check if (x, y) is the leaf part of the tree
        leafCenterX = self.x
        leafCenterY = self.y - self.height/4
        leafRadius = self.width/2
        if ((x - leafCenterX)**2 + (y - leafCenterY)**2) ** 0.5 < leafRadius:
            return True
        return False


class Apple(GameObject):
    @staticmethod
    def init():
        image1 = pygame.image.load("apple1.png").convert_alpha()
        Apple.staticImage = pygame.transform.scale(image1, (16, 16))
        image2 = pygame.image.load("apple2.png").convert_alpha()
        Apple.moveImage = pygame.transform.scale(image2, (17, 17))

    def __init__(self, x, y):
        super(Apple, self).__init__(x, y, Apple.staticImage, 8)

    def update(self, screenWidth, screenHeight):
        if self.x > 600 or self.x < 0:
            self.kill()
        if self.y > 400 or self.y < 0:
            self.kill()
        super(Apple, self).update(screenWidth, screenHeight)


class FallingApple(Apple): # tremble; when activated, fall with gravity
    def __init__(self, x, y):
        super(FallingApple, self).__init__(x, y)
        self.trembling = True # when begin to fall, stop trembling
        self.activated = False # fall if it's True
        self.gravity = 1
        self.imageChanged = False
        self.step = 0

    def changeImage(self):
        if self.imageChanged == False:
            self.image = Apple.moveImage
            self.y += 1
        else:
            self.image = Apple.staticImage
            self.y -= 1
        self.imageChanged = not self.imageChanged

    def move(self):
        self.image = Apple.moveImage
        self.ySpeed += self.gravity

    def update(self, screenWidth, screenHeight):
        if self.activated == False: # not falling, tremble, not move
            self.trembling = True
        else: # falling, stop tremble, move
            self.trembling = False
            self.move()
        if self.trembling == True and self.step % 5 == 0:
            self.changeImage()
        self.step += 1
        super(FallingApple, self).update(screenWidth, screenHeight)


class MovingApple(Apple): # tremble; when activated, move horizontally
    def __init__(self, x, y):
        super(MovingApple, self).__init__(x, y)
        self.trembling = True # when begin to fall, stop trembling
        self.activated = False # fall if it's True
        self.imageChanged = False
        self.step = 0

    def changeImage(self):
        if self.imageChanged == False:
            self.image = Apple.moveImage
            self.y += 1
        else:
            self.image = Apple.staticImage
            self.y -= 1
        self.imageChanged = not self.imageChanged

    def move(self):
        self.image = Apple.moveImage
        self.xSpeed = 7

    def update(self, screenWidth, screenHeight):
        if self.activated == False: # not moving, just tremble
            self.trembling = True
        else: # moving, stop tremble
            self.trembling = False
            self.move()
        if self.trembling == True and self.step % 5 == 0:
            self.changeImage()
        self.step += 1
        super(MovingApple, self).update(screenWidth, screenHeight)


class Plank(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("plank.png").convert()
        Plank.image = pygame.transform.scale(image, (30, 10))

    def __init__(self, x, y, xMin, xMax):
        super(Plank, self).__init__(x, y, Plank.image, 5)
        self.xMin = xMin
        self.xMax = xMax
        self.speed = 1
        self.right = True # True if moving right, False if moving left

    def setDirection(self):
        if self.x <= self.xMin:
            self.right = True
        elif self.x >= self.xMax:
            self.right = False

    def update(self, screenWidth, screenHeight):
        self.setDirection()
        if self.right == True:
            self.xSpeed = self.speed
        else:
            self.xSpeed = 0 - self.speed
        # print(self.xSpeed)
        super(Plank, self).update(screenWidth, screenHeight)


class Elevator(GameObject):
    def __init__(self, x, y, yMin, yMax, index):
        super(Elevator, self).__init__(x, y, Plank.image, 5)
        self.yMin = yMin
        self.yMax = yMax
        self.speed = random.randint(1, 2)
        self.index = index
        self.up = random.choice([True, False])
        # True if moving up, False if moving down
        self.size = 30
        self.maxSize = 35
        self.minSize = 20
        self.enlarge = random.choice([True, False])
        # decides whether the elevator increases or decreases in size at first
        self.addSize = random.choice([1, 2])
        self.time = 0
        self.interval = random.randint(4, 8)
        # the interval determines the speed the elevator changes its size

    def setDirection(self):
        if self.y <= self.yMin:
            self.up = False
        elif self.y >= self.yMax:
            self.up = True

    def setEnlarge(self):
        if self.size <= self.minSize:
            self.enlarge = True
        elif self.size >= self.maxSize:
            self.enlarge = False

    def extend(self):
        if self.enlarge == True:
            self.size += self.addSize
        else:
            self.size -= self.addSize
        self.image = pygame.transform.scale(Plank.image, (self.size, 10))

    def update(self, screenWidth, screenHeight):
        self.time += 1

        self.setDirection()
        if self.up == True:
            self.ySpeed = 0 - self.speed
        else:
            self.ySpeed = self.speed

        self.setEnlarge()
        if self.time % self.interval == 0:
            self.extend()
        super(Elevator, self).update(screenWidth, screenHeight)


class GiantObstacle(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("spike.png").convert_alpha()
        GiantObstacle.image = pygame.transform.scale(image, (80, 80))

    def __init__(self, x, y):
        super(GiantObstacle, self).__init__(x, y, GiantObstacle.image, 40)
        self.original = GiantObstacle.image
        self.image = self.original
        self.activated = False
        self.shot = False # becomes True if gets shot by bullet
        self.originalWidth = 80
        self.minWidth = 0
        self.maxWidth = 680
        self.shrinking = True
        self.originalY = self.y
        self.minY = 80
        self.rising = False
        self.falling = False
        self.step = 0
        # step 0: original
        # shrink to 0
        # step 1: 0 width
        # extend to max
        # step 2: max width
        # shrink to original
        # step 3: original size
        # rise to top
        # step 4: at top position
        # rotate
        # step 5: upside down
        # fall to ground
        self.ySpeed = 0
        self.angle = 0

    def setXDirection(self):
        if self.width == self.minWidth:
            self.shrinking = False
            self.step += 1 # will begin to extend
        elif self.width == self.maxWidth:
            self.step += 1 # will begin to shrink
            self.shrinking = True
        if (self.width <= self.originalWidth and self.shrinking == True 
            and self.step != 0):
            # when the giantObstacle shrinks to the original size
            self.shrinking = False
            self.step += 1

    def setYDirection(self):
        if self.y <= self.minY:
            self.rising = False
            self.step += 1
        if self.step == 3:
            self.rising = True
        elif self.step == 4:
            self.rising = False
        elif self.step == 5:
            self.falling = True
        
    def extend(self):
        self.setXDirection() 
        if self.shrinking == True:
            if self.step == 0:
                self.width -= 5
            elif self.step == 2:
                self.width -= 20
        elif self.step == 1:
            self.width += 5
        self.image = pygame.transform.scale(self.original, (self.width, 80))

    def move(self):
        self.setYDirection()
        if self.rising == True:
            self.ySpeed = -4
        elif self.falling == True:
            self.ySpeed = 6

    def rotate(self):
        self.ySpeed = 0.4
        self.image = pygame.transform.rotate(self.original, self.angle)
        self.angle += 5
        if self.angle == 180:
            self.step += 1

    def update(self, screenWidth, screenHeight):
        if self.activated == True:
            self.extend()
            self.move()
            if self.step == 4:
                self.rotate()
            if self.step > 4:
                self.image = pygame.transform.flip(self.original, True, True)
            if self.y > 440:
                self.kill()
            # print(self.step)
        super(GiantObstacle, self).update(screenWidth, screenHeight)


class Portal(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("portal.png").convert_alpha()
        Portal.image = pygame.transform.scale(image, (20, 20))

    def __init__(self, x, y):
        super(Portal, self).__init__(x, y, Portal.image, 10)


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


class GuySign(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("guySign.png").convert_alpha()
        GuySign.image = pygame.transform.scale(image, (180, 45))
    
    def __init__(self, x, y):
        super(GuySign, self).__init__(x, y, GuySign.image, 90)


class Guy(GameObject):
    @staticmethod
    def init():
        image1 = pygame.image.load("guy.png").convert_alpha()
        Guy.image = pygame.transform.scale(image1, (80, 80))
        image2 = pygame.Surface((80, 80), pygame.SRCALPHA)
        pygame.draw.rect(image2, (76, 11, 2), (0, 0, 80, 80))
        Guy.immuneImage = image2

    def __init__(self, x, y):
        super(Guy, self).__init__(x, y, Guy.image, 90)
        self.totalHealth = 100
        self.currHealth = 100
        self.lostHealth = 0
        self.hit = False
        self.immuneTime = 0 # during the immune time, guy is untargetable
        self.maxImmuneTime = 20
        self.time = 0
        self.die = False
        self.gravity = 0.5
        self.angle = 0

    def getLostHealth(self):
        self.lostHealth = self.totalHealth - self.currHealth

    def getImmuneStatus(self):
        if self.hit == True:
            self.immuneTime = self.maxImmuneTime
        self.hit = False
        if self.immuneTime > 0:
            self.immuneTime -= 1

    def bling(self):
        if self.immuneTime % 5 == 0:
            self.image = Guy.image
        else:
            self.image = Guy.immuneImage

    def getDie(self):
        if self.currHealth <= 0:
            self.die = True
            self.ySpeed = -20

    def getImage(self):
        if self.immuneTime > 0:
            self.bling()
        else:
            self.image = Guy.image

    def goAway(self):
        self.rotate()
        self.ySpeed += self.gravity

    def rotate(self):
        self.image = pygame.transform.rotate(Guy.image, self.angle)
        self.angle += 30

    def update(self, screenWidth, screenHeight):
        self.getLostHealth()
        if self.die == False:
            self.getDie()
            self.getImage()
            self.getImmuneStatus()
            # print(self.immuneTime)
        else:
            self.goAway()
            IWANNA.guyBullets.empty()
        # print(self.currHealth)
        super(Guy, self).update(screenWidth, screenHeight)


class GuyHealthGreen(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("greenBar.png").convert_alpha()
        GuyHealthGreen.image = pygame.transform.scale(image, (500, 20))

    def __init__(self, x, y):
        super(GuyHealthGreen, self).__init__(x, y, GuyHealthGreen.image, 15)
        self.length = 500
        self.changed = False
        self.currHealth = IWANNA.guy.currHealth

    def resize(self):
        self.changed = IWANNA.guy.hit
        self.length = self.currHealth * 5
        self.image = pygame.transform.scale(GuyHealthGreen.image, 
            (self.length, 20))

    def update(self, screenWidth, screenHeight):
        self.currHealth = IWANNA.guy.currHealth
        self.resize()
        if IWANNA.guy.die == False:
            if self.changed:
                self.xSpeed = -12.5
            else:
                self.xSpeed = 0
        else:
            self.xSpeed = 0
        super(GuyHealthGreen, self).update(screenWidth, screenHeight)


class GuyHealthRed(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("redBar.png").convert_alpha()
        GuyHealthRed.image = pygame.transform.scale(image, (1, 20))

    def __init__(self, x, y):
        super(GuyHealthRed, self).__init__(x, y, GuyHealthRed.image, 15)
        self.length = 0
        self.changed = False
        self.lostHealth = IWANNA.guy.lostHealth

    def resize(self):
        self.changed = IWANNA.guy.hit
        self.length = self.lostHealth * 5
        self.image = pygame.transform.scale(GuyHealthRed.image, 
            (self.length, 20))

    def update(self, screenWidth, screenHeight):
        self.lostHealth = IWANNA.guy.lostHealth
        self.resize()
        if IWANNA.guy.die == False:
            if self.changed:
                self.xSpeed = -12.5
            else:
                self.xSpeed = 0
        else:
            self.xSpeed = 0
        super(GuyHealthRed, self).update(screenWidth, screenHeight)


class GuyBullet(GameObject):
    @staticmethod
    def init():
        GuyBullet.yellowImage = pygame.image.load("yellowBullet.png").convert_alpha()
        GuyBullet.whiteImage = pygame.image.load("whiteBullet.png").convert_alpha()

    def __init__(self, x, y, size, yellow):
        self.size = size
        self.yellow = yellow
        self.yellowImage = pygame.transform.scale(GuyBullet.yellowImage, (size, size))
        self.whiteImage = pygame.transform.scale(GuyBullet.whiteImage, (size, size))
        if self.yellow == True:
            self.image = self.yellowImage
            # print("yellow", self.size)
        else:
            self.image = self.whiteImage
            # print("white", self.size)
        super(GuyBullet, self).__init__(x, y, self.image, 20)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.xSpeed = -4
        self.time = 0

    def bling(self):
        if self.yellow == True:
            self.yellow = False
            self.image = self.whiteImage
        else:
            self.yellow = True
            self.image = self.yellowImage
    
    def update(self, screenWidth, screenHeight):
        if self.time%5 == 0:
            self.bling()
        if self.x < -self.size/2:
            self.kill()
        self.time += 1
        super(GuyBullet, self).update(screenWidth, screenHeight)


class BlackFrame(GameObject):
    @staticmethod
    def init():
        BlackFrame.image = pygame.Surface((600, 400), pygame.SRCALPHA)
        pygame.draw.rect(BlackFrame.image, (0, 0, 0), (0, 0, 49, 400))
        pygame.draw.rect(BlackFrame.image, (0, 0, 0), (0, 0, 600, 24))
        pygame.draw.rect(BlackFrame.image, (0, 0, 0), (551, 0, 49, 400))
        pygame.draw.rect(BlackFrame.image, (0, 0, 0), (0, 376, 600, 24))

    def __init__(self, x, y):
        super(BlackFrame, self).__init__(x, y, BlackFrame.image, 300)


class Frame(GameObject):
    @staticmethod
    def init():
        pointlist = [(0, 0), (0, 348), (498, 348), (498, 0)]

        Frame.green = pygame.Surface((500, 350), pygame.SRCALPHA)
        pygame.draw.lines(Frame.green, (28, 231, 53), True, pointlist, 2)

        Frame.pink = pygame.Surface((500, 350), pygame.SRCALPHA)
        pygame.draw.lines(Frame.pink, (185, 0, 148), True, pointlist, 2)

        Frame.yellow = pygame.Surface((500, 350), pygame.SRCALPHA)
        pygame.draw.lines(Frame.yellow, (189, 217, 22), True, pointlist, 2)

        Frame.red = pygame.Surface((500, 350), pygame.SRCALPHA)
        pygame.draw.lines(Frame.red, (181, 0, 14), True, pointlist, 2)

        Frame.blue = pygame.Surface((500, 350), pygame.SRCALPHA)
        pygame.draw.lines(Frame.blue, (38, 59, 230), True, pointlist, 2)

        Frame.cyan = pygame.Surface((500, 350), pygame.SRCALPHA)
        pygame.draw.lines(Frame.cyan, (24, 175, 192), True, pointlist, 2)

    def __init__(self, x, y):
        super(Frame, self).__init__(x, y, Frame.green, 250)
        self.time = 0

    def changeColor(self):
        if self.time % 6 == 0:
            self.image = Frame.green
        elif self.time % 6 == 1:
            self.image = Frame.pink
        elif self.time % 6 == 2:
            self.image = Frame.blue
        elif self.time % 6 == 3:
            self.image = Frame.red
        elif self.time % 6 == 4:
            self.image = Frame.cyan
        else:
            self.image = Frame.yellow

    def update(self, screenWidth, screenHeight):
        self.changeColor()
        self.time += 1
        super(Frame, self).update(screenWidth, screenHeight)


class BossBg(GameObject):
    @staticmethod
    def init():
        BossBg.image = pygame.Surface((500, 350), pygame.SRCALPHA)
        pygame.draw.rect(BossBg.image, (5, 43, 52), (0, 0, 500, 350))

    def __init__(self, x, y):
        super(BossBg, self).__init__(x, y, BossBg.image, 250)


class BgBox(GameObject):
    @staticmethod
    def init():
        BgBox.image = pygame.Surface((50, 35), pygame.SRCALPHA)
        pygame.draw.rect(BgBox.image, (7, 72, 85), (0, 0, 50, 35), 15)

    def __init__(self, x, y):
        super(BgBox, self).__init__(x, y, BgBox.image, 25)
        self.width = 50
        self.height = 35
        self.time = 0

    def enlarge(self):
        self.width += 10
        self.height += 7
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (7, 72, 85), (0, 0, self.width, self.height), 30)

    def update(self, screenWidth, screenHeight):
        self.time += 1
        if self.time % 2 == 0:
            self.enlarge()
        if self.width >= 500 or self.height >= 350:
            self.kill()
        super(BgBox, self).update(screenWidth, screenHeight)


class Boss(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("boss2.png").convert_alpha()
        Boss.image = pygame.transform.scale(image, (150, 150))

    def __init__(self, x, y):
        self.originalImage = Boss.image
        self.image = pygame.transform.scale(self.originalImage, (10, 10))
        super(Boss, self).__init__(x, y, self.image, 5)
        self.width = 10
        self.height = 10
        self.size = 10
        self.angle = 0
        self.time = 0
        self.direction = 1 # to the right
        self.ySpeed = 0
        self.yMin = 180
        self.yMax = 220
        self.addSpeed = 3
        self.die = False

    def enlarge(self):
        self.width += 2
        self.height += 2
        self.image = pygame.transform.scale(Boss.image, 
            (self.width, self.height))

    def rotate(self):
        self.image = pygame.transform.rotate(self.originalImage, self.angle)
        self.angle += 60

    def updateOriginalImage(self):
        self.size += 2
        self.originalImage = pygame.transform.scale(
            Boss.image, (self.size, self.size))

    def setDirection(self):
        if IWANNA.hero.x <= 300:
            self.direction = -1
            self.image = self.originalImage
        else:
            self.direction = 1
            self.image = pygame.transform.flip(self.originalImage, True, False)

    def move(self):
        if self.y == self.yMax:
            self.ySpeed = -1
        elif self.y == self.yMin:
            self.ySpeed = 1

    def goDie(self):
        self.xSpeed = (IWANNA.hero.x - 300) / 10
        self.ySpeed = (IWANNA.hero.y - 200) / 10
        self.width -= 2
        self.height -= 2
        self.image = pygame.transform.scale(Boss.image, 
            (self.width, self.height))

    def update(self, screenWidth, screenHeight):
        self.time += 1
        if self.time % 2 == 0 and self.time <= 110:
            self.updateOriginalImage()
            self.enlarge()
            self.rotate()
        if self.time == 110:
            self.ySpeed = 1
        elif self.time > 110:
            self.setDirection()
            self.move()
        super(Boss, self).update(screenWidth, screenHeight)


class Box(GameObject):
    @staticmethod
    def init():
        image = pygame.image.load("box.png").convert_alpha()
        Box.image = pygame.transform.scale(image, (24, 24))

    def __init__(self, x, y, xSpeed, ySpeed):
        super(Box, self).__init__(x, y, Box.image, 12)
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.time = 0
        self.angle = 0

    def rotate(self):
        self.angle += 6
        self.image = pygame.transform.rotate(Box.image, self.angle)

    def update(self, screenWidth, screenHeight):
        self.time += 1
        self.rotate()
        super(Box, self).update(screenWidth, screenHeight)


class BouncingBox(Box):
    def __init__(self, x, y, xSpeed, ySpeed):
        super(BouncingBox, self).__init__(x, y, xSpeed, ySpeed)

    def update(self,screenWidth, screenHeight):
        if self.x + self.width/2 >= 550:
            self.xSpeed = -self.xSpeed
        elif self.x - self.width/2 <= 50:
            self.xSpeed = -self.xSpeed
        if self.y + self.height/2 >= 375:
            self.ySpeed = -self.ySpeed
        elif self.y - self.height/2 <= 25:
            self.ySpeed = -self.ySpeed
        if self.time > 150:
            self.kill()
        super(BouncingBox, self).update(screenWidth, screenHeight)


# Circle Boxes: when they hit the wall, they reset the speed so that they fly
# towards the hero. No matter how long they exist, they bounce only one time.
# The second time they hit the wall, they disappear
class CircleBox(Box):
    def __init__(self, x, y, xSpeed, ySpeed):
        super(CircleBox, self).__init__(x, y, xSpeed, ySpeed)
        self.activated = False
        self.acceleration = -0.05

    def resetSpeed(self):
        heroX = IWANNA.hero.x
        heroY = IWANNA.hero.y
        self.xSpeed = (heroX - self.x) / 50
        self.ySpeed = (heroY - self.y) / 50

    def update(self,screenWidth, screenHeight):
        if self.xSpeed > 0:
            self.xSpeed += self.acceleration
        elif self.xSpeed < 0:
            self.xSpeed -= self.acceleration
        if self.ySpeed > 0:
            self.ySpeed += self.acceleration
        elif self.ySpeed < 0:
            self.ySpeed -= self.acceleration
        if (self.x + self.width/2 >= 550 or
            self.x - self.width/2 <= 50 or
            self.y + self.height/2 >= 375 or
            self.y - self.height/2 <= 25):
            if self.activated == False:
                self.acceleration = 0
                self.activated = True
                self.resetSpeed()
            else:
                self.kill()
        super(CircleBox, self).update(screenWidth, screenHeight)


# This kind of box traces the player all the time; while updating the speed
# every half a second, they also have randomness in speed which somehow predict
# the possible future position of the player
class TracingBox(Box):
    def __init__(self, x, y, xSpeed, ySpeed):
        super(TracingBox, self).__init__(x, y, xSpeed, ySpeed)

    def resetSpeed(self):
        heroX = IWANNA.hero.x
        heroY = IWANNA.hero.y
        if IWANNA.hero.xSpeed >= 0:
            self.xSpeed = (heroX - self.x + 2) / 12 + random.randint(0, 3)
        elif IWANNA.hero.xSpeed <= 0:
            self.xSpeed = (heroX - self.x - 2) / 12 - random.randint(0, 3)
        if IWANNA.hero.ySpeed >= 0:
            self.ySpeed = (heroY - self.y + 1) / 12 + random.randint(0, 3)
        else:
            self.ySpeed = (heroY - self.y - 1) / 12 - random.randint(0, 3)

    def update(self, screenWidth, screenHeight):
        if self.time % 15 == 0:
            self.resetSpeed()
        if (self.x + self.width/2 >= 550 or
            self.x - self.width/2 <= 50 or
            self.y + self.height/2 >= 375 or
            self.y - self.height/2 <= 25):
            self.resetSpeed()
        if self.time > 100:
            self.kill()
        super(TracingBox, self).update(screenWidth, screenHeight)


# Also bounces when hits the border, and disappears after 100 seconds
class XBox(Box):
    def __init__(self, x, y, xSpeed, ySpeed, index):
        super(XBox, self).__init__(x, y, xSpeed, ySpeed)
        self.originalXSpeed = xSpeed
        self.originalYSpeed = ySpeed
        self.index = index

    def resetSpeed(self):
        self.ratio = 6 - abs(self.index - 6)
        if self.originalXSpeed > 0 and self.originalYSpeed > 0:
            self.xSpeed = -self.originalXSpeed / 10 * self.ratio / (self.index/3)
            self.ySpeed = self.originalYSpeed / 10 * self.ratio / (self.index/3)
        elif self.originalXSpeed < 0 and self.originalYSpeed > 0:
            self.xSpeed = self.originalXSpeed / 10 * self.ratio / (self.index/3)
            self.ySpeed = -self.originalYSpeed / 10 * self.ratio / (self.index/3)
        elif self.originalXSpeed < 0 and self.originalYSpeed < 0:
            self.xSpeed = -self.originalXSpeed / 10 * self.ratio / (self.index/3)
            self.ySpeed = self.originalYSpeed / 10 * self.ratio / (self.index/3)
        elif self.originalXSpeed > 0 and self.originalYSpeed < 0:
            self.xSpeed = self.originalXSpeed / 10 * self.ratio / (self.index/3)
            self.ySpeed = -self.originalYSpeed / 1 * self.ratio / (self.index/3)
        self.deltaXSpeed = random.randint(-self.ratio, self.ratio)/5
        self.deltaYSpeed = random.randint(-self.ratio, self.ratio)/5
        self.xSpeed += self.deltaXSpeed
        self.ySpeed += self.deltaYSpeed

    def update(self, screenWidth, screenHeight):
        if self.time >= 40 and self.time < 100:
            self.xSpeed = 0
            self.ySpeed = 0
        if self.time == 100:
            self.resetSpeed()
        if self.x + self.width/2 >= 550:
            self.xSpeed = -self.xSpeed
        elif self.x - self.width/2 <= 50:
            self.xSpeed = -self.xSpeed
        if self.y + self.height/2 >= 375:
            self.ySpeed = -self.ySpeed
        elif self.y - self.height/2 <= 25:
            self.ySpeed = -self.ySpeed
        if self.time > 250:
            self.kill()
        super(XBox, self).update(screenWidth, screenHeight)


# These boxes rolls towards the left of the screen at constant speed
# There is no motion vertically
class GroupBox(Box):
    def __init__(self, x, y, xSpeed, ySpeed):
        super(GroupBox, self).__init__(x, y, xSpeed, ySpeed)

    def update(self, screenWidth, screenHeight):
        if self.x - self.xSpeed <= 50:
            self.kill()
        super(GroupBox, self).update(screenWidth, screenHeight)


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()

IWANNA = Game(600, 400)
IWANNA.run()
