print("This program creates a random password from a given full name")

name = input("Please enter your full name (without any spaces): ").lower()

list_name = list(name)

import random

result = ""
k = 1

while k < 5:
    if k < 4:
        i = random.randint(0, (len(list_name) - 1))
        result += list_name[i]
    else:
        randomnumber = str(random.randint(1000,9999))
        result += randomnumber

    k += 1

print(result)

