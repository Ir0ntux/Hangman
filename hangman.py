def main():
	print("Welcome to HANGMAN!")
	game_mode()

def game_mode():
	players = int(input("Enter (1) for Single Player Mode or (2) for Two Player Mode: "))
	if players == 1:
		single_player()
	elif players == 2:
		two_player()
	else:
		print("Incorrect entry! Enter 1 for single player mode or 2 for two player mode")

def single_player():
	print("Welcome to Single Player Mode")

def two_player():
	print("Welcome to Two Player Mode")
	print("First player enters word(s) for second player to guess.")
	print("Enter guess below, and then hand the keyboard over to your opponent")
	guess = input("Enter Guess for Opponent: ")
	guess_count = guess_intake(guess)
	print(guess_count)
	player_guess(guess)

def guess_intake(guess):
	display = "Guess the word: "
	for letter in guess:
		if letter.isalnum():
			display += "_"
		elif letter == " ":
			display += " "
	return display

def player_guess(guess):
	wrong = 0
	updated_guess = "Guess the word: "
	while wrong < 6:
		letter = input("Enter a letter for your guess: ")
		if letter not in guess:
			wrong += 1
			hangman_img(wrong, updated_guess)
		else:
			for i in guess:
				if i != letter:
					updated_guess += "_"
				else:
					updated_guess += i
		hangman_img(wrong, updated_guess)

def hangman_img(wrong, updated_guess):
	#need to count the amount of wrong guesses and print the hangman image
	if wrong == 0:
		print("""
			|-------|
				|
				|
				|
				|
				|
				|
			________|________""")
		display = guess_intake(updated_guess)
		print(display)
	elif 
main()
