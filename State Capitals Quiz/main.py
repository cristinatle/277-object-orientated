"""
Cristina Le
Febuary 12, 2024
This program simulates a state capitals quiz with 10 questions, 
where the user will be asked to asnwer 10 multiple choice questions. 
They will answer the question with what they think the capital of 
the random state is. 
"""
import random
"""This function will open the file and read the file. It will also make two list one for states and one for capitals. It will then return the two lists."""
def read_file(file_name):
  file = open(file_name)
  lines = file.readlines()
  all_states_capitals = []
  
  for line in lines:
    line = str(line)
    state_capital = line.split(",")
    all_states_capitals.append(state_capital)

  return all_states_capitals
"""This function will take the two lists and randomly select a state and capital from the list. It will then return the state and capital."""

def get_random_states(states):
  answer = random.choice(states)
  return answer

def get_random_choices(states, correct_capital):
  all_states = []
  all_capitals = []
  for i in range(len(states)):
    all_states.append(states[i][0])
    all_capitals.append(states[i][1])
  
  all_capitals.remove(correct_capital)
  
  capital_choices = []
  remaining_capitals = 49
  
  while len(capital_choices) < 3:
    i = random.randint(0, remaining_capitals-1)
    capital_choices.append(all_capitals[i])
    all_capitals.remove(all_capitals[i])
    remaining_capitals -= 1

  capital_choices.append(correct_capital)
  random.shuffle(capital_choices)
  
  return capital_choices
  """This sets up the question and the answer choices. It will then return the question and answer choices. It will also make sure the user doesn't pick an invaild answer choice."""

def ask_question(correct_state, possible_answers):
  print("The capital of", correct_state[0], "is:\n") 

  print(f" A.{possible_answers[0]} B.{possible_answers[1]} C.{possible_answers[2]} D.{possible_answers[3]}", end="")
  
  user_selection = input("Enter selection:")
  user_selection = user_selection.upper()
  
  while user_selection not in ["A", "B", "C", "D"]:
    print ("Invalid input. Input choice A-D.")
    user_selection = input("Enter selection: ")
    user_selection = user_selection.upper()
    
  ans_dict = {'A': '0', 'B': '1', 'C': '2', 'D': '3'}
  user_selection = ans_dict[user_selection]
  
  return user_selection
"""This function will take the user's answer and the correct answer and see if they are correct. If they are correct, it adds a point to their score. If they are incorrect, it will tell them the correct answer."""
def main():
  print ("- State Captials Quiz -")
  q_num = 1
  correct = 0
  while q_num < 11:
    all_states_capitals = read_file("statecapitals.txt")
    answer = get_random_states(all_states_capitals)
    capital_choices = get_random_choices(all_states_capitals, answer[1])
    
    if capital_choices[0] == answer[1]:
      correct_choice = "0"
    elif capital_choices[1] == answer[1]:
      correct_choice = "1"
    elif capital_choices[2] == answer[1]:
      correct_choice = "2"
    elif capital_choices[3] == answer[1]:
      correct_choice = "3"
  
    print(str(q_num) + ". ", end = "")
    user_selection = ask_question(answer, capital_choices)
    if user_selection == correct_choice:
      print("Correct!\n")
      correct += 1
    else:
      print("Incorrect! The correct answer is:", answer[1])
    q_num += 1
  
  print ("End of test. You got", correct, "correct.")

main()
