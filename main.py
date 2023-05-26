import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()


class Food:
    def __init__(self, x, y, w, h, filename, ):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self, screen):
        screen.blit(self.png, [self.rect.x, self.rect.y])


class Snail:
    def __init__(self, x, y, w, h, filename, speedX, speedY):
        self.png = pygame.image.load(filename)
        self.rect = pygame.Rect(x, y, w, h)
        self.speedX = speedX
        self.speedY = speedY

    def draw(self, screen):
        screen.blit(self.png, [self.rect.x, self.rect.y])


snail2 = Snail(100, 0, 50, 50, "snail.png", 0, 0)

kapusta = Food(100, 0, 50, 50, "kapusta3.png")

ochku = 0
ochkuLable = pygame.font.Font(None, 38).render("Рахунок: " + str(ochku), True, (100, 100, 100))

winLable = pygame.font.Font(None, 100).render("ТИ ПЕРЕМІГ!", True, (100, 100, 100))

while True:

    if snail2.rect.colliderect(kapusta.rect):
        ochku += 1
        ochkuLable = pygame.font.Font(None, 38).render("Рахунок: " + str(ochku), True, (100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                snail2.speedY = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                snail2.speedY = -5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                snail2.speedX = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                snail2.speedX = 5

    if ochku == 2:
        screen.blit(winLable, [100, 100])
        pygame.display.flip()
        break

    if snail2.rect.colliderect(kapusta.rect):
        kapusta.rect.x = random.randint(0, 400)
        kapusta.rect.y = random.randint(0, 400)

    snail2.rect.x += snail2.speedX
    snail2.rect.y += snail2.speedY
    if snail2.rect.x > 500:
        snail2.speedX *= 0
    if snail2.rect.y > -500:
        snail2.speedY *= 0

    if snail2.rect.x > -500:
        snail2.speedX *= 0
    if snail2.rect.y > 500:
        snail2.speedY *= 0

    screen.fill((0, 160, 0))
    snail2.draw(screen)

    screen.blit(ochkuLable, [200, 0])
    kapusta.draw(screen)
    pygame.display.flip()
    fps.tick(60)
