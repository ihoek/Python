import sys
import pygame
import random

# 함수 선언 부분
def paintEntity(entity, x, y) :
    monitor.blit(entity, (int(x), int(y)))

def writeScore(num, score) :
    #number score를 받아서 number에 따른 score 더하기
    #txt는 total score로 표현
    myfont = pygame.font.Font('NanumGothic.ttf',20)

    monstertxt1 = myfont.render(u'1번 괴물 : ' + str(num1) + '개', True, (225 - r, 225 - g, 225 - b))
    monstertxt2 = myfont.render(u'2번 괴물 : ' + str(num2) + '개', True, (225 - r, 225 - g, 225 - b))
    monstertxt3 = myfont.render(u'3번 괴물 : ' + str(num3) + '개', True, (225 - r, 225 - g, 225 - b))
    monstertxt4 = myfont.render(u'4번 괴물 : ' + str(num4) + '개', True, (225 - r, 225 - g, 225 - b))
    monstertxt5 = myfont.render(u'5번 괴물 : ' + str(num5) + '개', True, (225 - r, 225 - g, 225 - b))
    monstertxt6 = myfont.render(u'6번 괴물 : ' + str(num6) + '개', True, (225 - r, 225 - g, 225 - b))
    monstertxt7 = myfont.render(u'7번 괴물 : ' + str(num7) + '개', True, (225 - r, 225 - g, 225 - b))
    monstertxt8 = myfont.render(u'8번 괴물 : ' + str(num8) + '개', True, (225 - r, 225 - g, 225 - b))
    monstertxt9 = myfont.render(u'9번 괴물 : ' + str(num9) + '개', True, (225 - r, 225 - g, 225 - b))
    monstertxt10 = myfont.render(u'10번 괴물 : ' + str(num10) + '개', True, (225 - r, 225 - g, 225 - b))


    txt = myfont.render(u'파괴한 우주괴물 수 : ' + str(score), True, (225-r,225-g,225-b))

    monitor.blit(monstertxt1,(10,10))
    monitor.blit(monstertxt2, (10, 40))
    monitor.blit(monstertxt3, (10, 70))
    monitor.blit(monstertxt4, (10, 100))
    monitor.blit(monstertxt5, (10, 130))
    monitor.blit(monstertxt6, (10, 160))
    monitor.blit(monstertxt7, (10, 190))
    monitor.blit(monstertxt8, (10, 220))
    monitor.blit(monstertxt9, (10, 250))
    monitor.blit(monstertxt10, (10, 280))

    monitor.blit(txt, (10,sheight-40))

def playGame() :
    global monitor, ship, monster, missile, number
    global num1, num2, num3, num4, num5, num6, num7, num8, num9, num10
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
    fireCount = 0
    number = None

    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9 = 0
    num10 = 0

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
            fireCount -= 3

        paintEntity(monster, monsterX, monsterY)

        if missileX != None :
            missileY -=10
            if missileY < 0 :
                missileX, missileY = None, None

        if missileX != None :
            paintEntity(missile,missileX,missileY)

            if(monsterX < missileX and missileX < monsterX + monsterSize[0]) and (monsterY < missileY and missileY < monsterY + monsterSize[1]) :
                if monsterSpeed == 5 :
                    fireCount += 5
                elif monsterSpeed == 4 :
                    fireCount += 4
                elif monsterSpeed == 3 :
                    fireCount += 3
                elif monsterSpeed == 2 :
                    fireCount += 2
                elif monsterSpeed == 1 :
                    fireCount += 1

                monster = pygame.image.load(random.choice(monsterImage))
                number = random.choice(monsterImage)
                monsterSize = monster.get_rect().size
                monsterX = 0
                monsterY = random.randrange(0,int(swidth*0.3))
                monsterSpeed = random.randrange(1,5)

                missileX, missileY = None, None
                print(fireCount)
                #print(number)

                if number == "monster01.png":
                    num1 += 1
                elif number == "monster02.png":
                    num2 += 1
                elif number == "monster03.png":
                    num3 += 1
                elif number == "monster04.png":
                    num4 += 1
                elif number == "monster05.png":
                    num5 += 1
                elif number == "monster06.png":
                    num6 += 1
                elif number == "monster07.png":
                    num7 += 1
                elif number == "monster08.png":
                    num8 += 1
                elif number == "monster09.png":
                    num9 += 1
                elif number == "monster10.png":
                    num10 += 1

        writeScore(number, fireCount)
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