import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock-Paper-Scissors Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
rock_img = pygame.image.load("rock.png")
paper_img = pygame.image.load("paper.png")
scissors_img = pygame.image.load("scissors.png")

# Resize images
rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissors_img = pygame.transform.scale(scissors_img, (150, 150))

# Positions
rock_rect = rock_img.get_rect(topleft=(50, 100))
paper_rect = paper_img.get_rect(topleft=(225, 100))
scissors_rect = scissors_img.get_rect(topleft=(400, 100))

# Game options
options = ["rock", "paper", "scissors"]
font = pygame.font.Font(None, 36)
result = ""

def display_message(message):
    """Display game results."""
    text = font.render(message, True, BLACK)
    screen.blit(text, (200, 300))

running = True
while running:
    screen.fill(WHITE)

    # Draw choices
    screen.blit(rock_img, rock_rect.topleft)
    screen.blit(paper_img, paper_rect.topleft)
    screen.blit(scissors_img, scissors_rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            # Detect user selection
            if rock_rect.collidepoint(x, y):
                user_choice = "rock"
            elif paper_rect.collidepoint(x, y):
                user_choice = "paper"
            elif scissors_rect.collidepoint(x, y):
                user_choice = "scissors"
            else:
                continue

            # Computer choice
            computer_choice = random.choice(options)

            # Determine winner
            if user_choice == computer_choice:
                result = f"Computer: {computer_choice} | It's a tie!"
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                result = f"Computer: {computer_choice} | You win!"
            else:
                result = f"Computer: {computer_choice} | Computer wins!"

    # Display result
    display_message(result)
    pygame.display.update()

pygame.quit()