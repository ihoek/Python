import sys
import pygame
import random

# 함수 선언 부분
def paintEntity(entity, x, y) :
    monitor.blit(entity, (int(x), int(y)))


def playGame() :
    global monitor, ship, monster, missile

    r = random.randrange(0,256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)

    shipX = swidth/2
    shipY = sheight*0.8
    dx, dy = 0, 0

    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size
    monsterX = 0
    monsterY = random.randrange(0,int(swidth*0.3))
    monsterSpeed = random.randrange(1,5)

    missileX, missileY = None, None

    while True :
        (pygame.time.Clock()).tick(50)
        monitor.fill((r,g,b))

        for e in pygame.event.get() :
            if e.type in [pygame.QUIT] :
                pygame.quit()
                sys.exit()

            if e.type in [pygame.KEYDOWN] :
                if e.key == pygame.K_LEFT : dx = -5
                elif e.key == pygame.K_RIGHT: dx = +5
                elif e.key == pygame.K_UP: dy = -5
                elif e.key == pygame.K_DOWN: dy = +5
                elif e.key == pygame.K_SPACE :
                    if missileX == None :
                        missileX = shipX + shipSize[0] /2
                        missileY = shipY

            if e.type in [pygame.KEYUP] :
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT or e.key == pygame.K_UP or e.key == pygame.K_DOWN :
                    dx, dy = 0, 0

        if(0<shipX + dx and shipX+dx <= swidth-shipSize[0]) and (sheight/2 < shipY+ dy and shipY + dy <= sheight-shipSize[1]) :
            shipX += dx
            shipY += dy
        paintEntity(ship,shipX,shipY)

        monsterX += monsterSpeed
        if monsterX > swidth :
            monsterX = 0
            monsterY = random.randrange(0,int(swidth*0.3))
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = random.randrange(1,5)

        paintEntity(monster, monsterX, monsterY)

        if missileX != None :
            missileY -=10
            if missileY < 0 :
                missileX, missileY = None, None
        if missileX != None :
            paintEntity(missile,missileX,missileY)

        pygame.display.update()


#전역 변수 선언
r,g,b = [0]*3
swidth, sheight = 500, 700
monitor = None
ship, shipSize = None, 0

monsterImage = ['monster01.png','monster02.png','monster03.png','monster04.png','monster05.png'
                ,'monster06.png', 'monster07.png', 'monster08.png', 'monster09.png','monster10.png']

monster = None
missile = None

pygame.init()
monitor = pygame.display.set_mode((swidth,sheight))
pygame.display.set_caption('우주괴물 무찌르기')

ship = pygame.image.load(('ship02.png'))
shipSize = ship.get_rect().size

missile = pygame.image.load('missile.png')

playGame()