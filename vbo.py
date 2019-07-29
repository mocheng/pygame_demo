import pygame
import sys
from pygame.locals import *
import random

from OpenGL.GL import *
from OpenGL.GLU import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.OPENGL)

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()


if __name__ == '__main__':
    main()
