import pygame # Import the pygame library
import time # Import the time library

pygame.init() # Initialize the pygame library

screen_width = 500 # Set the screen width
screen_height = 500 # Set the screen height
screen = pygame.display.set_mode((screen_width, screen_height)) # Create a window
pygame.time.Clock().tick(2) # Set the clock
running = True # Set the running variable to True

x = screen_width / 2 # Set the x position
y = screen_height / 2 # Set the y position

person_pos_x = x
person_pos_y = y
pressed_key = 0

while running: # While running is True
    for event in pygame.event.get(): # For each event in the event queue
        pressed_key = event.type
        if event.type == pygame.QUIT: # If the event is a quit event
            running = False # Set running to False

    if pressed_key == pygame.KEYDOWN:
        if event.key == pygame.K_UP: # If the event is a quit event
            person_pos_y -= 0.1 # Move the person up
        elif event.key == pygame.K_DOWN: # If the event is a quit event
            person_pos_y += 0.1 # Move the person down
        elif event.key == pygame.K_LEFT: # If the event is a quit event
            person_pos_x -= 0.1 # Move the person left
        elif event.key == pygame.K_RIGHT: # If the event is a quit event
            person_pos_x += 0.1 # Move the person right

    if person_pos_y < 0 or (person_pos_y + 50) > screen_height or person_pos_x < 0 or (person_pos_x + 50) > screen_width: # If the person is out of bounds
        print("You lost!") # Print "You lost!"

    screen.fill((100, 100, 100)) # Fill the screen with a gray color
    pygame.draw.rect(screen, (200, 200, 200), (person_pos_x, person_pos_y, 50, 50)) # Draw a rectangle

    pygame.display.flip() # Update the screen