# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:25:16 2024

@author: sarit
"""

import random

def generate_passwords(name, dob, phone_number, mothers_name, num_passwords):
    passwords = []
    
    # Extracting initials from the name
    initials = ''.join(word[0] for word in name.split())
    
    # Extracting year from the date of birth
    year = dob.split('-')[0][-2:]
    
    # Generating passwords
    for _ in range(num_passwords):
        # Random numbers for the password
        random_numbers = ''.join(str(random.randint(0, 9)) for _ in range(3))
        
        # Combining initials, year, and random numbers to form the password
        password = initials.lower() + year + random_numbers
        
        # Appending to the list of passwords
        passwords.append(password)
    
    return passwords

# Getting user input
name = input("Enter your name: ")
dob = input("Enter your date of birth (YYYY-MM-DD): ")
phone_number = input("Enter your phone number: ")
mothers_name = input("Enter your mother's name: ")
num_passwords = int(input("Enter the number of passwords you want to generate: "))

# Generating passwords
passwords = generate_passwords(name, dob, phone_number, mothers_name, num_passwords)

# Suggesting passwords to the user
print("Here are your suggested passwords:")
for i, password in enumerate(passwords, start=1):
    print(f"Password {i}: {password}")

print("These passwords are based on your initials, birth year, and some random numbers, making them easy to remember!")