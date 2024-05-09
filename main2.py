import pygame
import sys
import random


pygame.init()

WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(260,300))
ICON = pygame.image.load("assets/Icon.png")

pygame.display.set_caption("Wordle!")
pygame.display.set_icon(ICON)

words =[] #a list storing all the words
LETTER_SIZE = 75
letters = '' # max 5 
POS_X = 335
POS_Y = 300
#POS_Y = 920

full = open('dictionary.txt','r')
words = full.read().split()
correct = random.choice(words)
clets = list(correct)
print(clets)


class Letter:

  def __init__(self, x, y, letter):
    self.x = x
    self.y = y
    self.letter = letter
    self.font = pygame.font.SysFont("comicsans", 100)
    self.text = self.font.render(self.letter, 1, (0, 0, 0))
    self.text_rect = self.text.get_rect(center=(self.x//4, self.y//6))


  def draw(self, screen):
    screen.blit(self.text, self.text_rect)


running = True
while running:


  SCREEN.fill((0,0,0))
  SCREEN.blit(BACKGROUND, BACKGROUND_RECT)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN and  event.unicode.isalpha():
      letters += event.unicode #added typed letter the list letters
    # if event.type == pygame.KEYDOWN and event.key == pygame.K_DELETE:
    #   print("deleting : " + letters )
    #   letters = letters[0:len(letters)-1] #deleted last letter from list letters


    character = []

    for i in letters:

      character.append(i)

    for i in range(len(character)):
      character[i] = Letter(POS_X + (i * 4.5* LETTER_SIZE) + 26 , POS_Y, character[i])
      print(character[i].letter, clets[i])
      if character[i].letter == clets[i]:
        character[i].text = character[i].font.render(character[i].letter, 1, (0, 255, 0))
      elif character[i].letter != clets[i] and character[i].letter in clets:
        character[i].text = character[i].font.render(character[i].letter, 1, (255, 255, 0))  
      else:
        character[i].text = character[i].font.render(character[i].letter, 1, (255, 0, 0))
      #print(character[i].text)

      character[i].draw(SCREEN)

    if len(letters) >= 5:
      letters = ""


      POS_Y += 620

    if POS_Y >= 3720:
      POS_Y = 300

      # POS_X = 335

    pygame.display.update()


pygame.quit()



