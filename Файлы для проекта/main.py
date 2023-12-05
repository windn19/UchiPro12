import pygame

from pygame.colordict import THECOLORS

from life import Field

SCREEN_WIDTH = 800  # ширина окна
SCREEN_HEIGHT = 600  # высота окна
FIELD_WIDTH = 160  # ширина поля кратна ширине окна
FIELD_HEIGHT = 120  # высота поля кратна высоте окна
FPS = 10  # количество смен поколений в секунду

WHITE = THECOLORS['white']
GRAY = THECOLORS['gray']
BLACK = THECOLORS['black']


class GraphGame:
    def __init__(self, width, height, randomize=False):
        pygame.init()
        pygame.display.set_caption('Game of Life')
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.game_field = Field(
            width=width, height=height, randomize=randomize
        )
        self.cell_width = SCREEN_WIDTH // width
        self.cell_height = SCREEN_HEIGHT // height

    def set_figure(self, figure, row=None, col=None):
        self.game_field.set_figure(figure, row, col)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill(WHITE)
            self.draw()
            self.draw_lines()
            self.game_field.next_generation()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

    def draw_lines(self):
        for row in range(1, self.game_field.height):
            pygame.draw.line(
                self.screen,
                GRAY,
                (0, row * self.cell_height),
                (SCREEN_WIDTH, row * self.cell_height)
            )
        for col in range(1, self.game_field.width):
            pygame.draw.line(
                self.screen, GRAY,
                (col * self.cell_width, 0),
                (col * self.cell_width, SCREEN_HEIGHT))

    def draw(self):
        for row in range(self.game_field.height):
            for col in range(self.game_field.width):
                cell = self.game_field.field[row][col]
                if cell.is_alive:
                    color = BLACK
                    pygame.draw.rect(self.screen, color, (
                        col * self.cell_width,
                        row * self.cell_height,
                        self.cell_width,
                        self.cell_height))


if __name__ == '__main__':
    game = GraphGame(width=FIELD_WIDTH, height=FIELD_HEIGHT, randomize=True)
    # game = GraphGame(width=FIELD_WIDTH, height=FIELD_HEIGHT, randomize=True)
    # game.set_figure('r-pentamino')
    # game.set_figure('planner', row=5, col=5)
    game.run()
