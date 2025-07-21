#stackoverflow, 2010. Generate password in Python [online]. Available from:https://stackoverflow.com/questions/3854692/generate-password-in-python [Accessed 10 July 2025].
#SANKETH, M, 2023. How to make a password generator in Python [online]. Available from: https://medium.com/@mahimasanketh/how-to-make-a-password-generator-in-python-0a9a4024cd60 [Accessed 10 July 2025].
# This project was inspired by these ideas
import string
import random

s1 = list(string.ascii_lowercase) #These generate uppercase and lowercase letters, digits and special characters making the passwords hard to crack
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

length = input("What is the Length of your Password? "); #W3 Schools, 2025. Python input() Function [online]. Available from: https://www.w3schools.com/python/ref_func_input.asp [Accessed 10 July 2025].

while True: #LearnPython, 2025. Loops [online]. Available from: https://www.learnpython.org/en/Loops [Accesseed 10 July 2025].
   try:
       character_number = int(length)
       if character_number < 8:
        print("Passwords are required to have 8 characters or more. ")
        length = input("Please enter a number that is 8 or more. ")
       else:
           break
   except:
       print("Please only Enter Numbers")
       length = input("What is the Length of your Password?")


random.shuffle(s1) #W3 Schools, 2025. Python Random shuffle() Method [online]. Available from: https://www.w3schools.com/python/ref_random_shuffle.asp [Accessed 10 July 2025].
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character_number * (40/100))
part2 = round(character_number * (20/100))

result = []
for x in range(part1): #LearnPython, 2025. Loops [online]. Available from: https://www.learnpython.org/en/Loops [Accesseed 10 July 2025].
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

random.shuffle(result)
password = "".join(result)
print(password)

