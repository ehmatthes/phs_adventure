# PHS Adventure
#  You never know where you'll end up.
import os
import sys	

# --- Scenes and choices. ---

# Define the opening scene.
situation_1 = "You are standing at the front door of PHS."
choice_1 = "Open the door."
choice_2 = "Turn around."

# Define next situations and choices.
situations = {}

# After choice_1. "Open the door."
situation_2 = "Phil greets you warmly."
choice_3 = "Greet Phil, and continue into the rotunda."
choice_4 = "Turn around and walk out."

# situations[current choice] = [new situation, two new choices]
situations[choice_1] = [situation_2, choice_3, choice_4]

# After choice_2.
situation_3 = "A dark cloud appears overhead."
choice_5 = choice_1
choice_6 = "Leave school anyways."
situations[choice_2] = [situation_3, choice_5, choice_6]

# After choice_3. "Greet Phil, and continue into the rotunda."
situation_4 = "You see two students arguing, and an open classroom door."
choice_7 = "Call for Phil!"
choice_8 = "Approach the students yourself."
situations[choice_3] = [situation_4, choice_7, choice_8]

# After choice_8. "Approach the students yourself."
situation_5 = "The two students are arguing loudly, using derogatory language. They seem to be escalating."
choice_9 = "You continue to watch in silence."
choice_10 = "You decide to say something."
situations[choice_8] = [situation_5, choice_9, choice_10]

# --- END scenes and choices. ---


# --- Functions ---

def show_scene(description, choices):
	"""Show a scene and choices, return choice."""
	os.system('cls')
	
	print(description)
	print('\nWhat would you like to do?')
	for index, choice in enumerate(choices):
		print(str(index) + ": " + choice)
	response = input("\n\n0, 1, or q: ")
	
	if response == 'q':
		sys.exit()
	else:
		return choices[int(response)]
		
# --- Game logic ---

# Present first choice.
try:
	choice = show_scene(situation_1, (choice_1, choice_2))
except IndexError:
	# Bad approach, but works.
	choice = show_scene(situation_1, (choice_1, choice_2))

# Loop through all other scenes and choices.
while choice != 'q':
	try:
		choice = show_scene(situations[choice][0],
			(situations[choice][1], situations[choice][2]))
	except KeyError:
		choice = choice_1
	except IndexError:
		continue
