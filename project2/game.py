import sys, pygame
pygame.init()

size = width, height = 240, 160
screen = pygame.display.set_mode(size, pygame.SCALED)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()