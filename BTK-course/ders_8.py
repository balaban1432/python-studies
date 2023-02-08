# break and continue statements

# name = "ramazan balaban"

# for i in name:
#     if i == "m":
#         break
#     print(i)

# for i in name:
#     if i == "m":
#         continue
#     print(i)  


x = 0

# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x += 1    

# while x < 5:
#     if x == 2:
#         continue
#     print(x)
#     x += 1  

# while x < 5:
#     x += 1
#     if x == 2:
#         continue
#     print(x)
    

# sum of the odd numbers 1 to 100

# i = 0
# sum = 0
# while i <= 100:
#     if i % 2 == 1:
#         sum += i
#     i += 1 
# print (sum)   


# range method

# for i in range(10):
#     print(i)


# for i in range(5, 100, 10):
#     print(i)


# print(list(range(1, 100, 10)))


# enumarate

# word = "hello"

# for index, item in enumerate(word):
#     print(f"index: {index} letter: {item}")


# liste = list(enumerate(word))
# print(liste)


# zip

# liste1 = [1, 2, 3, 4, 5]
# liste2 = ["a", "b", "c", "d", "e"]
# liste3 = [100, 200, 300, 400, 500]

# print(list(zip(liste1, liste2, liste3)))


# for i in zip(liste1, liste2, liste3):
#     print(i)

# for a, b, c in zip(liste1, liste2, liste3):
#     print(b)


# list comprehensions

# numbers = []
# for x in range(10):
#     numbers.append(x)
# print(numbers)  # or

# numbers = [x for x in range(10)]
# print(numbers)


# numbers = [x ** 2 for x in range(10)]
# print(numbers)


# numbers = [x * x for x in range(10) if x % 3 == 0]
# print(numbers)


# my_string = "hello"

# my_list = [letter for letter in my_string]
# print(my_list)


# years = [1983, 1999, 2008, 1956, 1986]
# ages = [2023 - year for year in years]
# print(ages)


# result = []

# for x in range(3):
#     for y in range(3):
#         result.append((x,y))

# print(result)  # or

# numbers = [(x, y) for x in range(3) for y in range(3)]
# print(numbers)


# """
# 1 ile 100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın. hak sayısı 5 olsun.
# 100 üzerinden puan verilsin.
# """
# # import random
# # randomnumber = random.randint(1,20)
# # guess_count = 0
# # guess_limit = 5
# # count = 0
# # score = 120

# # while guess_count < guess_limit:
# #     guess = int(input("enter your guess number: "))
# #     count += 1
# #     score -= 20
# #     if guess == randomnumber:
# #         print(f"Cangratulations!!! You won at {count}. guess.")
# #         print(f"Your score is {score} out of 100")
# #         break
# #     elif guess < randomnumber:
# #         print("up")
# #     elif guess > randomnumber:
# #         print("down")    
# #     guess_count += 1
# # else:
# #     print(f"Sorry, you failled! Random number is {randomnumber}")


# """
# girilen bir sayının asal sayı olup ulmadığını kontrol edin.
# """

# number = int(input("enter a number: "))
# isprime = True

# if number == 1:
#     isprime = False

# for i in range(2,number):
#         if number % i == 0:
#             isprime = False
#             break

# if isprime:
#     print("The number is prime.")
# else:
#     print("The number is not prime.")
