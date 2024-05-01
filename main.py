import random
from colorama import Fore
import pygame
import sys
import random


# pygame.init()

# # Constants
# WIDTH, HEIGHT = 600, 600
# SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
# BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
# BACKGROUND_RECT = BACKGROUND.get_rect(center=(260, 300))
# ICON = pygame.image.load("assets/Icon.png")

# pygame.display.set_caption("Wordle!")
# pygame.display.set_icon(ICON)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     SCREEN.fill("white")
#     SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
#     pygame.display.update()

# pygame.quit()

full = open('dictionary.txt','r')
words = full.read().split()
print(words)

play_again = ''

while play_again != 'q':
  correct = random.choice(words)

  for z in range(5):
    guess = input().lower()
    while len(guess) != 5:
      guess = input().lower()
    emptyc = list(correct)
    emptyg = list(guess)
    # print(emptyc, emptyg)

    # print(guess)
  # '''
  # bug: if there isn't multiple uses of one letter in the word, letter should be red, not yellow
  # '''
    for k in range(5):
      if guess[k] == correct[k]:
        print(f"{Fore.GREEN}{guess[k]}", end = ' ')
      elif guess[k] != correct[k] and guess[k] in emptyc:
        print(f"{Fore.YELLOW}{guess[k]}", end = ' ')  
      else:
        print(f"{Fore.RED}{guess[k]}", end = ' ')
    print()
    if guess == correct:
      break
  play_again = input('\nDo you want to play wordle? Click \'q\' if no. ')

  
      