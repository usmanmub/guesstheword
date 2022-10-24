print("Welcome to the multiplayer guess the word")
word=input("Player 1, Enter a word. Don't show the other player(s) - ")
guess=input("Player 2, guess the word (Guess in 6 goes) - ")
if guess == word:
	print("Well Done")
else:
	print("Try Again")
	guess=input("Player 2, guess the word - ")
if guess == word:
	print("Well Done")
else:
	print("Try Again")
guess=input("Player 2, guess the word - ")
if guess == word:
	print("Well Done")
else:
	print("Try Again")
guess=input("Player 2, guess the word - ")
if guess == word:
	print("Well Done")
else:
	print("Try Again")
guess=input("Player 2, guess the word - ")
if guess == word:
	print("Well Done")
else:
	print("Try Again")
guess=input("Player 2, guess the word - ")
if guess == word:
	print("Well Done")
else:
	print("Game Over. You lose. The word is",word)
    	
