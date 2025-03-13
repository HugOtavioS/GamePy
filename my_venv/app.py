import pygame
import time
import math
import random

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

x = screen_width / 2
y = screen_height / 2

person_size = 50
person_pos_x = x
person_pos_y = y

# Armazena os quantro pontos do jogador (no caso um quadrado)
person = {
    "p1": [person_pos_x, person_pos_y],
    "p2": [person_pos_x + person_size, person_pos_y],
    "p3": [person_pos_x + person_size, person_pos_y + person_size],
    "p4": [person_pos_x, person_pos_y + person_size]
}
person_speed = 1

pressed_key = 0 # Variável que armazena o último evento de tecla pressionada (KEYDOWN ou KEYUP)
events = {}

foodGrow_size = 10
foodGrow_vector = {}
foodGrow_Qtd = 3

for f in range(0, foodGrow_Qtd):
    foodGrowx = random.randint(0, screen_width)
    foodGrowy = random.randint(0, screen_height)

    foodGrow_vector["f" + str(f)] = {
        "pos": [foodGrowx, foodGrowy], # Armazena a posição da comida
        # "c": False, # Variável que armazena se a comida foi comida ou não
        "vector": { # Armazena os quatro pontos do quadrado da comida
            "p1": [foodGrowx, foodGrowy],
            "p2": [foodGrowx + foodGrow_size, foodGrowy],
            "p3": [foodGrowx + foodGrow_size, foodGrowy + foodGrow_size],
            "p4": [foodGrowx, foodGrowy + foodGrow_size]
        }
    }

food_size = 10
food_vector = {}
food_Qtd = 3

for f in range(0, food_Qtd):
    foodx = random.randint(0, screen_width)
    foody = random.randint(0, screen_height)

    food_vector["f" + str(f)] = {
        "pos": [foodx, foody], # Armazena a posição da comida
        "vector": { # Armazena os quatro pontos do quadrado da comida
            "p1": [foodx, foody],
            "p2": [foodx + food_size, foody],
            "p3": [foodx + food_size, foody + food_size],
            "p4": [foodx, foody + food_size]
        }
    }

while running:

    for event in pygame.event.get():
        # Atribue qualquer tipo de evento do pygame
        pressed_key = event.type

        #  Verifica se o evento é de tecla pressionada ou solta e armazena no dicionário de eventos
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            events[pygame.key.name(event.key)] = event.key

            if event.key == pygame.K_ESCAPE:
                running = False

        # Verifica se o evento é de fechar a janela
        if event.type == pygame.QUIT:
            running = False

    # Verifica se o jogador colidiu com a comida verde
    for f in food_vector:
        if (person["p1"][0] < food_vector[f]["vector"]["p1"][0] + food_size and
            person["p1"][0] + person_size > food_vector[f]["vector"]["p1"][0] and
            person["p1"][1] < food_vector[f]["vector"]["p1"][1] + food_size and
            person["p1"][1] + person_size > food_vector[f]["vector"]["p1"][1]
        ):
            # Verifica a tecla pressionada e atualiza a posição do jogador
            if "up" in events:
                person_pos_y += person_speed
            if "down" in events:
                person_pos_y -= person_speed
            if "left" in events:
                person_pos_x += person_speed
            if "right" in events:
                person_pos_x -= person_speed
    
    # Verifica se o jogador colidiu com a comida vermelha
    for fg in foodGrow_vector:
        if (person["p1"][0] < foodGrow_vector[fg]["vector"]["p1"][0] + foodGrow_size and
            person["p1"][0] + person_size > foodGrow_vector[fg]["vector"]["p1"][0] and
            person["p1"][1] < foodGrow_vector[fg]["vector"]["p1"][1] + foodGrow_size and
            person["p1"][1] + person_size > foodGrow_vector[fg]["vector"]["p1"][1]
            # foodGrow_vector[fg]["c"] == False
        ):
            person_size += 5

            foodGrowx = random.randint(0, screen_width)
            foodGrowy = random.randint(0, screen_height)

            # Atualiza a posição da comida vermelha que foi comida/colidida
            foodGrow_vector[fg]["pos"] = [foodGrowx, foodGrowy]
            foodGrow_vector[fg]["vector"]["p1"] = [foodGrowx, foodGrowy]
            foodGrow_vector[fg]["vector"]["p2"] = [foodGrowx + foodGrow_size, foodGrowy]
            foodGrow_vector[fg]["vector"]["p3"] = [foodGrowx + foodGrow_size, foodGrowy + foodGrow_size]
            foodGrow_vector[fg]["vector"]["p4"] = [foodGrowx, foodGrowy + foodGrow_size]

    
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

    # Verifica se alguma tecla foi solta. Se ela corresponder a última tecla apertada, a remove do dicionário de eventos
    if pressed_key == pygame.KEYUP:
        for e in events:
            if events[e] == event.key:
                del events[e]
                break

    # Movimenta efetivamente o jogador e atualiza sua posição
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

    for i in foodGrow_vector:
        pygame.draw.rect(screen, (255, 0, 0), (foodGrow_vector[i]["pos"][0], foodGrow_vector[i]["pos"][1], foodGrow_size, foodGrow_size))

    clock.tick(120)

    pygame.display.flip()