# NAME: MOHAMMAD SALAUDEEN

import pygame
import math

screen = pygame.display.set_mode((700, 700))
# Colour constants
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)

screen.fill(white)
# draws body
pygame.draw.polygon(screen, black, ((136, 345), (184, 169), (228, 147), (271, 170), (269, 354)))

pygame.draw.circle(screen, black, (228, 172), 43)
# draws head, eye, nose
pygame.draw.circle(screen, black, (234, 73), 40)
pygame.draw.circle(screen, white, (253, 63), 5)
pygame.draw.rect(screen, black, (261, 70, 20, 10))
# draws arms, legs and prop
pygame.draw.arc(screen, black, (145, 61, 254, 175), 3 * math.pi / 2, 2 * math.pi, 7)
pygame.draw.rect(screen, grey, (375, 100, 30, 50))
pygame.draw.rect(screen, black, (391, 105, 10, 12))
pygame.draw.arc(screen, white, (240, 75, 50, 30), math.pi, 5 * math.pi / 3, 2)
pygame.draw.arc(screen, black, (100, 205, 200, 180), math.pi / 2, 5 * math.pi / 4, 7)
pygame.draw.arc(screen, black, (127, 322, 200, 195), math.pi / 2, 5 * math.pi / 4, 7)
pygame.draw.arc(screen, black, (113, 335, 200, 230), 11 * math.pi / 6, math.pi / 2, 7)
pygame.draw.circle(screen, black, (292, 520), 15)
pygame.draw.circle(screen, black, (167, 495), 15)
pygame.display.update()
pygame.time.delay(3000)
