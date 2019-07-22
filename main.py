import pygame, random
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLOR_WHITE = (255, 255, 255)

def load_image(image_path):
    image = pygame.image.load('./dino.png').convert()
    return image, image.get_rect()


class DinoStatus(Enum):
    Running = 1
    Jumping = 2
    Dropping = 3

class Dino(pygame.sprite.Sprite):
    MIN_TOP = 150
    SPRITE_SIZE = 80
    JUMP_SPEED = 10

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.transform.scale(pygame.image.load('./wario.png'), (Dino.SPRITE_SIZE, Dino.SPRITE_SIZE))
        #image.set_colorkey(image.get_at((1, 1)))
        self.image = image

        self.rect = self.image.get_rect()
        self.init_y = SCREEN_HEIGHT/2 - self.rect.height
        self.rect.move_ip(200, self.init_y)


        self.status = DinoStatus.Running
        self.altitude = 0

    def update(self):
        if self.status == DinoStatus.Running:
            pass
        elif self.status == DinoStatus.Jumping:
            if self.rect.top <= Dino.MIN_TOP:
                self.drop()
            else:
                self.rect.move_ip(0, -Dino.JUMP_SPEED)
        else: # Dropping
             if self.rect.top >= self.init_y:
                self.run()
             else:
                self.rect.move_ip(0, Dino.JUMP_SPEED)


    def jump(self):
        if self.status == DinoStatus.Running:
            self.status = DinoStatus.Jumping

    def drop(self):
        if self.status == DinoStatus.Jumping:
            self.status = DinoStatus.Dropping

    def run(self):
         if self.status == DinoStatus.Dropping:
            self.status = DinoStatus.Running

class Turtle(pygame.sprite.Sprite):
    SIZE = 30

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load('./turtle.png')
        image = pygame.transform.scale(image, (Turtle.SIZE, Turtle.SIZE))
        self.image = image

        rect = self.image.get_rect().move(SCREEN_WIDTH, SCREEN_HEIGHT/2 - Turtle.SIZE)
        self.rect = rect


    def update(self):
        self.rect.move_ip(-10, 0)

    def is_over(self):
        return self.rect.left < 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(COLOR_WHITE)

    clock = pygame.time.Clock()
    dino = Dino()
    mario = pygame.sprite.RenderPlain((dino))

    #all_sprites.add(Turtle())
    all_turtles = pygame.sprite.RenderPlain()

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                dino.jump()

        screen.fill(COLOR_WHITE)
        pygame.draw.line(screen, (0,0,0), (0, SCREEN_HEIGHT/2), (SCREEN_WIDTH, SCREEN_HEIGHT/2), 2)

        if random.randint(0, 50) < 1:
            all_turtles.add(Turtle())

        for sprite in all_turtles:
            if sprite.is_over():
                all_turtles.remove(sprite)

        mario.update()
        mario.draw(screen)

        all_turtles.update()
        all_turtles.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()


