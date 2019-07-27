import pygame
import sys
from pygame.locals import *
import random

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
)

def create_vertices(max_distance):
    x_value_change = random.randrange(-10, 10)
    y_value_change = random.randrange(-10, 10)
    z_value_change = random.randrange(-1 * max_distance, -20)

    new_vertices = tuple((v[0] + x_value_change, v[1] + y_value_change, v[2] + z_value_change) for v in vertices)

    return new_vertices

def draw_cube(vertices):
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            #glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                     DOUBLEBUF | OPENGL)

    gluPerspective(45, (SCREEN_WIDTH * 1.0/ SCREEN_HEIGHT), 0.1, 50.0)

    #glTranslatef(0.0, 0.0, -10)
    glTranslatef(random.randrange(-5, 5), 0.0, -30)

    #glRotatef(20, 0, 0, 0)

    cube_passed = False
    x_move = 0
    y_move = 0

    all_cubes = []

    for x in range(75):
        all_cubes.append(create_vertices(50))

    while not cube_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -0.5
                if event.key == pygame.K_RIGHT:
                    x_move = 0.5
                if event.key == pygame.K_UP:
                    y_move = 0.5
                if event.key == pygame.K_DOWN:
                    y_move = -0.5

            if event.type == pygame.KEYUP:
                if event.key in {pygame.K_LEFT, pygame.K_RIGHT}:
                    x_move = 0
                if event.key in {pygame.K_UP, pygame.K_DOWN}:
                    y_move = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                button1, button2, button3 = pygame.mouse.get_pressed()
                if button1:
                    glTranslatef(0, 0, 1.0)
                if button3:
                    glTranslatef(0, 0, -1.0)


        #glRotate(1, 3, 1, 1)

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        #[camera_x, camera_y, camera_z] = x[3]
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        # slowly move
        glTranslatef(x_move, y_move, 0.2)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for cube_vertices in all_cubes:
            draw_cube(cube_vertices)

        pygame.display.flip()
        #pygame.display.update() # update doesn't work for OpenGL:w

        if camera_z <= 0:
            cube_passed = True

        pygame.time.wait(10)


if __name__ == '__main__':
    for _ in range(1000):
        main()



