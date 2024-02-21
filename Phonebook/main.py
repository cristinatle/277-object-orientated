"""
Cristina Le
Febuary 19, 2024
Address book: Allows user to look up a contact list to find a contact's information such as zip code, phone number, name, address, and city after entering the contact's name and information.
"""
from contact import Contact
import check_input

def read_file():
  with open("addresses.txt") as file:
    contacts = []
    for line in file:
      line = line.strip()
      address = line.split(",")
      new_contact = Contact(address[0], address[1], address[2], address[3], address[4], address[5])
      contacts.append(new_contact)
    contacts.sort()
    return contacts

def write_file(contacts):
  with open("addresses.txt", "w") as file:
    for contact in contacts:
      file.write(Contact.__repr__(contact))
      file.write('\n')
  
def get_menu_choice():
  print("""
Rolodex Menu:
1. Display all contacts
2. Add Contact
3. Search Contacts
4. Modify Contact
5. Save and Quit
  """)
  choice = check_input.get_int_range("> ", 1, 5)
  return choice

def modify_contact(con):
  while True:
    print ("""
Modify Menu:
1. First Name
2. Last Name
3. Phone Number
4. Address
5. City
6. Zip
7. Save""")
    search_choice = check_input.get_int_range("> ", 1, 7)
    if search_choice == 1:
      new_fn = input("Enter New First Name: ")
      con.first_name = new_fn
    elif search_choice == 2:
      new_ln = input("Enter New Last Name: ")
      con.last_name = new_ln
    elif search_choice == 3:
      new_ph = input("Enter New Phone #: ")
      con.phone_number = new_ph
    elif search_choice == 4:
      new_addr = input("Enter New Address: ")
      con.address = new_addr
    elif search_choice == 5:
      new_city = input("Enter New City: ")
      con.city = new_city
    elif search_choice == 6:
      new_zip = input("Enter New Zip: ")
      con.zip_code = new_zip
    elif search_choice == 7:
      print("edits saved.")
      break
  return con
    
def main():
  user_contacts = read_file()
  while True:
    user_choice = get_menu_choice()
    if user_choice == 1:
      print("Contacts:", len(user_contacts))
      count = 1
      for contact in user_contacts:
        print(f"{count}. {Contact.__str__(contact)}")
        count += 1
  
    elif user_choice == 2:
      print("Enter new contact:")
      fn = input("First name: ")
      ln = input("Last name: ")
      ph = input("Phone #: ")
      addr = input("Address: ")
      city = input("City: ")
      zip = input("Zip: ")
      new_contact = Contact(fn, ln, ph, addr, city, zip)
      user_contacts.append(new_contact)
      user_contacts.sort()
      
    elif user_choice == 3:
      print ("1. Search by last name")
      print ("2. Search by zip code")
      search_choice = input("> ")
      if search_choice == "1":
        ln = input("Enter last name: ")
        ln_count = 0 #use counter instead of else to avoid loop of repeated response
        for contact in user_contacts: #iterate through all Contact objects in in user_contacts matrix
          if ln == contact.last_name:
            ln_count += 1
            print(Contact.__str__(contact))
        if ln_count == 0:
          print(f"No contacts with last name, {ln}, found.")
      elif search_choice == "2":
        zip = input("Enter zip code: ")
        zip_count = 0 
        for contact in user_contacts:
          if zip == contact.zip_code:
            print(Contact.__str__(contact))
            zip_count += 1
        if zip_count == 0:
          print(f"No contacts with zip code {zip} found.")
      
    elif user_choice == 4:
      first_name = input("Enter first name: ")
      last_name = input("Enter last name: ")
      for contact in user_contacts:
        if first_name == contact.first_name and last_name == contact.last_name:
          print("\n")
          print(f"{Contact.__str__(contact)}")
          updated_contact = modify_contact(contact)
      user_contacts.sort()
    
    elif user_choice == 5:
      print("Saving File...")
      write_file(user_contacts)
      print("File Saved. Ending Program")
      break
      
main()
