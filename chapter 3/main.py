import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display size
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20  # Size of each grid cell

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  # Snake color
RED = (213, 50, 80)  # Food color
BLUE = (50, 153, 213)  # Background color

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control speed
clock = pygame.time.Clock()

def draw_snake(snake):
    """Draw the snake on the screen."""
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    """Draw the food on the screen."""
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

def draw_score(score):
    """Display the current score on the screen."""
    font = pygame.font.SysFont(None, 35)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])

def game_over():
    """Display Game Over screen and wait for user input to restart or quit."""
    screen.fill(BLUE)
    font = pygame.font.SysFont(None, 35)
    text = font.render("Game Over! Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(text, [WIDTH // 10, HEIGHT // 3])
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()  # Restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()

def main():
    """Main game loop."""
    snake = [(WIDTH // 2, HEIGHT // 2)]  # Reset snake
    snake_direction = (CELL_SIZE, 0)  # Reset direction
    food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE, 
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
    score = 0  # Reset score
    running = True
    
    while running:
        screen.fill(BLUE)  # Fill the background
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, CELL_SIZE):
                    snake_direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -CELL_SIZE):
                    snake_direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and snake_direction != (CELL_SIZE, 0):
                    snake_direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-CELL_SIZE, 0):
                    snake_direction = (CELL_SIZE, 0)
        
        # Move the snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        
        # Check for collisions
        if new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            game_over()
            return  # Exit the function to restart if needed
        
        snake.insert(0, new_head)
        
        # Check if snake eats food
        if new_head == food:
            food = (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE, 
                    random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
            score += 10  # Increase score
        else:
            snake.pop()
        
        # Draw everything
        draw_snake(snake)
        draw_food(food)
        draw_score(score)
        pygame.display.flip()
        clock.tick(10)  # Control snake speed

if __name__ == "__main__":
    main()