import os
import sys
import engine

# Overall approach: show a message, then show choices,
#   then respond to choices

while 1:

    # Start the adventure.
    os.system('clear')
    message = "You are standing at the entrance to the new Pacific High School."

    choices = {}
    choices['1'] = "Enter."
    choices['2'] = "Turn around and jump into the water."

    print(message)
    choice = engine.get_choice(choices)


    # Respond to first choice.
    if choice == '1':
        os.system('clear')
        
        phs_values = ['honesty', 'perseverance', 'humor', 'acceptance', 'respect']
        key = ''
        while key.lower() not in phs_values:
            os.system('clear')
            print("You must know one of the five secrets in order to enter.")
            key = input("Please tell me one of the secrets: ")
        
        # You know the secret!
        os.system('clear')
        
        
        print("You have entered!")
        print("You notice that there is new paint on the walls.")
        print("Would you like to: ")
        print("\n[1] Open the door to Hillary's classroom.")
        print("[2] Go sit by Phil's desk.")
        print("[3] Go into Eric's class to do some Python.")
        choice = input("\nWhat is your choice? ")
        if choice == '1':
    	    os.system('clear')
    	    print("A British-sounding woman has just shouted at you.")
        elif choice == '2':
    	    # phil's desk
    	    os.system('clear')
    	    print("You are standing in front of Phil's desk.")
    	    print("Phil is talking on the phone about giraffes in the sky.")
    	    print("Would you like to: ")
    	    print("\n[1]Keep listening for a while.")
    	    print("[2]Interrupt Phil's conversation.")
    	    print("[3]Quietly sneak a Hames pass off of Phil's desk.")
    	    choice = input("\nWhat is your choice?")
        elif choice == '3':
    	    # eric's room
    	    pass
        else:
    	    print("I don't understand.")
    elif choice == '2':
        os.system('clear')
        print("You drowned! Just kidding.")
        print("You are now riding a dolphin.")
        print("Would you like to: ")
        print("\n[1] Head towards the magical underwater kingdom of Zubida.")
        print("\n[2] Head towards a magical land far, far away from here.")
        choice = input("\nWhat is your choice? ")
    else:
        print("I don't understand your choice.")
