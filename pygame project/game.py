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
BLOCK_SEMISOLID = [12, 13]
BLOCK_CLIMBABLE = [11, 12]

WEAPON_TRIPLE_SHOT = 0
WEAPON_CRYSTAL_BLAST = 1
WEAPON_SHOCK_FORCE = 2
WEAPON_SPIRAL_CYCLONE = 3
WEAPON_BURNER_WAVE = 4
WEAPON_LEAF_GUARD = 5
WEAPON_DOWNPOUR_STORM = 6

# used for boundaries in camera or npc behavior
class Section():
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x          = x
        self.y          = y
        self.width      = width
        self.height     = height

# classes
class Player():
    def __init__(self, x: int, y: int, section: int) -> None:
        self.gfx            = pygame.image.load("pygame project\\test.png")
        self.rect           = self.gfx.get_rect()
        # Gameplay vars
        self.width          = self.rect.width
        self.height         = self.rect.height
        self.speedX         = 0
        self.speedY         = 0
        self.direction      = 1
        self.section        = section
        self.maxHealth      = 16
        self.health         = self.maxHealth
        self.weapon         = 0
        # Starting location
        self.rect.x         = sections[section].x + x
        self.rect.y         = sections[section].y + y
        # Player states
        self.jumpTimer      = 0
        self.hasJumped      = 0
        self.attackCooldown = 0
        self.bulletsOut     = 0
        self.isOnGround     = True
        self.isClimbing     = False
        self.nearLadder     = False
    
    def handleControls(self):
        if pygame.key.get_pressed():
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.direction = DIR_RIGHT
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                self.direction = DIR_LEFT
            
            if not self.isClimbing:                    
                self.speedX = self.direction

                if pygame.key.get_pressed()[pygame.K_z] and (not self.hasJumped) and self.isOnGround:
                    self.hasJumped = True
                
                if (pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN]) and self.nearLadder:
                    self.isClimbing = True
            else:
                if pygame.key.get_pressed()[pygame.K_UP]:
                    self.speedY = -1
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.speedY = 1

                if (not pygame.key.get_pressed()[pygame.K_UP]) and (not pygame.key.get_pressed()[pygame.K_DOWN]):
                    self.speedY = 0
                
                # dismount from ladder
                if pygame.key.get_pressed()[pygame.K_z]:
                    self.isClimbing = False

            if (not pygame.key.get_pressed()[pygame.K_RIGHT]) and (not pygame.key.get_pressed()[pygame.K_LEFT]):
                self.speedX = 0
            
            if pygame.key.get_pressed()[pygame.K_s] and self.attackCooldown == 0 and self.bulletsOut < 3:
                self.attackCooldown = 10
                self.bulletsOut += 1

                offset = 0
                if self.direction == 1:
                    offset = self.width
                
                sectionX = self.rect.x - sections[self.section].x
                sectionY = self.rect.y - sections[self.section].y

                npcClass = NPC(1, sectionX + offset, sectionY, self.section, self.direction)

                npcs.append(npcClass)
    
    def update(self):
        if not camera.isUpdating:
            self.handleControls()
            
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

            if self.isClimbing:
                self.width = 16
            else:
                self.width = 32
        else:
            if camera.moveDir == DIR_LEFT or camera.moveDir == DIR_RIGHT:
                self.direction = camera.moveDir
                self.speedY = 0

                if self.isOnGround:
                    self.speedX = self.direction

        for k, b in enumerate(blocks):
            # ladder collision
            if b.climbable:
                if b.rect.colliderect(self.rect.x - 8, self.rect.y - 8, self.width + 8, self.height + 8):
                    self.nearLadder = True
                else:
                    self.nearLadder = False
                
                if self.isClimbing:
                    self.rect.x = b.rect.x
            
            # horizontal collision
            if b.solidSide:
                if b.rect.colliderect(self.rect.x + self.speedX, self.rect.y, self.width, self.height):
                    self.speedX = 0

            # vertical collision
            if b.rect.colliderect(self.rect.x, self.rect.y + self.speedY, self.width, self.height):
                # below the block
                if self.speedY < 0:
                    if b.solidBottom:
                        self.speedY = b.rect.bottom - self.rect.top
                        self.speedY = 0
                # above the block
                elif self.speedY > 0:
                    if b.solidTop:
                        if not self.isClimbing:
                            if b.solidSide:
                                self.speedY = b.rect.top - self.rect.bottom
                            else:
                                if (player.rect.x + player.speedX >= b.rect.top):
                                    self.speedY = b.rect.top - self.rect.bottom
                        else:
                            if b.solidSide:
                                self.speedY = b.rect.top - self.rect.bottom
                        # reset jump status
                        self.hasJumped = False
                        self.jumpTimer = 0
                        self.isOnGround = True

                        if b.climbable:
                            self.nearLadder = True
                
            #dismount from ladders
            if player.isClimbing:
                if b.climbable and b.solidTop:
                    if (self.rect.bottom < b.rect.top + 2):
                        self.isClimbing = False

        self.rect.x += self.speedX
        self.rect.y += self.speedY

        #check which section the player is in
        for k, s in enumerate(sections):
            if player.rect.x >= s.x and player.rect.x <= s.x + s.width:
                player.section = k

        screen.blit(self.gfx, (self.rect.x - camera.x, self.rect.y - camera.y))
        #pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

class Block():
    def __init__(self, id: int, x: int, y: int, section: int) -> None:
        self.id                 = id
        self.gfx                = pygame.image.load(f"pygame project\\block\\block-{id}.png")
        self.rect               = self.gfx.get_rect()
        self.width              = self.rect.width
        self.height             = self.rect.height
        # Starting location
        self.rect.x             = sections[section].x + x
        self.rect.y             = sections[section].y + y
        # block behavior
        self.solidSide          = False
        self.solidBottom        = False
        self.solidTop           = False
        self.climbable          = False
        self.foreground         = False

        if self.id in BLOCK_CLIMBABLE:
            self.climbable      = True
        if self.id in BLOCK_SOLID:
            self.solidSide      = True
            self.solidBottom    = True
            self.solidTop       = True
            self.foreground     = True
        if self.id in BLOCK_SEMISOLID:
            self.solidTop       = True
    
    def update(self):
        screenX = self.rect.x - camera.x
        screenY = self.rect.y - camera.y
        
        if screenX > -16 and screenX < width + 16 and screenY > -16 and screenY < height + 16:
            screen.blit(self.gfx, (screenX, screenY))
        #pygame.draw.rect(screen, (0, 0, 255), self.rect, 2)

class NPC():
    def __init__(self, id: int, x: int, y: int, section: int, direction: int) -> None:
        self.id             = id
        self.gfx            = pygame.image.load(f"pygame project\\npc\\npc-{id}.png")
        self.rect           = self.gfx.get_rect()
        self.width          = self.rect.width
        self.height         = self.rect.height
        # Starting location
        self.section        = section
        self.rect.x         = sections[section].x + x
        self.rect.y         = sections[section].y + y
        # NPC vars
        self.isValid        = True              # if it's alive
        self.isActive       = True              # if it's on-screen
        self.direction      = direction
        self.speedX         = 0
        self.speedY         = 0
        self.health         = 0                 # if the npc relies on health, it won't die until it reaches 0.
        self.immuneFrames   = 0                 # invincibility frames (only when > 0)
    
    def kill(self):
        self.isValid = False
        self.isActive = False
        
        npcs.remove(self)
    
    def harm(self, damage: int, invincibleFrames: int):
        self.health = self.health - damage

        if self.health <= 0:
            self.kill()
        else:
            self.immuneFrames = invincibleFrames
    
    def update(self):
        # the actual npc behavior
        if self.isValid:
            if self.id == 1:
                self.speedX = self.direction * 4

                if self.rect.x + self.width < camera.x or self.rect.x > camera.x + camera.width:
                    player.bulletsOut -= 1
                    self.kill()
                if camera.isUpdating:
                    player.bulletsOut -= 1
                    self.kill()
            
            self.rect.x += self.speedX
            self.rect.y += self.speedY

        # render npcs
        screenX = self.rect.x - camera.x
        screenY = self.rect.y - camera.y

        # check which section the npc is in
        for k, s in enumerate(sections):
            if self.rect.x >= s.x and self.rect.x <= s.x + s.width:
                self.section = k
        
        if screenX > -16 and screenX < width + 16 and screenY > -16 and screenY < height + 16:
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
        self.section    = player.section
    
    def update(self):
        if not self.isUpdating:
            if player.rect.x + player.width > sections[self.section].x + sections[self.section].width: # right
                self.dx = self.width
                self.targetX = self.x + self.width
                self.moveDir = DIR_RIGHT
            elif player.rect.x < sections[self.section].x: # left
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
        else:
            self.section = player.section

# gameplay objects
sections = [
    Section(0, 0, width * 2, height),
    Section(-width, 0, width, height)
]

player = Player(16, 160, 0)
camera = Camera(0, 0)
clock = pygame.time.Clock()

blocks = [
    #Block(3, 208, 192, 1),
    Block(3, 224, 192, 1),
    Block(3, 240, 192, 1),
    Block(3, 0, 192, 0),
    Block(3, 16, 192, 0),
    Block(3, 32, 192, 0),
    Block(1, 48, 160, 0),
    Block(1, 48, 176, 0),
    Block(3, 48, 192, 0),
    Block(3, 64, 192, 0),
    Block(3, 80, 192, 0),
    Block(4, 96, 192, 0),
    Block(1, 64, 64, 0),
    Block(1, 80, 64, 0),
    Block(1, 96, 64, 0),
    Block(3, 112, 208, 0),
    #Block(1, 128, 64, 0),
    Block(12, 112, 64, 0),
    Block(11, 112, 80, 0),
    Block(11, 112, 96, 0),
    Block(11, 112, 112, 0),
    Block(11, 112, 128, 0),
    Block(11, 112, 144, 0),
    Block(11, 112, 160, 0),
    Block(11, 112, 176, 0),
    Block(11, 112, 192, 0),
    Block(4, 128, 208, 0),
    Block(2, 208, 208, 0),
    Block(3, 224, 208, 0),
    Block(3, 240, 208, 0),
    Block(3, 256, 208, 0),
    Block(3, 272, 208, 0),
    Block(3, 288, 208, 0),
    Block(3, 304, 208, 0),
    Block(4, 320, 208, 0)
]

npcs = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    if inGame:
        screen.fill(black)

        for k, b in enumerate(blocks):
            if not b.foreground:
                b.update()
        
        player.update()

        # foreground blocks
        for k, b in enumerate(blocks):
            if b.foreground:
                b.update()
        
        for k, v in enumerate(npcs):
            v.update()
        
        camera.update()
    
    pygame.display.flip()
    clock.tick(60)