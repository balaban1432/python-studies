# koşul "":"" ile bitiyor ve yeni satır girinti(4 boşluk) ile başlıyor.
# if True:
#     print("it is True")


# empty_seat = 12
# if empty_seat > 3:  # 14>3 = True, so the body will execute
#     print("there is still seat to sit")


# x = 6
# y = 9
# print("is x equal to y?                    :", x == y )
# print("is x not equal to y?                :", x != y)
# print("is x less than y?                   :", x < y)
# print("is x greater than y?                :", x > y)
# print("is x less than or equal to y?       :", x <= y)
# print("is x greater than y or equal to y?  :", x >= y)


# course = "clarusway" 

# if course == "clarusway":
#     print("you guarenteed the job")
# else:
#     print("think about it again")  # ilk koşuşu sağladığı için onu yazdı.
# ilk koşuşu sağlamasaydı ikinciyi yazacaktı. 


# number = 5
# number_str = input("enter a number")
# number = int(number_str)

# if number <= 5 :
#     print("Number is smaller than or equal to 5")
# else:
#     print("Number is bigger than 5")


# basket = ["apple", "peach", "blackberry"]
# fruit = "...."
# fruit = "apple"
# fruit = input("write a fruit")

# if fruit not in basket :
#     print("I can have a little")
# else:
#     print("I have already")  


# if-elif-else
# if for the first one,
# elif for the rest, up until the final(optional)
# else for anything not caught by the other conditionals

# weight = 80
# weight_str = input("write the weight")
# weight = int(weight_str)

# if weight > 100:
#     print("That's too heavy!")
# elif weight > 75:
#     print("I can lift that")
# else:
#     print("That's too light!") 

# ihtiyacımız kadar elif deyimi kullanabiliriz.

# audience = "baby"

# if audience == "kid":
#     print("it is free to go to cinema")
# elif audience == "teen":
#     print("discounted price!")
# elif audience == "adult":
#     print("normal price")
# else:
#     print("No such audience, stay at your home!")   
       

# number = 37

# if number >= 10:
#     print("The number is equal or greater than 10")
# else:
#     print("The number is less than 10")    


# nested if-elif-else

# audience_group = "kid", "teen", "adult"

# audience = "teen"
# audience = input("enter your status")

# if audience in audience_group:
#     if audience == "kid":
#         print("it is free to go to cinema")
#     elif audience == "teen":
#         print("discounted price!")
#     else:
#         print("normal price")
# else:
#     print("No such audience, stay at your home")   


# score = int(input("Enter your score :"))

# if score >= 90:
#     if score >= 95:
#         Score_letter="A+"
#         print(Score_letter) #*****
#     else:
#         Score_letter="A"
#         print(Score_letter) # ******
# elif score >= 80:
#     if score >= 85:
#         Score_letter="B+"
#         print(Score_letter) # ****
#     else:
#         Score_letter="B"
#         print(Score_letter)  # ****
# else:
#     Score_letter="below B"
#     print(Score_letter)  # ****

# ****** yerleri silip şu şekilde de yapabiliyoruz.

# if score >= 90:
#     if score >= 95:
#         Score_letter="A+"
#     else:
#         Score_letter="A"
# elif score >= 80:
#     if score >= 85:
#         Score_letter="B+"
#     else:
#         Score_letter="B"
# else:
#     Score_letter="below B"

# print(f"Your degree {Score_letter}")


# price = 2.00
# if price >= 1.00:
#     tax = .07
#     print(tax)
# else:
#     tax = 0
#     print(tax)  # ya da su şekilde

# if price >= 1.00:
#     tax = .07
# else:
#     tax = 0
# print(tax)
