# Kenneth John Costa
# Assignment #2
# The Vigenere Cipher

print("VIGENERE CIPHER".center(45, "="))

# Ask the user to input their name
name = input("\033[93mPlease enter your name: ")

# Ask the user to input the message and keyword
while True:
    message_input = input("\033[95mPlease enter the message: ")
    key_input = input("\033[92mPlease enter the keyword: ")

# Convert the message and keyword to uppercase
    upper_message = message_input.upper()
    upper_key = key_input.upper()

# Convert the message and keyword with no spaces
    nospace_message = upper_message.replace(" ", "")
    nospace_key = upper_key.replace(" ", "")

# Convert the keyword with in order to become same character with message

# Converting the message and key into ciphertext

#Convert the letters of message into numbers 

# Convert the letters of keyword into numbers

# Take the result mod 26 

# Match the converted numbers into its equivalent letter

# Save the ciphertext

# Print the result

# Ask the user if he/she wants to continue