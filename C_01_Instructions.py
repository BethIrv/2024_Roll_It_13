# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        print()
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes / No")


def instruction():
    print('''
    
^^^ Instructions ^^^

Do something
and then do something else
etc
    
    ''')


# Main routine
print("🎲🎲 Roll it 13 🎲🎲")

# loop for testing purposes

print()
want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("Program continues")
