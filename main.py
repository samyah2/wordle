import random
from colorama import Fore
#full = open dictioanry file
full = open('dictionary.txt','r')
#words = words.read().split()
words = full.read().split()
print(words)
correct = random.choice(words)

guess = input().lower()
while len(guess) != 5:
    guess = input().lower()
emptyc = list(correct)
emptyg = list(guess)
print(emptyc, emptyg)

print(guess)
'''
bug: if there isn't multiple uses of one letter in the word, letter should be red, not yellow
'''
for k in range(5):
    if guess[k] == correct[k]:
      print(f"{Fore.GREEN}{guess[k]}", end=' ')
    elif guess[k] != correct[k] and guess[k] in emptyc:
      print(f"{Fore.YELLOW}{guess[k]}", end=' ')  
    else:
      print(f"{Fore.RED}{guess[k]}", end=' ')
      

