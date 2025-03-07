import pygame
import time
import math
import random

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

x = screen_width / 2
y = screen_height / 2

person_size = 50
person_pos_x = x
person_pos_y = y
person = {
    "p1": [person_pos_x, person_pos_y],
    "p2": [person_pos_x + person_size, person_pos_y],
    "p3": [person_pos_x + person_size, person_pos_y + person_size],
    "p4": [person_pos_x, person_pos_y + person_size]
}
person_speed = 1

pressed_key = 0
events = {}

foodx = random.randint(0, screen_width)
foody = random.randint(0, screen_height)
food_size = 10
food = {
    "p1": [foodx, foody],
    "p2": [foodx + food_size, foody],
    "p3": [foodx + food_size, foody + food_size],
    "p4": [foodx, foody + food_size]
}

while running:
    for event in pygame.event.get():
        pressed_key = event.type

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            events[pygame.key.name(event.key)] = event.key

            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.QUIT:
            running = False
    
    if "up" in events:
        person_pos_y -= person_speed
    if "down" in events:
        person_pos_y += person_speed
    if "left" in events:
        person_pos_x -= person_speed
    if "right" in events:
        person_pos_x += person_speed
    
    if person_pos_y < 0 or (person_pos_y + person_size) > screen_height or person_pos_x < 0 or (person_pos_x + person_size) > screen_width:
        if "up" in events:
            person_pos_y += person_speed
        if "down" in events:
            person_pos_y -= person_speed
        if "left" in events:
            person_pos_x += person_speed
        if "right" in events:
            person_pos_x -= person_speed

    if pressed_key == pygame.KEYUP:
        for e in events:
            if events[e] == event.key:
                del events[e]
                break

    if (person["p1"][0] < food["p1"][0] + food_size and
        person["p1"][0] + person_size > food["p1"][0] and
        person["p1"][1] < food["p1"][1] + food_size and
        person["p1"][1] + person_size > food["p1"][1]
    ):
        foodx = random.randint(0, screen_width)
        foody = random.randint(0, screen_height)

    person["p1"] = [person_pos_x, person_pos_y]
    person["p2"] = [person_pos_x + person_size, person_pos_y]
    person["p3"] = [person_pos_x + person_size, person_pos_y + person_size]
    person["p4"] = [person_pos_x, person_pos_y + person_size]

    food["p1"] = [foodx, foody]
    food["p2"] = [foodx + food_size, foody]
    food["p3"] = [foodx + food_size, foody + food_size]
    food["p4"] = [foodx, foody + food_size]

    screen.fill((100, 100, 100))
    pygame.draw.rect(screen, (200, 200, 200), (person_pos_x, person_pos_y, person_size, person_size))
    pygame.draw.rect(screen, (255, 0, 0), (foodx, foody, food_size, food_size))

    clock.tick(120)

    pygame.display.flip()