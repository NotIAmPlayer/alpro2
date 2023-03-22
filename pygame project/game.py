import sys, pygame
pygame.init()

size = width, height = 256, 224
screen = pygame.display.set_mode(size)
black = (0, 0, 0)

class Player():
    def __init__(self, x: int, y: int) -> None:
        self.gfx            = pygame.image.load("pygame project\\test.png")
        self.rect           = self.gfx.get_rect()
        # Gameplay vars
        self.width          = self.rect.width
        self.height         = self.rect.height
        self.speedX         = 0
        self.speedY         = 0
        self.direction      = 1
        # Starting location
        self.rect.x         = x
        self.rect.y         = y
        # Player states
        self.jumpTimer      = 0
        self.hasJumped      = 0
    
    def update(self):        
        if pygame.key.get_pressed():
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.speedX = 1
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.speedX = -1
            if (not pygame.key.get_pressed()[pygame.K_RIGHT]) and (not pygame.key.get_pressed()[pygame.K_LEFT]):
                self.speedX = 0
            
            if pygame.key.get_pressed()[pygame.K_z] and not self.hasJumped:
                self.hasJumped = True
                self.collideBottom = False
        
        if self.hasJumped and self.jumpTimer < 22:
            self.speedY = -2.2

            self.jumpTimer += 1
        else:
            if self.speedY < 3:
                self.speedY += 0.4
            else:
                self.speedY = 3
        
        for k, v in enumerate(blocks):
            # horizontal collision
            if v.rect.colliderect(self.rect.x + self.speedX, self.rect.y, self.width, self.height):
                self.speedX = 0

            # vertical collision
            if v.rect.colliderect(self.rect.x, self.rect.y + self.speedY, self.width, self.height):
                # below the block
                if self.speedY < 0:
                    self.speedY = v.rect.bottom - self.rect.top
                    self.speedY = 0
                # above the block
                elif self.speedY >= 0:
                    self.speedY = v.rect.top - self.rect.bottom
                    # reset jump status
                    self.hasJumped = False
                    self.jumpTimer = 0

        self.rect.x += self.speedX
        self.rect.y += self.speedY

        screen.blit(self.gfx, self.rect)
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

class Block():
    def __init__(self, id: int, x: int, y: int) -> None:
        self.id             = id
        self.gfx            = pygame.image.load(f"pygame project\\block-{id}.png")
        self.rect           = self.gfx.get_rect()
        self.width          = self.rect.width
        self.height         = self.rect.height
        # Starting location
        self.rect.x         = x
        self.rect.y         = y
    
    def update(self):
        screen.blit(self.gfx, self.rect)
        #pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

player = Player(16, 160)
clock = pygame.time.Clock()

blocks = [
    Block(3, 0, 192),
    Block(3, 16, 192),
    Block(3, 32, 192),
    Block(1, 48, 160),
    Block(1, 48, 176),
    Block(3, 48, 192),
    Block(3, 64, 192),
    Block(3, 80, 192),
    Block(4, 96, 192),
    Block(1, 64, 64),
    Block(1, 80, 64),
    Block(1, 96, 64),
    Block(3, 112, 208),
    Block(3, 128, 208),
    Block(3, 144, 208),
    Block(4, 160, 208),
    Block(2, 240, 208)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    
    player.update()

    for k, b in enumerate(blocks):
        b.update()
    
    pygame.display.flip()
    clock.tick(60)