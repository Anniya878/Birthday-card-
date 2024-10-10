import pygame
import time
pygame.init()
screen = pygame.display.set_mode((700, 700))
bg = pygame.image.load("background.jpg") 
bg = pygame.transform.scale(bg, (700 ,700))
cake = pygame.image.load("cake.jpg")
cake = pygame.transform.scale(cake, (700,700))
box = pygame.image.load("present.jpg")
box = pygame.transform.scale(box, (700,700))
font = pygame.font.SysFont("forte", 50)
text_font = font.render("Happy Birthday!", True, (14, 119, 176))
text_font1 = font.render("Have a great day!", True, (206, 87, 242))
text_font2 = font.render("Here's your gift!", True, (11, 135, 27))
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("light pink")
    screen.blit(bg, (0,0))
    screen.blit(text_font, (200,350))
    pygame.display.update()
    time.sleep(3)
    screen.blit(cake, (0,0))
    screen.blit(text_font1, (400,100))
    pygame.display.update()
    time.sleep(3)
    screen.blit(box, (0,0))
    screen.blit(text_font2, (400,100))
    pygame.display.update()
    time.sleep(3)

    