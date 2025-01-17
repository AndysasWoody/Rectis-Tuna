import sys

import pygame
from random import randint
from classes import *

pygame.init()

WIDTH = 1280
HEIGHT = 720

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recti's Tuna")

text_font = pygame.font.SysFont('arialblack', 30)
text_inter_col = (255, 255, 255)
text_speech_col = (108, 183, 7)


def main():
    run = True
    player = KW()
    play_button = Button(((1180 / 2) - 200), ((620 / 2) - 100), 200, 75, (110, 32, 155))
    quit_button = Button(((1180 / 2) - 200), ((620 / 2) + 100), 200, 75, (110, 32, 155))

    while run:
        pygame.time.Clock().tick(10)
        for event in pygame.event.get():  # event handler
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        player.tick(keys)
        play_button.tick(keys, player)
        quit_button.tick(keys, player)

        if play_button.tick(keys, player):
            room()

        if quit_button.tick(keys, player):
            sys.exit()

        window.fill((2, 1, 37))
        play_button.draw()
        quit_button.draw()
        player.draw()
        draw_text("Recti's Tuna", text_font, (237, 34, 228), (WIDTH / 2) + 50, 50)
        draw_text('Play', text_font, text_inter_col, ((WIDTH / 2) - 200), ((HEIGHT / 2) - 140))
        draw_text('Quit', text_font, text_inter_col, ((WIDTH / 2) - 200), ((HEIGHT / 2) + 60))
        draw_text("Move: 'w', 's', 'a', 'd'", text_font, text_speech_col, (WIDTH / 2) + 50, (HEIGHT / 2) - 190)
        draw_text("Interact: 'e'", text_font, text_speech_col, (WIDTH / 2) + 50, (HEIGHT / 2) - 140)
        pygame.display.update()


def room():
    run = True
    player = KW()
    door_button = Button(((1180 / 2) - 200), 0, 200, 50, (79, 56, 22))
    bed_button = Button((1180 / 2), HEIGHT / 2 + 100, 400, 200, (174, 32, 50))
    pillow_button = Button(((1180 / 2) + 10), HEIGHT / 2 + 125, 100, 150, text_inter_col)

    while run:
        pygame.time.Clock().tick(10)
        for event in pygame.event.get():  # event handler
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        player.tick(keys)
        door_button.tick(keys, player)
        bed_button.tick(keys, player)

        if door_button.tick(keys, player):
            tuna_keep()

        if bed_button.tick(keys, player):
            dream()

        window.fill((2, 1, 37))
        door_button.draw()
        bed_button.draw()
        pillow_button.draw()
        player.draw()
        draw_text('Door', text_font, text_inter_col, ((WIDTH / 2) - 200), 0)
        draw_text('Bed', text_font, text_inter_col, ((1180 / 2) + 150), (HEIGHT / 2 + 150))
        draw_text("You're waking up in a room you've never been before", text_font, text_speech_col, 70, (HEIGHT / 2) - 190)
        draw_text("Let's take a nap", text_font, text_speech_col, 750, 400)
        draw_text("Where does this door lead to?", text_font, text_speech_col, 600, 0)
        pygame.display.update()


def dream():
    run = True
    player = KW()
    clock = 0
    score = 0
    collectibles = []
    while run:
        clock += pygame.time.Clock().tick(10)
        for event in pygame.event.get():  # event handler
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if clock >= 1000:
            clock = 0
            collectibles.append(Collectible())

        player.tick(keys)
        for collectible in collectibles:
            collectible.tick()

        window.fill((2, 1, 37))

        draw_text(f'Gathered: {score}/5', text_font, text_inter_col, 10, 0)

        for collectible in collectibles:
            if player.hitbox.colliderect(collectible.hitbox):
                collectibles.remove(collectible)
                score += 1

            while score >= 5:
                tuna_keep()

        player.draw()
        for collectible in collectibles:
            collectible.draw()
        draw_text("I gotta gather 'em all!!!!!", text_font, text_speech_col, 800, 500)

        pygame.display.update()


def tuna_keep():
    run = True
    player = KW()
    tuna_button = Button((1180 / 2), (620 / 2) - 200, 100, 20, (232, 104, 104))
    button_button = Button(1180, (620 / 2), 10, 10, (120, 114, 79))
    door_button = Button(((1180 / 2) - 200), 670, 200, 50, (79, 56, 22))
    while run:
        pygame.time.Clock().tick(10)
        for event in pygame.event.get():  # event handler
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        tuna_button.tick(keys, player)
        button_button.tick(keys, player)
        player.tick(keys)

        if button_button.tick(keys, player):
            long_journey()

        window.fill((2, 1, 37))
        tuna_button.draw()

        button_button.draw()
        door_button.draw()
        player.draw()
        draw_text('Tuna', text_font, text_inter_col, 1180 / 2, ((620 / 2) - 200))
        draw_text('Button', text_font, text_inter_col, 1180 - 50, ((620 / 2) - 50))
        draw_text('Door', text_font, text_inter_col, (1180 / 2) - 150, 670)
        draw_text("It's rotting, there's nothin' I can do", text_font, text_speech_col, 10, 20)
        draw_text('THE DOOR IS LOCKED!!! HOW?!', text_font, text_speech_col, 10, 500)
        draw_text("Oh, what is it doing?", text_font, text_speech_col, WIDTH - 500, HEIGHT - 400)
        pygame.display.update()


def long_journey():
    run = True
    player = KW()
    exit_button = Button((WIDTH / 3), (HEIGHT / 3) - 200, 300, 150, (42, 240, 144))

    while run:
        pygame.time.Clock().tick(10)
        for event in pygame.event.get():  # event handler
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        player.tick(keys)
        exit_button.tick(keys, player)
        if exit_button.tick(keys, player):
            main()

        window.fill((2, 1, 37))
        exit_button.draw()
        player.draw()
        draw_text('Bravo, the end', text_font, text_inter_col, 1180 / 2 + 200, (620 / 2) + 200)
        draw_text('Ye may leave!', text_font, text_inter_col, (WIDTH / 3), HEIGHT/3)
        pygame.display.update()


if __name__ == "__main__":
    main()
