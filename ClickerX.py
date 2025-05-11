import pygame
import sys
from random import randint
pygame.init()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, scale1, scale2):
        super().__init__()
        self.height = scale1
        self.width = scale2
        self.image = pygame.transform.scale(pygame.image.load(player_image), (self.height, self.width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    

class Click(GameSprite):
    def update(self):
        if self.rect.y <= 600:
            self.rect.y -= self.speed
        elif self.rect.y >= 0:
            self.kill()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("КликерX")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

background = pygame.image.load("Zhdun.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

font = pygame.font.SysFont('Arial', 50)




clicks = 0
pygame.mouse.set_visible(False) 
running = True
points = pygame.sprite.Group()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicks += 1
            point = ("ZhdunXclick.png",event.pos[0] ,event.pos[1],1, 10, 10 )
            points.add(point)
            
    screen.blit(background, (0, 0))

    text = font.render(f"Кликов: {clicks}", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH//2, 50))
    
    points.update()
    text_bg = pygame.Surface((text_rect.width + 20, text_rect.height + 10))
    text_bg.set_alpha(180) 
    text_bg.fill(WHITE)
    screen.blit(text_bg, (text_rect.x - 10, text_rect.y - 5))
    
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()