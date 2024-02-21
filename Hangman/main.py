"""
Cristina Le
Febuary 6, 2024
Hangman Game: users are able to guess a radom 5 letter word, they have 6 guesses before the hangman will be complete and the game will end (the user loses). If the user is able to correctly guess before the hangman is finished they will win.

"""
import check_input
import dictionary
import random
from dictionary import words
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def display_gallows(num_incorrect):
  '''This creates the base drawing of the hangman and adds the correct body parts based 
on the number of incorrect guesses.'''
  if num_incorrect == 0:
    print ("""
  ========
  |  |/  |
  |  |
  |  |
  |  |
  |  |
  """)
  elif num_incorrect == 1:
    print ("""
  ========
  |  |/  |
  |  |   o
  |  |
  |  |
  |  |
  """)
  elif num_incorrect == 2:
    print ("""
  ========
  |  |/  |
  |  |   o
  |  |   |
  |  |
  |  |
  """)
  elif num_incorrect == 3:
    print ("""
  ========
  |  |/  |
  |  |   o
  |  |   |
  |  |  /
  |  |
  """)
  elif num_incorrect == 4:
    print ("""
  ========
  |  |/  |
  |  |   o
  |  |   |
  |  |  / \\
  |  |
  """)
  elif num_incorrect == 5:
    print ("""
  ========
  |  |/  |
  |  |  \\o
  |  |   |
  |  |  / \\
  |  |
  """)
  elif num_incorrect == 6:
    print ("""
========
|  |/  |
|  |  \\o/
|  |   |
|  |  / \\
|  |
""")

def display_letters(letters):
  '''This function displays the letters that have been guessed so far.'''
  for item in letters:
    print(item, end=" ")
  print("\n")

def get_letters_remaining(incorrect, correct):
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  
  for x in incorrect:
    if x in alphabet:
      alphabet.remove(x)
      
  for i in correct:
    if i in alphabet:
      alphabet.remove(i)

  print("Letters Remaining:", end=" ")
  display_letters(alphabet)

def main():
  '''Main function of the game that inititates and manages Hangman. 
It asks users to make a guess and checks if the guess is correct or not.'''
  
  play = True
  while play == True:
    print ("-Hangman-")
    random_word = dictionary.words[random.randint(0, len(dictionary.words))]
    #print(random_word)
    num_correct = 0
    num_incorrect = 0
    final_guess = ['_','_','_','_','_']
    correct_guesses = ['']
    incorrect_guesses = ['']
    answer = []

    for char in random_word:
      answer.append(char)
    
    while num_correct <= 5 and num_incorrect <= 6:
      print ("Incorrect selections: ", end = ' ')
      display_letters(incorrect_guesses)
      display_gallows(num_incorrect)
      display_letters(final_guess)
      (get_letters_remaining(incorrect_guesses, correct_guesses))
      
      user_guess = input("Enter a letter: ")
      user_guess = user_guess.upper()
      
      while user_guess not in abc or len(user_guess) != 1:
        print('That is not a letter.')
        user_guess = input("Enter a letter: ")
        user_guess = user_guess.upper()
        
      if user_guess in correct_guesses or user_guess in incorrect_guesses:
        print('You already guessed that letter.\n')
        continue
      
      if not user_guess.isalpha():
        print("That is not a letter.\n")
      
      else:
        user_guess = user_guess.upper()
        for i in range(len(answer)):
          if user_guess == answer[i]:
            final_guess[i] = user_guess
            
      if user_guess in answer:
        correct_guesses.append(user_guess)
        num_correct += 1
        print("Correct!\n")
        if num_correct == 5:
          if num_correct == 5:
            display_gallows(num_incorrect)
            display_letters(final_guess)
            print("You win!")
          break 
              
      else:
        incorrect_guesses.append(user_guess)
        num_incorrect += 1
        print("Incorrect!\n")
        if num_incorrect == 6:
          if '_' in final_guess:
            display_gallows(num_incorrect)
            display_letters(final_guess)
            print("You lose!")
            print(f'The word was: {random_word}')
          break
          

      if '_' not in final_guess:
        display_gallows(num_incorrect)
        display_letters(final_guess)
        print("You win!")
        break
    
    again = check_input.get_yes_no("Play Again? (Y/N): ")
    if again == False:
        break
    
      
main()
