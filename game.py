import sys, pygame
pygame.init()

size = width, height = 320, 240
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
rect = pygame.Rect(16, 16, 32, 32)
gfx = pygame.Surface((32, 32))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill((0, 0, 0))

    pygame.display.flip()
    clock.tick(60)