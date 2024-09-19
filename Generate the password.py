import random

#define character sets
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_={}[]::;;<>,.?/"
all_characters = letters + digits + symbols

# Prompt the user to specify the desired length of the password
length = int(input("Enter the desired length of the password:"))

#Generate the password
password = ""
for n in range(length):
    #Generate a random index to select a character from all_characters
    index = int(random.uniform(0, len(all_characters)))
    password += all_characters[index]
    
#Display the generated password 
print("Generated password:", password)