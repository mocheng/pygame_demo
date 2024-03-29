import pygame, random
from enum import Enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

"""
color constants
"""
COLOR_BACKGROUND = (255, 255, 255)
COLOR_WARNING = (255, 0, 0)

"""
custom event
"""
class Event(Enum):
    ADD_TURTLE = pygame.USEREVENT + 1


class PlayerStatus(Enum):
    Running = 1
    Jumping = 2
    Dropping = 3


class Player(pygame.sprite.Sprite):
    """
    Player that is controlled by human.
    For the time being, the constume is wario.
    """
    MIN_TOP = 120
    SPRITE_SIZE = 80
    JUMP_SPEED = 10

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.transform.scale(pygame.image.load('./resources/wario.png'), (Player.SPRITE_SIZE, Player.SPRITE_SIZE))
        # image.set_colorkey(image.get_at((1, 1)))
        self.image = image

        self.rect = self.image.get_rect()
        self.init_y = SCREEN_HEIGHT/2 - self.rect.height
        self.rect.move_ip(200, self.init_y)

        self.status = PlayerStatus.Running
        self.altitude = 0

    def update(self):
        if self.status == PlayerStatus.Running:
            pass
        elif self.status == PlayerStatus.Jumping:
            if self.rect.top <= Player.MIN_TOP:
                self.drop()
            else:
                self.rect.move_ip(0, -Player.JUMP_SPEED)
        else:  # Dropping
            if self.rect.top >= self.init_y:
                self.run()
            else:
                self.rect.move_ip(0, Player.JUMP_SPEED)

    def jump(self):
        if self.status == PlayerStatus.Running:
            self.status = PlayerStatus.Jumping

    def drop(self):
        if self.status == PlayerStatus.Jumping:
            self.status = PlayerStatus.Dropping

    def run(self):
        if self.status == PlayerStatus.Dropping:
            self.status = PlayerStatus.Running


class Turtle(pygame.sprite.Sprite):
    SIZE = 30

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load('./resources/turtle.png')
        image = pygame.transform.scale(image, (Turtle.SIZE, Turtle.SIZE))
        self.image = image

        rect = self.image.get_rect().move(SCREEN_WIDTH, SCREEN_HEIGHT/2 - Turtle.SIZE)
        self.rect = rect

    def update(self):
        self.rect.move_ip(-10, 0)

    def is_over(self):
        return self.rect.left < 0


class Banner:
    """
    Banner to display game-over or other info.
    """
    def __init__(self):
        self.basic_font = pygame.font.SysFont(None, 48)
        self.display_count_down = 0

    def update(self):
        if self.display_count_down >= 0:
            self.display_count_down -= 1

    def draw(self, screen):
        if self.display_count_down >= 0:
            text = self.basic_font.render('You Crashed!', True, COLOR_WARNING)
            text_rect = text.get_rect()
            text_rect.centerx = screen.get_rect().centerx
            text_rect.centery = screen.get_rect().centery
            screen.blit(text, text_rect)

    def show(self):
        self.display_count_down = 10


def main():
    """main function of the game"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(COLOR_BACKGROUND)

    clock = pygame.time.Clock()
    player = Player()
    all_players = pygame.sprite.RenderPlain((player))

    all_turtles = pygame.sprite.RenderPlain()

    banner = Banner()

    pygame.time.set_timer(Event.ADD_TURTLE, 200)
    turtle_born_count_down = 0

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                player.jump()
            elif event.type == Event.ADD_TURTLE:
                if turtle_born_count_down == 0:
                    if random.randint(1, 5) < 2:
                        all_turtles.add(Turtle())
                        turtle_born_count_down = 3 # avoid turtles too close
                else:
                    turtle_born_count_down -= 1


        screen.fill(COLOR_BACKGROUND)
        pygame.draw.line(screen, (0,0,0), (0, SCREEN_HEIGHT/2), (SCREEN_WIDTH, SCREEN_HEIGHT/2), 2)

        for sprite in all_turtles:
            if sprite.is_over():
                all_turtles.remove(sprite)

        if pygame.sprite.spritecollideany(player, all_turtles):
            banner.show()

        all_players.update()
        all_players.draw(screen)

        all_turtles.update()
        all_turtles.draw(screen)

        banner.update()
        banner.draw(screen)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()


