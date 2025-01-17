import pygame
from random import randint

pygame.init()

WIDTH = 1280

HEIGHT = 720

window = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_text(text, font, text_colo, x, y):
    img = font.render(text, True, text_colo)
    window.blit(img, (x, y))


class KW:
    def __init__(self):
        self.speed = 50
        self.KW_width = 75
        self.KW_height = 75
        self.colour = (64, 20, 9)
        self.rect = pygame.Rect((WIDTH - self.KW_width) / 2, (HEIGHT - self.KW_height) / 2, self.KW_width, self.KW_height)
        self.hitbox = self.rect

    def tick(self, keys):
        if keys[pygame.K_w]:
            self.rect.y = max([self.rect.y - self.speed, 0])

        if keys[pygame.K_s]:
            self.rect.y = min([self.rect.y + self.speed, HEIGHT - self.KW_height])

        if keys[pygame.K_a]:
            self.rect.x = max([self.rect.x - self.speed, 0])

        if keys[pygame.K_d]:
            self.rect.x = min([self.rect.x + self.speed, WIDTH - self.KW_width])

        self.hitbox = self.rect

    def draw(self):
        pygame.draw.rect(window, self.colour, self.rect)


class Collectible:
    def __init__(self):
        self.collectible_x = 10
        self.collectible_y = 10
        self.x_cord = randint(0, (1280 - self.collectible_x))
        self.y_cord = randint(0, (720 - self.collectible_y))
        self.colour = (22, 111, 44)
        self.rect = pygame.Rect(self.x_cord, self.y_cord, self.collectible_x, self.collectible_y)
        self.hitbox = self.rect

    def tick(self):
        self.hitbox = self.rect

    def draw(self):
        pygame.draw.rect(window, self.colour, self.rect)


class Button:
    def __init__(self, x_cord, y_cord, x_lenght, y_lenght, colour):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.x_lenght = x_lenght
        self.y_lenght = y_lenght
        self.colour = colour
        self.rect = pygame.Rect(self.x_cord, self.y_cord, self.x_lenght, self.y_lenght)
        self.hitbox = self.rect

    def tick(self, keys, player):
        if self.hitbox.colliderect(player.hitbox):
            if keys[pygame.K_e]:
                return True

    def draw(self):
        pygame.draw.rect(window, self.colour, self.rect)


