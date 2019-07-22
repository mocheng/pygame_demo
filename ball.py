import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game')

speed_vector = [4, 3]

# convert method makes rendering faster
ball = pygame.image.load("./ball.gif").convert()
ball_rect = ball.get_rect()

screen.fill((255, 255, 255))

clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    original_rect = ball_rect
    ball_rect = ball_rect.move(speed_vector)

    if (ball_rect.left < 0) or ball_rect.right > SCREEN_WIDTH:
        speed_vector[0] = - speed_vector[0]

    if (ball_rect.top < 0) or ball_rect.bottom > SCREEN_HEIGHT:
        speed_vector[1] = - speed_vector[1]

    screen.fill((255, 255, 255))
    screen.blit(ball, ball_rect)
    #pygame.display.flip()
    #pygame.display.update(pygame.Rect.union(ball_rect, original_rect))
    pygame.display.update(ball_rect)


    #pygame.time.delay(16)

