import random
import string
import pyperclip


def generate_password(length, letters, numbers, characters, clipboard):
    source = ""
    generated_password = ""
    if letters == "yes":
        source += string.ascii_letters
    if numbers == "yes":
        source += string.digits
    if characters == "yes":
        source+= string.punctuation
    if not source:
        print("No character types selected. Cannot generate password.")
        return
    
    generated_password = ''.join(random.choices(source, k = length))
    print(generated_password)
    if clipboard == "yes":
        pyperclip.copy(generated_password)
        print("Your password was copied to your clipboard!")


length_password = int(input("Enter the length of your password: "))
letters = input("Do you want letters in your password? ").lower()
numbers = input("Do you want numbers in your password? ").lower()
characters = input("Do you want special characters in your password? ").lower()
clipboard = input("Do you want your password to be copied to your clipboard after it's generated? ").lower()

generate_password(length_password, letters, numbers, characters, clipboard)