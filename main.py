import pygame

MINED, NOT_MINED, EXPLORED = range(3)

GRID_WIDTH = 40
GRID_HEIGHT = 40

class Board:
    def __init__(self, size):
        self.size = size
        self.mine_grids = [[NOT_MINED for _ in range(size)] for _ in range(size)]
        self.flag_grids = [[False for _ in range(size)] for _ in range(size)]

    def _pos_to_xy(self, pos):
        x = pos[0] / GRID_WIDTH
        y = pos[1] / GRID_HEIGHT

        print pos, GRID_WIDTH, GRID_HEIGHT, (x, y)
        return (x, y)

    def flag(self, pos):
        x, y = self._pos_to_xy(pos)
        self.flag_grids[x][y] = True

    def stamp(self, pos):
        x, y = self._pos_to_xy(pos)
        self.mine_grids[x][y] = EXPLORED

    def draw(self, screen):
        for x in range(self.size):
            for y in range(self.size):
                color = (255, 0, 0) if self.flag_grids[x][y] else (0, 255, 0)
                pygame.draw.rect(screen, color, pygame.Rect(x * GRID_WIDTH, y * GRID_HEIGHT, GRID_WIDTH, GRID_HEIGHT), 2)


def main():
    screen = pygame.display.set_mode((400, 400))

    board = Board(10)

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        pos = pygame.mouse.get_pos()
        button1_pressed, button2_pressed, button3_pressed = pygame.mouse.get_pressed()

        if button1_pressed:
            print 'button 1 pressed'
            board.stamp(pos)

        if button3_pressed:
            print 'button 3 pressed'
            board.flag(pos)

        screen.fill((128, 128, 128))
        board.draw(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()

