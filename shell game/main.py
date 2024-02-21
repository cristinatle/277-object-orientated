"""
Cristina Le
January 29, 2024
Shell Game: program that allows the user to bet money and guess which shell contains the ball

"""
import random
import check_input

def main():

  print("""
  -Shell Game-
  Find the ball to double your bet!
  """)
 
  current_amount = 100
  
  while current_amount > 0:
    print("You have $", current_amount)

    bet = check_input.get_int_range("Bet Amount? $ ", 1, current_amount)
    
    print ("""
       _____        _____        _____   
      /     \      /     \      /     \\
     /   1   \    /   2   \    /   3   \\
    /_________\  /_________\  /_________\\
    """)
    
    guess = check_input.get_int_range("Make a guess: ", 1, 3)
    ball_location = random.randint(1, 3)

    if ball_location == 1:
      print ("""
         _____        _____        _____   
        /     \      /     \      /     \\
       /   ○   \    /       \    /       \\
      /_________\  /_________\  /_________\\
      """)

    if ball_location == 2:
      print ("""
         _____        _____        _____   
        /     \      /     \      /     \\
       /       \    /   ○   \    /       \\
      /_________\  /_________\  /_________\\
      """)

    if ball_location == 3:
      print ("""
         _____        _____        _____   
        /     \      /     \      /     \\
       /       \    /       \    /   ○   \\
      /_________\  /_________\  /_________\\
      """)

    if guess == ball_location:
      print("Congratulations!")
      current_amount += bet
    
    else: 
      print("Sorry...you lose.")
      current_amount -= bet
      
      if current_amount == 0:
        print("You're out of money! Game Over.")
        break

    again = check_input.get_yes_no("Play Again? (Y/N): ")
    
    if again == False:
      break
      
main()
