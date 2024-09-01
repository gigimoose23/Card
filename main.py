import pygame
import time
WIDTH = 500
HEIGHT = 500
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Card")

cake = pygame.image.load("images/cake.jpg")
cake = pygame.transform.scale(cake, (WIDTH,HEIGHT))

caketin = pygame.image.load("images/caketin.jpg")
caketin = pygame.transform.scale(caketin, (WIDTH,HEIGHT))

bj = pygame.image.load("images/bj.jpg")
bj = pygame.transform.scale(bj, (WIDTH,HEIGHT))








while True:
    screen.fill("skyblue")
    screen.blit(cake, (0,0))
   
    
  
    time.sleep(2)
    font = pygame.font.SysFont("Times New Roman", 50)
    text1 = font.render("Happy Birthday", True, (0,0,0))
    screen.blit(text1, (50, 200))
    pygame.display.update()

    screen.fill("skyblue")
    screen.blit(caketin, (0,0))



    time.sleep(2)
    font = pygame.font.SysFont("Times New Roman", 50)
    text1 = font.render("Love You", True, (0,0,0))
    screen.blit(text1, (50, 200))
    pygame.display.update()
    screen.fill("skyblue")
    screen.blit(bj, (0,0))
    time.sleep(2)
    font = pygame.font.SysFont("Times New Roman", 50)
    text1 = font.render("Happy Life", True, (0,0,0))
    screen.blit(text1, (50, 200))
    pygame.display.update()

    