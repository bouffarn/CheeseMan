#Name:  Nathan Bouffard
#Date:  5/3/2023
#Title: Cheese man cheese
#Description:   Don't get hit! Your goal is to avoid getting hit by using the 'W' and 'S' keys. You can also use 'R' to reset
import pygame
import random

# modules
import enemies
import player

# variables
x, y = size = (1280, 720)
passthrough = {"x": x, "y": y}
character = player.player(passthrough)
objects = []
running = True
inGame = True
lastSpawned = 0
startTime = 0
score = 0
# pygame
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Comis Sans MS', 75)
while running:
    # game loop variables
    time = pygame.time.get_ticks()
    if inGame:
        score = int((time - startTime) / 100)
    if lastSpawned + 1000 < time and inGame:
        lastSpawned = time
        if random.randint(1, 2) == 1:
            enemy = enemies.car(passthrough, time)
        else:
            enemy = enemies.plane(passthrough, time)
        objects.append(enemy)
    # game events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                character.duck(True)
            elif event.key == pygame.K_w:
                character.jump(time)
            elif event.key == pygame.K_r:
                objects = []
                lastSpawned = time
                startTime = time
                character.reset(passthrough)
                inGame = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                character.duck(False)
        elif event.type == pygame.QUIT:
            running = False
    # game logic
    character.tick(passthrough, time)
    for i, object in enumerate(objects):
        if object.tick(passthrough, time):
            objects.pop(i)
        if pygame.Rect.colliderect(pygame.Rect([object.position[0] - object.size[0] * object.origin[0], object.position[1] - object.size[1] * object.origin[1]], object.size), pygame.Rect([character.position[0] - character.size[0] * character.origin[0], character.position[1] - character.size[1] * character.origin[1]], character.size)):
            inGame = False
    # reset screen
    screen.fill((51, 153, 255))
    grass = pygame.Surface((x, y * 1/3))
    grass.fill((51, 204, 51))
    screen.blit(grass, [0, y * 2/3])
    # draw enemies
    for object in objects:
        screen.blit(object.image, [object.position[0] - object.size[0] * object.origin[0], object.position[1] - object.size[1] * object.origin[1]])
    # draw text
    scoreText = font.render('Score: ' + str(score), False, (255, 255, 255))
    if inGame:
        screen.blit(scoreText, (0, 0))
        # draw player
        screen.blit(character.image, [character.position[0] - character.size[0] * character.origin[0], character.position[1] - character.size[1] * character.origin[1]])
    else:
        gameOverText = font.render('Game Over', False, (255, 0, 0))
        screen.blit(gameOverText, (x / 2 - gameOverText.get_size()[0] / 2, y / 2 - gameOverText.get_size()[1]))
        screen.blit(scoreText, (x / 2 - scoreText.get_size()[0] / 2, y / 2))
    # display frame
    pygame.display.flip()
