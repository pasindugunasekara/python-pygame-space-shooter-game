import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 700))

background = pygame.image.load("assests/background.png")

pygame.display.set_caption("shooter space")
icon = pygame.image.load('assests/launchpad.png')
pygame.display.set_icon(icon)

shooterImg = pygame.image.load('assests/rocket (2).png')
shooterX = 370
shooterY = 610
shooterX_change = 0

aleanImg = []
aleanX = []
aleanY = []
aleanX_change = []
aleanY_change = []
countof_alean = 7

for i in range(countof_alean):
    aleanImg.append(pygame.image.load('assests/enemy.png'))
    aleanX.append(random.randint(0, 700))
    aleanY.append(random.randint(50, 170))
    aleanX_change.append(0.5)
    aleanY_change.append(40)

bulletImg = pygame.image.load('assests/bullet.png')
bulletX = 0
bulletY = 570
bulletX_change = 0
bulletY_change = 3
bullet_state = "ready"
score = 0


def shooter(x, y):
    screen.blit(shooterImg, (x, y))


def alean(x, y, i):
    screen.blit(aleanImg[i], (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))


def Collision(aleanX, aleanY, bulletX, bulletY):
    distance = math.sqrt((math.pow(aleanX - bulletX, 2)) + (math.pow(aleanY - bulletY, 2)))
    if distance < 30:
        return True
    else:
        return False


run = True
while run:

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shooterX_change = -0.8
            if event.key == pygame.K_RIGHT:
                shooterX_change = 0.8
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = shooterX
                    bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                shooterX_change = 0

    shooterX += shooterX_change

    if shooterX <= 0:
        shooterX = 0
    elif shooterX >= 740:
        shooterX = 740

    for i in range(countof_alean):
        aleanX[i] += aleanX_change[i]
        if aleanX[i] <= 0:
            aleanX_change[i] = 0.6
            aleanY[i] += aleanY_change[i]
        elif aleanX[i] >= 740:
            aleanX_change[i] = -0.6
            aleanY[i] += aleanY_change[i]

        collision = Collision(aleanX[i], aleanY[i], bulletX, bulletY)
        if collision:
            bulletY = 490
            bullet_state = "ready"
            score += 1
            print(score)
            aleanX[i] = random.randint(0, 700)
            aleanY[i] = random.randint(50, 170)

        alean(aleanX[i], aleanY[i] , i)

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    shooter(shooterX, shooterY)

    pygame.display.update()
