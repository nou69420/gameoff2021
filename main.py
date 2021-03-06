'''
Made by TheZeldaBoi/Ldude162
Submission for GitHub gameoff 2021
'''

#--- Import modules ---
import math
import random as rand
import pygame as game

#--- Start display ---
game.init()
surface = game.display.set_mode((400,300))

#--- color variables ---
lightGray = (170,170,170)
darkGray = (100,100,100)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
darkGreen = (0,100,0)

#--- Texts ---
startFont = game.font.SysFont('Corbel', 30)
startText = startFont.render('Click to start', True, green)
quitFont = game.font.SysFont('Corbel', 15)
quitText = quitFont.render('quit', True, darkGreen)
instructions = quitFont.render('Press space to flip gravity, dont get hit by red!', True, green)
gameOver = startFont.render('Game Over!', True, red)
mainMenu = quitFont.render('Main Menu', True, darkGreen)

#--- classes ---
class Ground(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game.Surface((400,80))
        self.image.fill(darkGreen)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 250

    def draw(self):
        surface.blit(self.image, self.rect)

class Player(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game.Surface((50,50))
        self.image.fill(green)

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 150
        self.onground = True

  # Draws the player on the screen and updates it
    def draw(self):
        self.rect.y = 0
        if self.onground == True:
            self.rect.bottom = ground.rect.top
        surface.blit(self.image, self.rect)

  # Function for jumping
    def gravitySwitch(self):
        if self.onground == False:
            self.onground = True
        elif self.onground == True:
            self.onground = False

class Redbox(game.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = game.Surface((50,50))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 0
        self.lap = 2
        self.location = 1

    def draw(self):
        self.rect.y = 0

        if self.location == 1:
            self.rect.bottom = ground.rect.top
        surface.blit(self.image, self.rect)
        self.rect.x -= math.log(self.lap,1.2)
        if self.rect.x <= 0:
            self.rect.x = 400
            self.location = rand.randrange(0,2)
            self.lap += 1

#--- sprites and objects ---
allSprites = game.sprite.Group()
ground = Ground()
player = Player()
redBox = Redbox()
allSprites.add(player)
allSprites.add(ground)
allSprites.add(redBox)
ticktock = game.time.Clock()


#--- Game Functions ---
def start():
    print("started")
    frame = 1
    global keepGoing
    
    while keepGoing:
        ticktock.tick(30)
        for event in game.event.get():
            if event.type == game.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
                    game.quit()
            elif event.type == game.KEYDOWN:
                if event.key == game.K_SPACE:
                    player.gravitySwitch()



        mouse = game.mouse.get_pos()

        surface.fill(blue)

        if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
            game.draw.rect(surface,lightGray,[0,0,30,20])
        else:
            game.draw.rect(surface,darkGray,[0,0,30,20])


        collide = player.rect.colliderect(redBox.rect)

        if collide:
            endGame()

        surface.blit(quitText,(0,0))
        allSprites.update()
        player.draw()
        frame += 1
        redBox.draw()
        ground.draw()
        game.display.update()

def endGame():
    global keepGoing
    while keepGoing:
        mouse = game.mouse.get_pos()
        for event in game.event.get():

            if event.type == game.MOUSEBUTTONDOWN:
                if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
                    game.quit()
                elif 175 <= mouse[0] <= 255 and 200 <= mouse[1] <= 220:
                    keepGoing = False

        if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
            game.draw.rect(surface,lightGray,[0,0,30,20])
            game.draw.rect(surface,darkGray,[175,200,80,20])
        elif 175 <= mouse[0] <= 255 and 200 <= mouse[1] <= 220:
            game.draw.rect(surface,darkGray,[0,0,30,20])
            game.draw.rect(surface,lightGray,[175,200,80,20])
        else:
            game.draw.rect(surface,darkGray,[0,0,30,20])
            game.draw.rect(surface,darkGray,[175,200,80,20])

        surface.blit(gameOver, (150,150))
        surface.blit(mainMenu, (175,205))
        surface.blit(startFont.render("Score: " + str(redBox.lap - 2), True, red),(175,175))
        surface.blit(quitText,(0,0))
        game.display.update()

#--- start loop ---

keepGoing = True
while True:
    while keepGoing:
        ticktock.tick(60)
        mouse = game.mouse.get_pos()
        for event in game.event.get():
            if event.type == game.MOUSEBUTTONDOWN:
                if 115 <= mouse[0] <= 255 and 130 <= mouse[1] <= 170:
                    start()
                elif 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
                    game.quit()

        surface.fill((0,0,255))


        if 115 <= mouse[0] <= 255 and 130 <= mouse[1] <= 170:
            game.draw.rect(surface,lightGray,[115,130,155,40])
            game.draw.rect(surface,darkGray,[0,0,30,20])
        elif 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
            game.draw.rect(surface,lightGray,[0,0,30,20])
            game.draw.rect(surface,darkGray,[115,130,155,40])
        else:
            game.draw.rect(surface,darkGray,[115,130,155,40])
            game.draw.rect(surface,darkGray,[0,0,30,20])

        surface.blit(startText, (120,135))
        surface.blit(quitText, (0,0))
        surface.blit(instructions, (100,200))

        game.display.update()
    keepGoing = True
    player = Player()
    redBox = Redbox()