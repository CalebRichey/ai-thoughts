import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the snake
snake = [(200, 200), (220, 200), (240, 200)]
direction = "right"

# Set up the food
food = (400, 300)

# Set up the score
score = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!= "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction!= "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction!= "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction!= "left":
                direction = "right"

    # Move the snake
    head = snake[-1]
    if direction == "up":
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == "down":
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == "left":
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == "right":
        new_head = (head[0] + BLOCK_SIZE, head[1])

    snake.append(new_head)

    # Check for collision with food
    if snake[-1] == food:
        score += 1
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop(0)

    # Check for collision with wall or self
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
            snake[-1] in snake[:-1]):
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    for x, y in snake:
        pygame.draw.rect(screen, WHITE, (x, y, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.Clock().tick(SPEED)
