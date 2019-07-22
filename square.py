import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game')

x = 0
y = 0
width = 40
height = 40
velocity = 5

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= velocity:
        x -= velocity

    if keys[pygame.K_RIGHT] and x <= SCREEN_WIDTH - width - velocity:
        x += velocity

    if keys[pygame.K_UP] and y > velocity:
        y -= velocity

    if keys[pygame.K_DOWN] and y <= SCREEN_HEIGHT - height - velocity:
        y += velocity

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    # pygame.display.update()
    pygame.display.flip()

pygame.quit()