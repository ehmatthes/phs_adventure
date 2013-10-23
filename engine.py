# Functions for PHS Adventure.

def get_choice(choices):
    # This function takes in a dictionary of choices,
    #   and returns the user's choice.
    # The dictionary has the form:
    #   {'choice_token': 'choice text', }
    # The function forces the user to make one of the given choices,
    #   or quit.
    print("\nWould you like to: ")
    for choice_token in choices:
        print("[%s]: %s" % (choice_token, choices[choice_token]))
    # Always offer the choice to quit.
    print("[q]: Quit.")
    choice_token = ''
    while choice_token not in choices.keys():
        choice_token = input("\nWhat is your choice? ")
        choice_token = str(choice_token)
        if choice_token == 'q':
            print("Thanks for playing! Bye.")
            sys.exit()
    return choice_token
