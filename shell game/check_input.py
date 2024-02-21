def get_int(prompt):
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      valid = True
    except ValueError:
      print("Invalid input - should be an integer.")
  return val

def get_positive_int(prompt):
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      if val >= 0:
        valid = True
      else:
        print("Invalid input - should not be negative.")
    except ValueError:
      print("Invalid input - should be an integer.")
  return val  

def get_int_range(prompt, low, high):
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      if val >= low and val <= high:
        valid = True
      else:
        print("Invalid input - should be within range " + str(low) + "-" + str(high) + ".")
    except ValueError:
      print("Invalid input - should be an integer.")
  return val

def get_float(prompt):
  val = 0
  valid = False
  while not valid:
    try:
      val = float(input(prompt))
      valid = True
    except ValueError:
      print("Invalid input - should be a decimal value.")
  return val

def get_yes_no(prompt):
  valid = False
  while not valid:
    val = input(prompt).upper()
    if val == "YES" or val == "Y":
      return True
    elif val == "NO" or val == "N":
      return False
    else:
      print("Invalid input - should be a 'Yes' or 'No'.")
