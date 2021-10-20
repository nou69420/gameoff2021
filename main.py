#--- Import modules ---
import pygame as game
import sys

#--- Start display ---
game.init()
surface = game.display.set_mode((400,300))

#--- color variables ---
lightGray = (170,170,170)
darkGray = (100,100,100)
startColor = (0,255,0)

#--- Texts ---
startFont = game.font.SysFont('Corbel', 35)
startText = startFont.render('Click to start', True, startColor)

#--- Game Functions
def start():
  print("started")
  game.quit()

#--- Main Loop ---

while True:
  for event in game.event.get():
    if event.type == game.MOUSEBUTTONDOWN:
      if 115 <= mouse[0] <= 255 and 130 <= mouse[1] <= 170:
         start()
  
  surface.fill((0,0,255))
  mouse = game.mouse.get_pos()
  
  if 115 <= mouse[0] <= 255 and 130 <= mouse[1] <= 170:
    game.draw.rect(surface,lightGray,[115,130,155,40])
  else:
    game.draw.rect(surface,darkGray,[115,130,155,40])
  
  surface.blit(startText, (120,135))

  game.display.update()