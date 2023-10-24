# Input: Get a character from the user
character = input("Enter a character: ")

# Check if the character is a single alphabet letter
if len(character) == 1 and character.isalpha():
    # Convert the character to lowercase for case-insensitive comparison
    character = character.lower()

    if character in 'aeiou':
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")
else:
    print("Please enter a single alphabet letter.")