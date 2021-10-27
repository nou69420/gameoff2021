#--- Import modules ---
import pygame as game
import sys

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
quitText = quitFont.render('quit', True, red)

#--- classes ---
class Player(game.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.image = game.Surface((50,50))
    self.image.fill(green)
    
    self.rect = self.image.get_rect()
    self.rect.x = 0
    self.rect.y = 150
    self.isJumping = False
    self.jumpCount = 10
    
  # Draws the player on the screen and updates it
  def draw(self):
    self.rect.y = 0
    self.rect.bottom = ground.rect.top
    self.isJumping = False
    surface.blit(self.image, self.rect)

  # Function for jumping
  def jumpTick(self):
    #if self.isJumping:


  # Moves player to the left by 1 step
  def moveLeft(self):
    self.rect.x -= 1

  # Moves player to the right by 1 step
  def moveRight(self):
    self.rect.x += 1


class Ground(game.sprite.Sprite):
  def __init__(self):
    super(Ground, self).__init__()
    self.image = game.Surface((400,80))
    self.image.fill(darkGreen)
    self.rect = self.image.get_rect()
    self.rect.x = 0
    self.rect.y = 250
  
  def draw(self):
    surface.blit(self.image, self.rect)

  


#--- sprites and objects ---
allSprites = game.sprite.Group()
player = Player()
allSprites.add(player)
ground = Ground()
allSprites.add(ground)
ticktock = game.time.Clock()

#--- Game Functions ---
def start():
  print("started")
  
  while(True):
    ticktock.tick(120)
    for event in game.event.get():
      if event.type == game.KEYDOWN:
        if event.key == game.K_UP:
          player.isJumping = True

      if event.type == game.MOUSEBUTTONDOWN:
        if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
          game.quit()

    # Detects which keys are held down
    keys = game.key.get_pressed()
    if keys[game.K_LEFT]:
      player.moveLeft()
    elif keys[game.K_RIGHT]:
      player.moveRight()
    


    mouse = game.mouse.get_pos()
    
    surface.fill(blue)

    if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
      game.draw.rect(surface,lightGray,[0,0,30,20])
    else:
      game.draw.rect(surface,darkGray,[0,0,30,20])
    
    surface.blit(quitText,(0,0))
    allSprites.update()
    player.jumpTick()
    player.draw()
    ground.draw()
    game.display.update()
    
  

#--- start loop ---

while True:
  ticktock.tick(60)
  for event in game.event.get():
    if event.type == game.MOUSEBUTTONDOWN:
      if 115 <= mouse[0] <= 255 and 130 <= mouse[1] <= 170:
         start()
      elif 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
        game.quit()
  
  surface.fill((0,0,255))
  mouse = game.mouse.get_pos()
  

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

  game.display.update()