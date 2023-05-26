import sys, pygame
pygame.init()

size = width, height = 256, 224
screen = pygame.display.set_mode(size, pygame.SCALED)
font = pygame.font.Font("pygame project/font/PressStart2P.ttf", 8)

clock = pygame.time.Clock()

# default set of controls, though gets overwritten by the ones read from the file.
controls = {
    'left'      : pygame.K_LEFT,
    'right'     : pygame.K_RIGHT,
    'up'        : pygame.K_UP,
    'down'      : pygame.K_DOWN,
    'jump'      : pygame.K_z,
    'shoot'     : pygame.K_s,
    'change (l)': pygame.K_c,
    'change (r)': pygame.K_d,
    'pause'     : pygame.K_RETURN,
}

new_controls = {
    'left'      : 0,
    'right'     : 0,
    'up'        : 0,
    'down'      : 0,
    'jump'      : 0,
    'shoot'     : 0,
    'change (l)': 0,
    'change (r)': 0,
    'pause'     : 0,
}

control_names = ['left', 'right', 'up', 'down', 'jump', 'shoot', 'change (l)', 'change (r)', 'pause']

sel = 0
keyIdx = 0
delay = 0
savingTextTimer = 0
takesChanges = False

try:
    file = open("test/option_controls.txt", "r")
except FileNotFoundError:
    print("Control configuration file doesn't exist. Creating a new file...")

    file = open("test/option_controls.txt", "w")
    text = f"{controls['left']};{controls['right']};{controls['up']};{controls['down']};{controls['jump']};{controls['shoot']};{controls['change (l)']};{controls['change (r)']};{controls['pause']}"
    file.write(text)
    file.close()
else:
    line = file.read()
    temp = line.split(';')

    for k, v in enumerate(controls):
        controls[control_names[k]] = int(temp[k])
    file.close()

# init the "new controls" to change into
for k, v in enumerate(controls):
    new_controls[control_names[k]] = controls[control_names[k]]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN and takesChanges:
            new_controls[control_names[sel]] = event.key
            takesChanges = False
            delay += 10
    
    screen.fill((0, 0, 0))

    text = font.render("NEW CONTROL SCHEMES ONLY APPLY", False, (255, 255, 255))
    text2 = font.render("AFTER CONFIRMING CHANGES", False, (255, 255, 255))
    screen.blit(text, (8, 48))
    screen.blit(text2, (32, 56))

    for k, v in enumerate(new_controls):
        color = (255, 255, 255)

        if k == sel and takesChanges:
            color = (245, 200, 66)
        
        keyName = pygame.key.name(new_controls[v])

        text = font.render(control_names[k].upper(), False, color)
        screen.blit(text, (16, 80 + (8 * k)))

        text2 = font.render(keyName.upper(), False, color)
        screen.blit(text2, (104, 80 + (8 * k)))

        if new_controls[v] != controls[v]:
            old_color = (100, 100, 100)
            keyName_old = pygame.key.name(controls[v])
            text3 = font.render(f"({keyName_old.upper()})", False, old_color)
            screen.blit(text3, (104 + (8 * len(keyName)), 80 + (8 * k)))
    
    confirmColor = (255, 255, 255)

    if sel == len(new_controls):
        confirmColor = (245, 200, 66)
    
    text = font.render("CONFIRM", False, confirmColor)
    screen.blit(text, (16, 160))

    cursor = font.render("> ", False, (245, 200, 66))
    if sel < len(new_controls):
        screen.blit(cursor, (8, 80 + (8 * sel)))
    else:
        screen.blit(cursor, (8, 160))

    if not takesChanges:
        if delay == 0:
            if pygame.key.get_pressed()[controls["down"]]:
                sel += 1
                delay += 10

                if sel >= len(controls) + 1:
                    sel -= len(controls) + 1
            elif pygame.key.get_pressed()[controls["up"]]:
                sel -= 1
                delay += 10

                if sel < 0:
                    sel += len(controls) + 1
        
            if pygame.key.get_pressed()[controls["jump"]]:
                if sel != len(controls):
                    takesChanges = True
                else:
                    savingTextTimer = 120
                    file = open("test/option_controls.txt", "w")
                    
                    text = f"{new_controls['left']};{new_controls['right']};{new_controls['up']};{new_controls['down']};{new_controls['jump']};{new_controls['shoot']};{new_controls['change (l)']};{new_controls['change (r)']};{new_controls['pause']}"
                    file.write(text)
                    file.close()
    else:
        text = font.render("PRESS ANY VALID KEY TO REPLACE THE SELECTED KEY", False, (255, 255, 255))
        screen.blit(text, (8, 176))

    if savingTextTimer > 0:
        delay = savingTextTimer
        text = font.render("SAVING CONTROL CONFIGURATION...", False, (255, 255, 255))
        screen.blit(text, (8, 176))

        savingTextTimer -= 1

        if savingTextTimer % 8 == 0:
            if keyIdx < len(controls):
                controls[control_names[keyIdx]] = new_controls[control_names[keyIdx]]

            keyIdx += 1
    else:
        keyIdx = 0
    
    if delay > 0:
        delay -= 1
    
    pygame.display.flip()
    clock.tick(60)