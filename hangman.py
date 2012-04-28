#a hangman program

#imports the random module, allowing you to
#generate a random number, which will pull from a dictionary
#to use the word for the hangman program.
import random
#imports the string module, which allows me to use the Len() function to determine the length of the word chosen
import string
#this is the key (dictionary) we will use to pull words for our program.
dictionary={1:"stinkface", 2:"couches", 3:"blues", 4:"porkface", 5:"keyboard", 6:"computer", 7:"whales", 8:"catscratch", 9:"woman", 10:"mankind"}
#picks a random number between 1 and 10 that we will use to 
#call the word
choice=random.randint(1, 10)
#the variable 'word' as the word that corresponds to the number from the previous line
word=dictionary[choice]
#This is just a cheat for testing purposes. Uncomment the next line to see the word at the beginning of the program.
#print "ANSWER:", word
#title page
print '''





WELCOME TO JOSHs HANGING OF THE MEN!!






'''
#the following three lines prints one blank for each letter in the word, giving you a starting point, followed by an empy line (the "\n").
for x in word:
 print "_",
print "\n"
#the next three strings are set to empty strings, and will be used to store the user's input.
choices=""
badchoices=""
goodchoices=""
#'hangman' is a counter that will be used to display the right hangman
hangman=1
#win is the counter to determine when the player wins.
win=0
head= """\n\n\nHangman:\n
0 \n\n\n\n"""
body= """\n\n\nHangman:\n\n 0
 |
 |\n\n\n\n"""
arm1="""\n\n\nHangman:\n\n 0
/|
 |\n\n\n\n"""
arm2="""\n\n\nHangman:\n\n 0
/|\\
 |\n\n\n\n"""
leg1="""\n\n\nHangman:\n\n 0
/|\\
 |
/\n\n\n\n
"""
ALLDONE="""\n\n\nHangman:\n\n 0
/|\\
 |
/ \\
\n\n\n\n****GAME OVER!!!!****\n******YOU LOSE!!******\n\n\n\n
"""

#this is the main function of the program. it accepts input from the user
#and sets it to "pickletter". 
def letterentry():
 global pickletter
 pickletter=raw_input("\nEnter a letter or hit CTRL+Z to exit: ")
 global choices
#the following three lines keeps the user from entering a character
#they have already entered, or from entering a space, or from entering
#more than one character in one turn
 while pickletter in choices or len(pickletter)!=1 or pickletter==" ":
  print "Try another letter please."
  pickletter=raw_input("\nEnter a letter or hit CTRL+Z to exit: ")
#the next three lines assigns the user's input to the 'choices' variable
#and then runs a check on it (which will be explained further down).
 if pickletter not in choices:
  choices = choices + pickletter
  checks(pickletter)
#if the input is not in the word, calls the badmove function, basically
#increasing the amount of the hangman you have
  if pickletter not in word:
   badmove()
#if input is in the word, this function (goodmove()) takes you one step closer to winning.
  else:
   goodmove()
#the following two lines print a summary of the letters you've chosen
#divided into good choices and bad choices
 print "\nTHESE LETTERS ARE NOT IN THE WORD:", badchoices, "\n"
 print "THESE ARE GOOD LETTERS:", goodchoices, "\n\n", "==="*15

#this function adds a letter to the 'goodchoices' variable, 
#then prints out the word with the letters you've guessed 
#correctly printed out and the letters you havent guessed
#are printed as a blank
def checks(item):
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
 print "\n"

#this function increases the 'win' counter by 1 for each correct letter you've guessed.
def goodmove():
 global win
 global pickletter
 global choices
#this line was tricky for me. it goes through each letter in the word
#each turn and for each time the letter you guessed appears in the letter
#the 'win' counter is increased by one. (this is what
#makes words with double letters winnable)
 for x in word:
  if pickletter == x:
   win=win+1
#once you've guessed the right letters, you win!
 if win==len(word):
  print "\n\n\n**** YOU WIN!! ****\n\n\n"
  return

#for each time you guess a letter that's not in the word,
#this function increases the 'hangman' counter by one, bringing
#you closer to your lynching!
def badmove():
  global badchoices
  global choices
  choices=choices+pickletter
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

#as long as you haven't reached the proper counters for 'hangman'
#and 'win', this statement calls the letterentry() function.
#not sure why though the win has to be less than or 
#equal to the length of the word -1. oh well.
while hangman<=6 and win<=len(word)-1:
 letterentry()
