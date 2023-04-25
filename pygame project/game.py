import sys, pygame
pygame.init()

size = width, height = 256, 224
screen = pygame.display.set_mode(size)
black = (0, 0, 0)
inGame = True

# constants
DIR_LEFT = -1
DIR_RIGHT = 1
DIR_UP = -2
DIR_DOWN = 2

BLOCK_SOLID = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
BLOCK_CLIMBABLE = [11]

# functions
def getBlock(ids: list):
    b = blocks
    
    #filter
    if ids != []:
        for k, v in enumerate(b):
            if not(v.id in ids):
                b.remove(v)
    
    return b

# classes
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
        self.attackCooldown = 0
        self.bulletsOut     = 0
        self.isOnGround     = True
    
    def update(self):
        if not camera.isUpdating:
            if pygame.key.get_pressed():
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    self.direction = DIR_RIGHT
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    self.direction = DIR_LEFT
                self.speedX = self.direction

                if (not pygame.key.get_pressed()[pygame.K_RIGHT]) and (not pygame.key.get_pressed()[pygame.K_LEFT]):
                    self.speedX = 0
                
                if pygame.key.get_pressed()[pygame.K_z] and (not self.hasJumped) and self.isOnGround:
                    self.hasJumped = True
                
                if pygame.key.get_pressed()[pygame.K_s] and self.attackCooldown == 0 and self.bulletsOut < 3:
                    self.attackCooldown = 10
                    self.bulletsOut += 1

                    offset = 0
                    if self.direction == 1:
                        offset = self.width

                    npcClass = NPC(1, self.rect.x + offset, self.rect.y, self.direction)

                    npcs.append(npcClass)
            
            if self.hasJumped and self.jumpTimer < 22:
                self.speedY = -2.2

                self.jumpTimer += 1
                self.isOnGround = False
            else:
                if self.speedY < 3:
                    self.speedY += 0.4
                else:
                    self.speedY = 3
                self.isOnGround = False

            if self.attackCooldown > 0:
                self.attackCooldown -= 1
        else:
            if camera.moveDir == DIR_LEFT or camera.moveDir == DIR_RIGHT:
                self.direction = camera.moveDir
                self.speedY = 0

                if self.isOnGround:
                    self.speedX = self.direction

        for k, v in enumerate(getBlock(BLOCK_SOLID)):
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
                    self.isOnGround = True

        self.rect.x += self.speedX
        self.rect.y += self.speedY

        screen.blit(self.gfx, (self.rect.x - camera.x, self.rect.y - camera.y))
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

class Block():
    def __init__(self, id: int, x: int, y: int) -> None:
        self.id             = id
        self.gfx            = pygame.image.load(f"pygame project\\block\\block-{id}.png")
        self.rect           = self.gfx.get_rect()
        self.width          = self.rect.width
        self.height         = self.rect.height
        # Starting location
        self.rect.x         = x
        self.rect.y         = y
    
    def update(self):
        screenX = self.rect.x - camera.x
        screenY = self.rect.y - camera.y
        
        if screenX > -16 and screenX < 272 and screenY > -16 and screenY < 240:
            screen.blit(self.gfx, (screenX, screenY))
        #pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

class NPC():
    def __init__(self, id: int, x: int, y: int, direction: int) -> None:
        self.id             = id
        self.gfx            = pygame.image.load(f"pygame project\\npc\\npc-{id}.png")
        self.rect           = self.gfx.get_rect()
        self.width          = self.rect.width
        self.height         = self.rect.height
        # Starting location
        self.rect.x         = x
        self.rect.y         = y
        # NPC vars
        self.isValid        = True              #if it's alive
        self.isActive       = True              #if it's on-screen
        self.direction      = direction
        self.speedX         = 0
        self.speedY         = 0
    
    def update(self):
        if self.isValid:
            if self.id == 1:
                self.speedX = self.direction * 3

                if self.rect.x + self.width < camera.x or self.rect.x > camera.x + camera.width:
                    player.bulletsOut -= 1
                    npcs.remove(self)
                if camera.isUpdating:
                    player.bulletsOut -= 1
                    npcs.remove(self)
            
            self.rect.x += self.speedX
            self.rect.y += self.speedY

        screenX = self.rect.x - camera.x
        screenY = self.rect.y - camera.y
        
        if screenX > -16 and screenX < 272 and screenY > -16 and screenY < 240:
            screen.blit(self.gfx, (screenX, screenY))
            self.isActive = True
        else:
            self.isActive = False # might add exceptions because some enemies can work off-screen

class Camera():
    def __init__(self, startX: int, startY: int) -> None:
        self.x          = startX
        self.y          = startY
        self.width      = width
        self.height     = height
        # movement vars (targetX, Y, and moveDir only used to nudge the player a bit)
        self.dx         = 0
        self.dy         = 0
        self.targetX    = 0
        self.targetY    = 0
        self.moveDir    = 0
        self.isUpdating = False
    
    def update(self):
        if not self.isUpdating:
            if player.rect.x + player.width > self.x + self.width: # right
                self.dx = self.width
                self.targetX = self.x + self.width
                self.moveDir = DIR_RIGHT
            elif player.rect.x < self.x: # left
                self.dx = -self.width
                self.targetX = self.x - self.width
                self.moveDir = DIR_LEFT
            self.isUpdating = True
        
        if self.dx != 0:
            if self.dx > 0:
                self.dx -= 4
                self.x += 4
            else:
                self.dx += 4
                self.x -= 4
        
        if self.dy != 0:
            if self.dy > 0:
                self.dy -= 4
                self.y += 4
            else:
                self.dy += 4
                self.y -= 4
        
        if (self.dx == 0) and (self.dy == 0):
            self.isUpdating = False

# gameplay objects
player = Player(16, 160)
camera = Camera(0, 0)
clock = pygame.time.Clock()

blocks = [
    #Block(3, -48, 192),
    Block(3, -32, 192),
    Block(3, -16, 192),
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
    Block(11, 112, 192),
    Block(11, 112, 176),
    Block(11, 112, 160),
    Block(4, 128, 208),
    Block(2, 208, 208),
    Block(3, 224, 208),
    Block(3, 240, 208),
    Block(3, 256, 208),
    Block(3, 272, 208),
    Block(3, 288, 208),
    Block(3, 304, 208),
    Block(4, 320, 208)
]

npcs = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if inGame:
        screen.fill(black)
        
        player.update()

        for k, b in enumerate(blocks):
            b.update()
        
        for k, v in enumerate(npcs):
            v.update()
        
        camera.update()
    
    pygame.display.flip()
    clock.tick(60)