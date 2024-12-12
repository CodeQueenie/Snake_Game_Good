import pygame
import random
from utils import log_error

class Game:
    """
    Game class to manage the Snake game logic and state.
    """

    def __init__(self, screen):
        """
        Initializes the Game with the given screen.

        Parameters
        ----------
        screen : pygame.Surface
            The screen surface where the game will be drawn.
        """
        self.screen = screen
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = pygame.K_RIGHT
        self.food = self.generate_food()
        self.score = 0
        self.level = 1
        self.speed = 10

    def handle_events(self):
        """
        Handles user input events such as key presses and window close events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    self.direction = event.key

    def update(self):
        """
        Updates the game state, including the snake's position and collision detection.
        """
        head = self.snake[0]
        if self.direction == pygame.K_UP:
            new_head = (head[0], head[1] - 10)
        elif self.direction == pygame.K_DOWN:
            new_head = (head[0], head[1] + 10)
        elif self.direction == pygame.K_LEFT:
            new_head = (head[0] - 10, head[1])
        elif self.direction == pygame.K_RIGHT:
            new_head = (head[0] + 10, head[1])
        
        self.snake = [new_head] + self.snake[:-1]
        
        if self.snake[0] == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.generate_food()
            self.score += 10
            if self.score % 50 == 0:
                self.level += 1
                self.speed += 2

        if self.snake[0] in self.snake[1:] or not (0 <= self.snake[0][0] < 800 and 0 <= self.snake[0][1] < 600):
            self.game_over()

    def draw(self):
        """
        Draws the game elements on the screen.
        """
        self.screen.fill((0, 0, 0))
        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (*segment, 10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, 10, 10))
        self.draw_text(f"Score: {self.score}", 10, 10)
        self.draw_text(f"Level: {self.level}", 10, 30)

    def generate_food(self):
        """
        Generates a new food item at a random position on the screen.

        Returns
        -------
        tuple
            The (x, y) coordinates of the new food item.
        """
        x = random.randint(0, self.screen.get_width() // 10 - 1) * 10
        y = random.randint(0, self.screen.get_height() // 10 - 1) * 10
        return (x, y)

    def draw_text(self, text, x, y):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, (255, 255, 255))
        self.screen.blit(text_surface, (x, y))

    def game_over(self):
        self.draw_text("Game Over", 400, 300)
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.quit()
        exit()
# Generated by Nicole LeGuern