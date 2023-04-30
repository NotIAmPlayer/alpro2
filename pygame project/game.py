import sys, pygame
import math
pygame.init()

size = width, height = 256, 224
screen = pygame.display.set_mode(size, pygame.SCALED)
black = (0, 0, 0)
inGame = True

pygame.display.set_caption("Xyler Infiltration w10")
font = pygame.font.Font("pygame project\\font\\PressStart2P.ttf", 8)

# assets
bars = [
    pygame.image.load("pygame project\\hud\\bar_health.png"),
    pygame.image.load("pygame project\\hud\\bar_crystal_blast.png"),
    pygame.image.load("pygame project\\hud\\bar_shock_force.png"),
    pygame.image.load("pygame project\\hud\\bar_spiral_cyclone.png"),
    pygame.image.load("pygame project\\hud\\bar_burner_wave.png"),
    pygame.image.load("pygame project\\hud\\bar_leaf_guard.png"),
    pygame.image.load("pygame project\\hud\\bar_downpour_storm.png"),
    pygame.image.load("pygame project\\hud\\bar_empty.png"),
]

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

# functions
def lookForSection(x: int, y: int) -> int:
    for k, s in enumerate(sections):
        if x >= s.x and x <= s.x + s.width and y >= s.y and y <= s.y + s.height:
            return k
    
    return -1 #no sections are found

def math_clamp(num, min, max) -> float:
    return min if num < min else max if num > max else num

# classes
# used for boundaries in camera or npc behavior
class Section():
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x          = x
        self.y          = y
        self.width      = width
        self.height     = height

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
        self.maxHealth      = 18
        self.health         = self.maxHealth
        self.weapon         = 0
        # Starting location
        self.rect.x         = sections[section].x + x
        self.rect.y         = sections[section].y + y
        # Player states
        self.jumpTimer      = 0
        self.hasJumped      = 0
        self.attackCooldown = 0
        self.isOnGround     = False
        self.isClimbing     = False
        self.nearLadder     = False
        self.bulletsOut     = 0
        self.immuneFrames   = 0
        self.hasDied        = False
        self.deathTimer     = 0

    def harm(self, damage: int):
        self.health = self.health - damage

        if self.health <= 0:
            self.hasDied = True
        else:
            self.immuneFrames = 90
    
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
        #self.health = (self.health + 1) % self.maxHealth + 1
        if not self.hasDied:
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
                                    if (player.rect.bottom + player.speedX >= b.rect.top - 2) and (player.rect.centery + (player.height/3) < b.rect.top):
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
            
            if self.immuneFrames > 0:
                self.immuneFrames -= 1

            self.rect.x += self.speedX
            self.rect.y += self.speedY

        #check which section the player is in
        for k, s in enumerate(sections):
            if player.rect.x >= s.x and player.rect.x <= s.x + s.width and player.rect.y >= s.y and player.rect.y <= s.y + s.height:
                player.section = k
        
        # flicker when the player gets damaged
        if self.immuneFrames % 4 == 0:
            screen.blit(self.gfx, (self.rect.x - camera.x, self.rect.y - camera.y), (0, 0, self.width, self.height))
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

class NPC_config():
    def __init__(self):
        self.width              = [8, 16, 8]
        self.height             = [8, 16, 8]
        self.gfxwidth           = [8, 18, 8]
        self.gfxheight          = [8, 18, 8]
        self.gfxoffsetx         = [0, -1, 0]
        self.gfxoffsety         = [0, -2, 0]
        self.frames             = [2, 4, 1]
        self.framestyle         = [1, 1, 0]
        self.framedelay         = [1, 1, 1]
        self.health             = [0, 3, 0]
        self.nogravity          = [True, False]
        self.noblockcollision   = [True, False]

npc_cfg = NPC_config()        

class NPC():
    def __init__(self, id: int, x: int, y: int, section: int, direction: int) -> None:
        self.id             = id
        self.gfx            = pygame.image.load(f"pygame project\\npc\\npc-{id}.png")
        self.rect           = self.gfx.get_rect()
        self.rect.width     = npc_cfg.width[id - 1]
        self.rect.height    = npc_cfg.height[id - 1]
        self.gfxwidth       = npc_cfg.gfxwidth[id - 1]
        self.gfxheight      = npc_cfg.gfxheight[id - 1]
        # Starting location
        self.section        = section
        self.rect.x         = sections[section].x + x
        self.rect.y         = sections[section].y + y
        # NPC vars
        self.aiState        = 0
        self.aiTimer        = 0
        self.isValid        = True                      # if it's alive
        self.isActive       = True                      # if it's on-screen
        self.direction      = direction
        self.speedX         = 0
        self.speedY         = 0
        self.health         = npc_cfg.health[id - 1]    # if the npc relies on health, it won't die until it reaches 0.
        self.immuneFrames   = 0                         # invincibility frames (only when > 0)
        self.frame          = 0                         # frame in animation
        self.frameTimer     = 0

        #shorthands
        self.width          = self.rect.width
        self.height         = self.rect.height
    
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
                
                if self.direction == DIR_LEFT:
                    self.frame = 0
                else:
                    self.frame = 1
            if self.id == 2:
                if self.aiState == 0:
                    if math.fabs(player.rect.centerx - self.rect.centerx) <= 80:
                        self.aiState = 1
                    
                    if player.rect.centerx - self.rect.centerx < 0:
                        self.direction = DIR_LEFT
                    else:
                        self.direction = DIR_RIGHT
                    
                    if self.direction == DIR_LEFT:
                        self.frame = 0
                    else:
                        self.frame = 2

                    for k, v in enumerate(npcs):
                        if self.rect.colliderect(v.rect):
                            if v.id == 1:
                                v.direction = -v.direction
                                v.speedY = -3/math.sqrt(2)
                                v.speedX = 4 * v.direction
                else:
                    if self.aiTimer == 0:
                        sectionX = self.rect.x - sections[self.section].x
                        sectionY = self.rect.y - sections[self.section].y
                        
                        p1 = NPC(3, sectionX + self.width/2, sectionY + self.height/2, self.section, self.direction)
                        p1.speedX = 3/math.sqrt(2) * self.direction
                        p1.speedY = -3/math.sqrt(2)

                        p2 = NPC(3, sectionX + self.width/2, sectionY + self.height/2, self.section, self.direction)
                        p2.speedX = 3 * self.direction

                        p3 = NPC(3, sectionX + self.width/2, sectionY + self.height/2, self.section, self.direction)
                        p3.speedX = 3/math.sqrt(2) * self.direction
                        p3.speedY = 3/math.sqrt(2)

                        npcs.append(p1)
                        npcs.append(p2)
                        npcs.append(p3)

                    self.aiTimer += 1

                    if self.direction == DIR_LEFT:
                        self.frame = 1
                    else:
                        self.frame = 3

                    if self.aiTimer >= 96:
                        self.aiState = 0
                        self.aiTimer = 0
                    
                    for k, v in enumerate(npcs):
                        if self.rect.colliderect(v.rect) and self.immuneFrames == 0:
                            if v.id == 1:
                                self.harm(1, 8)
                
                if player.immuneFrames == 0:
                    if self.rect.colliderect(player.rect):
                        player.harm(1)
            if self.id == 3:
                if self.rect.x + self.width < camera.x or self.rect.x > camera.x + camera.width:
                    player.bulletsOut -= 1
                    self.kill()
                if camera.isUpdating:
                    player.bulletsOut -= 1
                    self.kill()
                
                if player.immuneFrames == 0:
                    if self.rect.colliderect(player.rect):
                        player.harm(2)
            
            self.rect.x += self.speedX
            self.rect.y += self.speedY
        
        if self.immuneFrames > 0:
            self.immuneFrames -= 1

        # render npcs
        screenX = self.rect.x - camera.x
        screenY = self.rect.y - camera.y

        # check which section the npc is in
        for k, s in enumerate(sections):
            if self.rect.x >= s.x and self.rect.x <= s.x + s.width:
                self.section = k
        
        if screenX > -16 and screenX < width + 16 and screenY > -16 and screenY < height + 16:
            # same treatment as the player
            if self.immuneFrames % 4 == 0:
                screen.blit(self.gfx, (screenX + npc_cfg.gfxoffsetx[self.id - 1], screenY + npc_cfg.gfxoffsety[self.id - 1]), (0, self.frame * self.gfxheight, self.gfxwidth, self.gfxheight))
            self.isActive = True
        else:
            self.isActive = False # might add exceptions because some enemies can work off-screen
        #pygame.draw.rect(screen, (255, 0, 0), (screenX, screenY, self.width, self.height), 2)

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
        '''
        if not self.isUpdating:
            if player.rect.x + player.width > sections[self.section].x + sections[self.section].width: # right
                nextSection = lookForSection(player.rect.x + player.width, player.rect.y)

                if nextSection != -1:
                    self.dx = self.width
                    self.targetX = self.x + self.width
                    self.moveDir = DIR_RIGHT
            elif player.rect.x < sections[self.section].x: # left
                nextSection = lookForSection(player.rect.x, player.rect.y)
                
                if nextSection != -1:
                    self.dx = -self.width
                    self.targetX = self.x - self.width
                    self.moveDir = DIR_LEFT
            elif player.rect.y + player.height > sections[self.section].y + sections[self.section].height: # down
                nextSection = lookForSection(player.rect.x, player.rect.y + player.height)
                
                if nextSection != -1:
                    self.dy = self.height
                    self.targetY = self.y + self.height
                    self.moveDir = DIR_DOWN
            elif player.rect.y < sections[self.section].y: # up
                nextSection = lookForSection(player.rect.x, player.rect.y)

                if nextSection != -1:
                    self.dy = -self.height
                    self.targetY = self.y - self.height
                    self.moveDir = DIR_UP
            self.isUpdating = True
        print(f"{self.x}, {self.y}")

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
        '''
        if player.rect.x >= self.x + (self.width / 2) and player.speedX > 0:
            self.dx = player.speedX
        if player.rect.x <= self.x + (self.width / 2) and player.speedX < 0:
            self.dx = player.speedX
        
        self.x += self.dx
        self.y += self.dy
        self.x = math_clamp(self.x, sections[player.section].x, sections[player.section].x + sections[player.section].width - self.width)
        self.y = math_clamp(self.y, sections[player.section].y, sections[player.section].y + sections[player.section].height - self.height)
        self.dx = 0
        self.dy = 0

        self.section = player.section

# gameplay objects
sections = [
    Section(0, 0, width * 2, height),
    Section(-width, 0, width, height),
]

blocks = [
    #Block(3, 208, 192, 1),
    Block(3, 224, 192, 1),
    Block(3, 240, 192, 1),
    Block(3, 0, 192, 0),
    Block(3, 16, 192, 0),
    Block(3, 32, 192, 0),
    Block(1, 48, 160, 0),
    Block(1, 48, 176, 0),
    Block(13, 64, 160, 0),
    Block(13, 80, 160, 0),
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
    Block(1, 176, 64, 0),
    Block(1, 192, 64, 0),
    Block(1, 208, 64, 0),
    Block(1, 224, 64, 0),
    Block(1, 240, 64, 0),
    Block(1, 256, 64, 0),
    Block(1, 272, 64, 0),
    Block(1, 288, 64, 0),
    Block(1, 304, 64, 0),
    Block(1, 320, 64, 0),
    Block(4, 128, 208, 0),
    Block(2, 208, 208, 0),
    Block(3, 224, 208, 0),
    Block(3, 240, 208, 0),
    Block(3, 256, 208, 0),
    Block(3, 272, 208, 0),
    Block(3, 288, 208, 0),
    Block(3, 304, 208, 0),
    Block(4, 320, 208, 0),
    Block(13, 272, 160, 0),
    Block(13, 288, 160, 0),
    Block(13, 304, 160, 0),
    Block(13, 320, 160, 0),
    Block(1, 336, 64, 0),
    Block(1, 352, 64, 0),
    Block(1, 368, 64, 0),
    Block(1, 384, 64, 0),
    Block(1, 400, 64, 0),
    Block(1, 416, 64, 0),
    Block(1, 432, 64, 0),
    Block(1, 448, 64, 0),
    Block(1, 464, 64, 0),
    Block(1, 480, 64, 0),
    Block(1, 496, 64, 0),
    Block(1, 496, 0, 0),
    Block(1, 496, 16, 0),
    Block(1, 496, 32, 0),
    Block(1, 496, 48, 0),
]

npcs = [NPC(2, 304, 144, 0, DIR_LEFT)]

player = Player(16, 144, 0)
camera = Camera(0, 0)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if inGame:
        screen.fill((30, 86, 51))

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
        
        # HUDs
        screen.blit(bars[7], (8, 78 - player.maxHealth * 2), (0, 0, 8, player.maxHealth * 2))

        for i in range(player.health + 1):
            x = 8
            y = 78 - 2 * i
            screen.blit(bars[0], (x, y))
        
        text = font.render(f"{player.health}", False, (255, 255, 255))
        screen.blit(text, (8, 88))
        
        camera.update()
    
    pygame.display.flip()
    clock.tick(60)