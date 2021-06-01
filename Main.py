import pygame
from pygame.locals import *
import time
import random

SIZE = 16
Score = 0
BACK = (162, 255, 0)


class Aple:
    Player_Score = 0

    def __init__(self, parent_sc):
        self.parent_sc = parent_sc
        self.x = SIZE * random.randint(1, 30)
        self.y = SIZE * random.randint(1, 30)
        self.image = pygame.image.load("pineapple.jpg")

    def draw_apple(self):
        self.parent_sc.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 30) * SIZE
        self.y = random.randint(1, 30) * SIZE


class Snake:
    def increase_length(self):
        self.length += 1
        self.x.append(+1)
        self.y.append(+1)

    def __init__(self, parent_sc, length):
        self.length = length
        self.parent_sc = parent_sc
        self.block = pygame.image.load("blocks.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def draw(self):
        self.parent_sc.fill(BACK)
        for i in range(self.length):
            self.parent_sc.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def left(self):
        self.direction = 'left'

    def right(self):
        self.direction = 'right'

    def up(self):
        self.direction = 'up'

    def down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'down':
            self.y[0] += 16
        if self.direction == 'up':
            self.y[0] -= 16
        if self.direction == 'right':
            self.x[0] += 16
        if self.direction == 'left':
            self.x[0] -= 16

        self.draw()


class GM:
    def ab(self):
        self.snake.walk()
        self.apple.draw_apple()

        self.score()
        pygame.display.flip()

    def __init__(self):
        self.a = 0
        pygame.init()
        pygame.display.set_caption("SNAKE GAME")
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Aple(self.surface)
        self.apple.draw_apple()

    def score(self):
        font = pygame.font.SysFont('arial', 14)
        score = font.render(f"Score:{self.a}", True, (8, 0, 255))
        self.surface.blit(score, (10, 10))

    def run(self):
        pygame.display.flip()

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.up()

                    if event.key == K_DOWN:
                        self.snake.down()

                    if event.key == K_LEFT:
                        self.snake.left()

                    if event.key == K_RIGHT:
                        self.snake.right()

                elif event.type == QUIT:

                    running = False

            self.ab()
            time.sleep(0.2)

            if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                self.snake.increase_length()
                self.apple.move()
                self.a += 1

    def is_collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False


if __name__ == "__main__":
    game = GM()
    game.run()
