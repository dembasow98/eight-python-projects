import string as s
from random import *

#FUNCTIONS TO USE:
def generate_random_password(length):
    #Unite all ascii characters, digits and punctuations in one string:
    ascii_string = s.ascii_letters+s.digits+s.punctuation

    #join one random character lenght time
    password = "".join(choice(ascii_string) for i in range(length))

    #print out the generated password
    print("Generated Password: "+password)
    

print("**********************WELCOME TO RANDOM PASSWORD GENERATOR***************************")
low = int(input("Enter the minimum password length:\n"))
high = int(input("Enter the maximum password length:\n"))
length = randint(low,high)
generate_random_password(length)

answer = ""
while answer == "Y" or "y" or "yes" or "YES" or "Yes":
    answer = (input("Do you want to generate a new random password? "))
    if answer == "N" or "NO" or "n" or "no": 
        break
    else:
        low = int(input("Enter the minimum password length:\n"))
        high = int(input("Enter the maximum password length:\n"))
        length = randint(low,high)
        generate_random_password(length)

print("**********************GOODBYE MATE****************************************************")