import random
#from colorama import Fore
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

LETTER_SIZE = 75
letters = 'STRON' # max 5 
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

contents = []
LETTERS = ''

running = True
while running:


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN and event.unicode.isalpha():
        LETTERS += event.unicode
        # if event.key == pygame.K_h:
        #   contents.append('h')
        # elif event.key == pygame.K_e:
        #   contents.append('e')
        # elif event.key == pygame.K_l:
        #   contents.append('l')
        # elif event.key == pygame.K_o:
        #   contents.append('o')
        # contents.append(event.unicode)
        # print(event.unicode)
        # if len(contents) >= 5:
        #   #character = [0*len(contents)]
        #   for k in range(5):
        #     contents[k] = Letter(POS_X + (k * 4.5* LETTER_SIZE) + 26 , POS_Y, contents[k])
        #     # if contents[k] == clets[k]:
        #     contents[k].text = contents[k].font.render(contents[k].letter, 1, (0, 255, 0))
        #     print(contents[k].text)
        #     # elif contents[k] != clets[k] and contents[k] in clets:
        #     #   contents[k].text = contents[k].font.render(contents[k].letter, 1, (255, 255, 0))  
        #     # else:
        #     #   contents[k].text = contents[k].font.render(contents[k].letter, 1, (255, 0, 0))
        #     contents[k].draw(SCREEN)
        #     print()
        character = []

        for i in letters:

            character.append(i)

        for i in range(len(character)):
            character[i] = Letter(POS_X + (i * 4.5* LETTER_SIZE) + 26 , POS_Y, character[i])
        


            character[i].draw(SCREEN)

        if len(LETTERS) > 5:
            LETTERS = ""

  #play_again = input('\nDo you want to play wordle? Click \'q\' if no. ')

  SCREEN.fill((0,0,0))
  SCREEN.blit(BACKGROUND, BACKGROUND_RECT)



  # character = []

  # for i in letters:

  #   character.append(i)

  # for i in range(len(character)):
  #   character[i] = Letter(POS_X + (i * 4.5* LETTER_SIZE) + 26 , POS_Y, character[i])
  #   #if letter correct color respective colors if statements (character[i].text = color)
  #   #character[i].text = character[i].font.render(character[i].letter, 1, (0, 250, 0))
  #   character[i].draw(SCREEN)

    

  # word = Letter(POS_X, POS_Y,letters)
  # word.draw(SCREEN)

  pygame.display.update()

print(contents)
pygame.quit()


# full = open('dictionary.txt','r')
# words = full.read().split()
# print(words)

# play_again = ''

# while play_again != 'q':
#   correct = random.choice(words)

  # for z in range(5):
  #   guess = input().lower()
  #   while len(guess) != 5:
  #     guess = input().lower()
  #   emptyc = list(correct)
  #   emptyg = list(guess)
  #   # print(emptyc, emptyg)

#     # print(guess)
#   # '''
#   # bug: if there isn't multiple uses of one letter in the word, letter should be red, not yellow
#   # '''
  #   for k in range(5):
  #     if guess[k] == correct[k]:
  #       print(f"{Fore.GREEN}{guess[k]}", end = ' ')
  #     elif guess[k] != correct[k] and guess[k] in emptyc:
  #       print(f"{Fore.YELLOW}{guess[k]}", end = ' ')  
  #     else:
  #       print(f"{Fore.RED}{guess[k]}", end = ' ')
  #   print()
  #   if guess == correct:
  #     break
  # play_again = input('\nDo you want to play wordle? Click \'q\' if no. ')