import sys, pygame
pygame.init()

size = width, height = 256, 224
screen = pygame.display.set_mode(size)
black = (0, 0, 0)

class Player():
    def __init__(self) -> None:
        self.gfx            = pygame.image.load("pygame project\\test.png")
        self.rect           = self.gfx.get_rect()
        #Gameplay vars
        self.x              = self.rect.x
        self.y              = self.rect.y
        self.width          = self.rect.width
        self.height         = self.rect.height
        self.speedX         = 0
        self.speedY         = 0
        self.direction      = 1
        # Player states
        self.jumpTimer      = 0
        self.hasJumped      = 0
        self.collideLeft    = False
        self.collideRight   = False
        self.collideTop     = False
        self.collideBottom  = False
    
    def update(self):
        self.x = self.rect.x
        self.y = self.rect.y

        if pygame.key.get_pressed():
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.speedX = 1
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.speedX = -1
            if (not pygame.key.get_pressed()[pygame.K_RIGHT]) and (not pygame.key.get_pressed()[pygame.K_LEFT]):
                self.speedX = 0
            
            if pygame.key.get_pressed()[pygame.K_z] and self.rect.collideobjectsall(blockRects):
                self.hasJumped = True
        
        if not self.rect.collideobjectsall(blockRects):
            if self.speedY < 3:
                self.speedY += 0.4
        else:
            self.speedY = 0
        
        if self.hasJumped and self.jumpTimer < 32:
            self.speedY = -2.2

            self.jumpTimer += 1
        else:
            self.hasJumped = False
            self.jumpTimer = 0
        
        self.rect = self.rect.move((self.speedX, self.speedY))

        screen.blit(self.gfx, self.rect)

        

player = Player()
clock = pygame.time.Clock()

blockGFXs = [pygame.image.load("pygame project\\block-1.png")]
blockRects = [blockGFXs[0].get_rect(), blockGFXs[0].get_rect(), blockGFXs[0].get_rect(), blockGFXs[0].get_rect(), blockGFXs[0].get_rect(), blockGFXs[0].get_rect(), blockGFXs[0].get_rect()]
playerStates = [False, 0]

blockRects[0].y = 192
blockRects[1].x, blockRects[1].y = 16, 192
blockRects[2].x, blockRects[2].y = 32, 192
blockRects[3].x, blockRects[3].y = 48, 160
blockRects[4].x, blockRects[4].y = 64, 192
blockRects[5].x, blockRects[5].y = 80, 192
blockRects[6].x, blockRects[6].y = 96, 192

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)

    for k, v in enumerate(blockRects):
        screen.blit(blockGFXs[0], blockRects[k])
    
    player.update()
    
    pygame.display.flip()
    clock.tick(60)