import os

# Initialize game state
secret_word = 'perfume'
correct_letters = ''
number_of_attempts = 0

# Game loop
while True:
    # Get user input
    entered_letter = input('Enter a letter: ')
    number_of_attempts += 1

    # Validate user input
    if len(entered_letter) > 1:
        print('Enter only one letter.')
        continue

    # Check if letter is in secret word
    if entered_letter in secret_word:
        correct_letters += entered_letter

    # Form the word with correct letters
    formed_word = ''
    for secret_letter in secret_word:
        if secret_letter in correct_letters:
            formed_word += secret_letter
        else:
            formed_word += '*'

    # Print formed word
    print('Formed word:', formed_word)

    # Check if user won
    if formed_word == secret_word:
        # Winning message and reset game state
        os.system('clear')
        print('YOU WON!! CONGRATULATIONS!')
        print('The word was', secret_word)
        print('Attempts:', number_of_attempts)
        correct_letters = ''
        number_of_attempts = 0