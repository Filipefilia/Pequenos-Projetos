import pygame
import random

# Configurações da interface do jogo
WIDTH = 600
HEIGHT = 400
GRID_SIZE = 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Inicializa a interface vazia
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobra Simples")
clock = pygame.time.Clock()


# Classe responsável pela cobrinha
class Snake:

    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = (GRID_SIZE, 0)

    def move(self):
        head = (self.body[0][0] + self.direction[0],
                self.body[0][1] + self.direction[1])
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:] or head[0] < 0 or head[
            0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, WHITE, (*segment, GRID_SIZE, GRID_SIZE))


# Classe responsável pela comida
class Food:

    def __init__(self):
        self.position = (random.randrange(0, WIDTH, GRID_SIZE),
                         random.randrange(0, HEIGHT, GRID_SIZE))

    def respawn(self):
        self.position = (random.randrange(0, WIDTH, GRID_SIZE),
                         random.randrange(0, HEIGHT, GRID_SIZE))

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, GRID_SIZE, GRID_SIZE))


# Função para exibir a tela de Game Over
def game_over():
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Pressione R para Reiniciar", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False


# Função que controla o funcionamento do jogo
def main():
    while True:
        snake = Snake()
        food = Food()
        running = True

        while running:
            screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and snake.direction != (
                            0, GRID_SIZE):
                        snake.direction = (0, -GRID_SIZE)
                    elif event.key == pygame.K_DOWN and snake.direction != (
                            0, -GRID_SIZE):
                        snake.direction = (0, GRID_SIZE)
                    elif event.key == pygame.K_LEFT and snake.direction != (
                            GRID_SIZE, 0):
                        snake.direction = (-GRID_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and snake.direction != (
                            -GRID_SIZE, 0):
                        snake.direction = (GRID_SIZE, 0)

            snake.move()

            if snake.body[0] == food.position:
                snake.grow()
                food.respawn()

            if snake.check_collision():
                running = False

            snake.draw(screen)
            food.draw(screen)
            pygame.display.flip()
            clock.tick(10)

        game_over()


main()
