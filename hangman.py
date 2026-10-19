import random

words = ["python", "computer", "program", "coding"]
secret_word = random.choice(words)

guessed_letters = []
wrong_attempts = 0
max_attempts = 6

gallows = [
"""
+---+
|   |
|
|
|
=======
""",
"""
+---+
|   |
O   |
|
|
=======
""",
"""
+---+
|   |
O   |
|   |
|
=======
""",
"""
+---+
|   |
O   |
/|   |
|
=======
""",
"""
+---+
|   |
O   |
/|\  |
|
=======
""",
"""
+---+
|   |
O   |
/|\  |
/    |
=======
""",
"""
+---+
|   |
O   |
/|\  |
/ \  |
=======
"""
]

print("Welcome to Hangman!")

while wrong_attempts < max_attempts:
print(gallows[wrong_attempts])

display_word = ""  

for letter in secret_word:  
    if letter in guessed_letters:  
        display_word += letter  
    else:  
        display_word += "_"  

print("Word:", " ".join(display_word))  
print("Guessed letters:", guessed_letters)  
print("Wrong attempts:", wrong_attempts, "/", max_attempts)  

if "_" not in display_word:  
    print("Congratulations! You won!")  
    break  

guess = input("Guess one letter: ").lower().strip()  

if len(guess) != 1 or not guess.isalpha():  
    print("Please enter one letter.")  
    continue  

if guess in guessed_letters:  
    print("You already guessed that letter!")  
    continue  

guessed_letters.append(guess)  

if guess in secret_word:  
    print("Correct guess!")  
else:  
    wrong_attempts += 1  
    print("Wrong guess!")

if wrong_attempts == max_attempts:
print(gallows[6])
print("Game over! The word was:", secret_word)
hangman.py