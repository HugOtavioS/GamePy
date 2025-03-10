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

food_size = 10
food_vector = {}
for f in range(0, 3):
    foodx = random.randint(0, screen_width)
    foody = random.randint(0, screen_height)
    food_vector["f" + str(f)] = {
        "pos": [foodx, foody],
        "vector": {
            "p1": [foodx, foody],
            "p2": [foodx + food_size, foody],
            "p3": [foodx + food_size, foody + food_size],
            "p4": [foodx, foody + food_size]
        }
    }
food = {
    "p1": [foodx, foody],
    "p2": [foodx + food_size, foody],
    "p3": [foodx + food_size, foody + food_size],
    "p4": [foodx, foody + food_size]
}

while running:
    for event in pygame.event.get():
        pressed_key = event.type

        # Verifica e adiciona os eventos de apertar e soltar teclas e armazena num dicionário
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            events[pygame.key.name(event.key)] = event.key

            if event.key == pygame.K_ESCAPE:
                running = False

        # Verifica se o evento é de fechar a janela
        if event.type == pygame.QUIT:
            running = False

    # Verifica a posição das comidas e movimenta o jogador
    for f in food_vector:
        if (person["p1"][0] < food_vector[f]["vector"]["p1"][0] + food_size and
            person["p1"][0] + person_size > food_vector[f]["vector"]["p1"][0] and
            person["p1"][1] < food_vector[f]["vector"]["p1"][1] + food_size and
            person["p1"][1] + person_size > food_vector[f]["vector"]["p1"][1]
        ):
            if "up" in events:
                person_pos_y += person_speed
            if "down" in events:
                person_pos_y -= person_speed
            if "left" in events:
                person_pos_x += person_speed
            if "right" in events:
                person_pos_x -= person_speed
    
    #Verifica se o jogador atingiu ou passou dos limites da tela
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

    # Movimenta a atualiza a posição do jogador
    if "up" in events:
        person_pos_y -= person_speed
    if "down" in events:
        person_pos_y += person_speed
    if "left" in events:
        person_pos_x -= person_speed
    if "right" in events:
        person_pos_x += person_speed

    # Atualiza os dados da posição do jogador
    person["p1"] = [person_pos_x, person_pos_y]
    person["p2"] = [person_pos_x + person_size, person_pos_y]
    person["p3"] = [person_pos_x + person_size, person_pos_y + person_size]
    person["p4"] = [person_pos_x, person_pos_y + person_size]

    # Preenche a tela com a cor de fundo
    screen.fill((100, 100, 100))

    # Desenha o jogador
    pygame.draw.rect(screen, (200, 200, 200), (person_pos_x, person_pos_y, person_size, person_size))

    # Desenha a(s) comida(s)
    for i in food_vector:
        pygame.draw.rect(screen, (0, 255, 0), (food_vector[i]["pos"][0], food_vector[i]["pos"][1], food_size, food_size))

    # Inicializando Fontes e renderizando na tela
    # pygame.font.init()
    # font = pygame.font.SysFont("Arial", 20)
    # text = font.render("Hello World!", True, (255, 255, 255))
    # screen.blit(text, (0, 0))

    clock.tick(120)

    pygame.display.flip()