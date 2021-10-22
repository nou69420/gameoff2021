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

#--- Texts ---
startFont = game.font.SysFont('Corbel', 30)
startText = startFont.render('Click to start', True, green)
quitFont = game.font.SysFont('Corbel', 15)
quitText = quitFont.render('quit', True, red)

#--- classes ---
class Player(game.sprite.Sprite):
  def __init__(self):
    game.sprite.Sprite.__init__(self)
    self.image = game.Surface((50,50))
    self.image.fill(green)
    self.rect = self.image.get_rect()
  
  def moveLeft(self):
    self.rect.x += 5
    if self.rect.left > 400:
      self.rect.right = 0

#--- sprites ---
allSprites = game.sprite.Group()
player = Player()
allSprites.add(player)

#--- Game Functions ---
def start():
  print("started")
  while(True):
    for event in game.event.get():
      if event.type == game.KEYDOWN:
        if event.key == game.K_RIGHT:
          player.moveLeft()
      
      if event.type == game.MOUSEBUTTONDOWN:
        if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
          game.quit()
    
    if 0 <= mouse[0] <= 30 and 0 <= mouse[1] <= 20:
      game.draw.rect(surface,lightGray,[0,0,30,20])
    else:
      game.draw.rect(surface,darkGray,[0,0,30,20])
    
  

#--- start loop ---

while True:
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