#a hangman program

#imports the random module, allowing you to
#generate a random number, which will pull from a dictionary
#to use the word for the hangman program.
import random
import string
#this is the key (dictionary) we will use to pull words for our program.
dictionary={1:"stinkface", 2:"couches", 3:"blues", 4:"porkface", 5:"keyboard", 6:"computer", 7:"whales", 8:"catscratch", 9:"woman", 10:"mankind"}
choice=random.randint(1, 10)
word=dictionary[choice]
print "ANSWER:", word
print '''





           WELCOME TO JOSHs HANGING OF THE MEN!!






'''
for x in word:
 print "_",

choices=""
badchoices=""
hangman=1
goodchoices=""
win=1
head= """\n\n\nHangman:\n
   0   \n\n\n\n"""
body= """\n\n\nHangman:\n\n  0
  |
  |\n\n\n\n"""
arm1="""\n\n\nHangman:\n\n  0
 /|
  |\n\n\n\n"""
arm2="""\n\n\nHangman:\n\n  0
 /|\\
  |\n\n\n\n"""
leg1="""\n\n\nHangman:\n\n  0
 /|\\
  |
 /\n\n\n\n
"""
ALLDONE="""\n\n\nHangman:\n\n  0
 /|\\
  |
 / \\ 
\n\n\n\n****GAME OVER!!!!****\n******YOU LOSE!!******\n\n\n\n
"""



def letterentry():
 global pickletter
 pickletter=raw_input("\n\nEnter a letter or hit CTRL+Z to exit: ")
 def checks(pickletter):
  print "\n"
  for x in word:
   if pickletter in x and choices:
    global goodchoices
    goodchoices=goodchoices+pickletter
    print pickletter,
   elif x in choices:
    print x,
   else:
    print "_",
 global choices
 choices = choices + pickletter
 if pickletter not in word:
  checks(pickletter)
  badmove()
 else: 
  checks(pickletter)
  goodmove()
 print "\n\nTHESE LETTERS ARE NOT IN THE WORD:", badchoices, "\n"
 print "THESE ARE GOOD LETTERS:", goodchoices, "\n\n\n", "==="*15


def goodmove():
 global win
 global pickletter
 global choices
 if pickletter in choices:
  win=win
 elif pickletter in word:
  win=win+1
 if win==len(word)+1:
  print "\n\n\n**** YOU WIN!! ****\n\n\n"
def badmove():
  global badchoices
  badchoices=badchoices + pickletter
  global hangman
  if hangman==1:
   print head
  elif hangman==2:
   print body
  elif hangman==3:
   print arm1
  elif hangman==4:
   print arm2
  elif hangman==5:
   print leg1
  elif hangman==6:
   print ALLDONE
  hangman=hangman+1

while hangman<=6 and win<=len(word):
 letterentry()











































