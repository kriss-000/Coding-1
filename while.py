# Set an initial condition.
game_active = True
# Set up the while loop.
while game_active:
# Run the game.
# At some point, the game ends and game_active will be set to False.
# When that happens, the loop will stop executing.
# Do anything else you want done after the loop runs.
# The player's power starts out at 5.
power = 5
# The player is allowed to keep playing as long as their power is over 0.
while power > 0:
print("You are still playing, because your power is %d." % power)
# Your game code would go here, which includes challenges that make it
# possible to lose power.
# We can represent that by just taking away from the power.
power = power - 1
print("\nOh no, your power dropped to 0! Game Over.")
# Get some input from the user.
variable = input('Please enter a value: ')
# Do something with the value that was entered.
# Start with a list containing several names.
names = ['guido', 'tim', 'jesse']
# Ask the user for a name.
new_name = input("Please tell me someone I should know: ")
# Add the new name to our list.
names.append(new_name)
# Show that the name has been added to the list.
print(names)
# The same program, in Python 2.7
# Start with a list containing several names.
names = ['guido', 'tim', 'jesse']
# Ask the user for a name.
new_name = raw_input("Please tell me someone I should know: ")
# Add the new name to our list.
names.append(new_name)
# Show that the name has been added to the list.
print(names)
# Start with an empty list. You can 'seed' the list with
# some predefined values if you like.
names = []
# Set new_name to something other than 'quit'.
new_name = ''
# Start a loop that will run until the user enters 'quit'.
while new_name != 'quit':
# Ask the user for a name.
new_name = input("Please tell me someone I should know, or enter 'quit': ")
# Add the new name to our list.
names.append(new_name)
# Show that the name has been added to the list.
print(names)
# Start with an empty list. You can 'seed' the list with
# some predefined values if you like.
names = []
# Set new_name to something other than 'quit'.
new_name = ''
# Start a loop that will run until the user enters 'quit'.
while new_name != 'quit':
# Ask the user for a name.
new_name = input("Please tell me someone I should know, or enter 'quit': ")
# Add the new name to our list.
if new_name != 'quit':
names.append(new_name)
# Show that the name has been added to the list.
print(names)
# Give the user some context.
print("\nWelcome to the nature center. What would you like to do?")
# Set an initial value for choice other than the value for 'quit'.
choice = ''
# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
# Give all the choices in a series of print statements.
print("\n[1] Enter 1 to take a bicycle ride.")
print("[2] Enter 2 to go for a run.")
print("[3] Enter 3 to climb a mountain.")
print("[q] Enter q to quit.")
# Ask for the user's choice.
choice = input("\nWhat would you like to do? ")
# Respond to the user's choice.
if choice == '1':
print("\nHere's a bicycle. Have fun!\n")
elif choice == '2':
print("\nHere are some running shoes. Run fast!\n")
elif choice == '3':
print("\nHere's a map. Can you leave a trip plan for us?\n")
elif choice == 'q':
print("\nThanks for playing. See you later.\n")
else:
print("\nI don't understand that choice, please try again.\n")
# Print a message that we are all finished.
print("Thanks again, bye now.")
# Define the actions for each choice we want to offer.
def ride_bicycle():
print("\nHere's a bicycle. Have fun!\n")
def go_running():
print("\nHere are some running shoes. Run fast!\n")
def climb_mountain():
print("\nHere's a map. Can you leave a trip plan for us?\n")
# Give the user some context.
print("\nWelcome to the nature center. What would you like to do?")
# Set an initial value for choice other than the value for 'quit'.
choice = ''
# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
# Give all the choices in a series of print statements.
print("\n[1] Enter 1 to take a bicycle ride.")
print("[2] Enter 2 to go for a run.")
print("[3] Enter 3 to climb a mountain.")
print("[q] Enter q to quit.")
# Ask for the user's choice.
choice = input("\nWhat would you like to do? ")
# Respond to the user's choice.
if choice == '1':
ride_bicycle()
elif choice == '2':
go_running()
elif choice == '3':
climb_mountain()
elif choice == 'q':
print("\nThanks for playing. See you later.\n")
else:
print("\nI don't understand that choice, please try again.\n")
# Print a message that we are all finished.
print("Thanks again, bye now.")
# Start with a list of unconfirmed users, and an empty list of confirmed users.
unconfirmed_users = ['ada', 'billy', 'clarence', 'daria']
confirmed_users = []
# Work through the list, and confirm each user.
while len(unconfirmed_users) > 0:
# Get the latest unconfirmed user, and process them.
current_user = unconfirmed_users.pop()
print("Confirming user %s...confirmed!" % current_user.title())
# Move the current user to the list of confirmed users.
confirmed_users.append(current_user)
# Prove that we have finished confirming all users.
print("\nUnconfirmed users:")
for user in unconfirmed_users:
print('- ' + user.title())
print("\nConfirmed users:")
for user in confirmed_users:
print('- ' + user.title())
# Start with a list of unconfirmed users, and an empty list of confirmed users.
unconfirmed_users = ['ada', 'billy', 'clarence', 'daria']
confirmed_users = []
# Work through the list, and confirm each user.
while len(unconfirmed_users) > 0:
# Get the latest unconfirmed user, and process them.
current_user = unconfirmed_users.pop(0)
print("Confirming user %s...confirmed!" % current_user.title())
# Move the current user to the list of confirmed users.
confirmed_users.append(current_user)
# Prove that we have finished confirming all users.
print("\nUnconfirmed users:")
for user in unconfirmed_users:
print('- ' + user.title())
print("\nConfirmed users:")
for user in confirmed_users:
print('- ' + user.title())
current_number = 1
# Count up to 5, printing the number each time.
while current_number <= 5:
print(current_number)
current_number = 1
# Count up to 5, printing the number each time.
while current_number <= 5:
print(current_number)
current_number = current_number + 1
current_number = 1
# Count up to 5, printing the number each time.
while current_number <= 5:
print(current_number)
current_number = current_number - 1