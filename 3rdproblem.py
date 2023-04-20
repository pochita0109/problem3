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

# Convert the keyword in order to become same character with message
    key_converted = nospace_key*(len(nospace_message)//len(nospace_key)+1)
    key_converted = key_converted[:len(nospace_message)]

# Converting the message and key into ciphertext
    cipher_text = ""
    for i in range(len(nospace_message)):

# Convert the letters of message into numbers 
        numbered_message = ord(nospace_message[i])-65

# Convert the letters of keyword into numbers
        numbered_keyword = ord(nospace_key[i])-65
        
# Take the result mod 26 
        modular_result = (numbered_message + numbered_keyword) % 26

# Match the converted numbers into its equivalent letter
        ciphered_letter = chr(modular_result + 65)

# Save the ciphertext
        cipher_text += ciphered_letter

# Print the result

# Ask the user if he/she wants to continue