# count = 0  # while döngüsünde sayaç atama önemli
# while count <= 5:
#     print("Halil pazarlama")
#     count += 1
# print("Osman pazarlama")


# name = "ramazan"

# for i in name:
#     print(i, end = " ")


# times = int(input("How many times should I say 'I love you'"))

# for i in range(times):
#     print("I love you") 

# count = 0
# while count <= times:
#     count += 1
#     print("I love you")


# number = int(input("enter a number 1-10"))
# for i in range(1,11):
#     print(f"{number} * {i} = {number * i}")


# print(list(range(11,1,-1)))

# print(set(range(10)))

# print(range(5))
# print(*range(5))
# print("separate")
# print(*"separate")
# print(*range(1,50,3))


# numbers = [1, 2, 3, 4, 5, 6, 7]
# text = ["one", "two", "three", "four", "five"]

# for x,y in zip(text,numbers):  # kısa listeyi baz alır
#     print(x, ":", y)


# evens = []
# ods = []

# for i in range(1,10):
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         ods.append(i)
# print(evens, ods, sep="\n")


# numbers = [11, 36, 33, 66, 89, 21, 32, 16, 10]
# count_evens = 0
# count_odds = 0

# for i in numbers:
#     if i % 2 == 0:
#         count_evens += 1
#     else:
#         count_odds += 1
# print(f"The number of even numbers : {count_evens}")
# print(f"The number of odd numbers : {count_odds }")


# for i in range(1,10):
#     print(f"{i}" * i)


# sum = 0

# for i in range(1,75):
#     sum += i
# print(sum)


# nested for loops

# who = ["I am ", "You are "]
# mood = ["happy", "confident"]

# for i in who:
#     for k in mood:
#         print(i + k) 


# names = ["susan", "tom", "edward"] 
# mood = ["happy", "sad"]

# for i in names:
#     for k in mood:
#         print(i + " is " + k)


# çarpım tablosu oluştur
# for i in range(1, 10):
#     for k in range(1, 10):
#         print(f"{i * k:4}", end ="")
#     print()


# elmas şekli

# for i in range(1, 15, 2):  
#     print(f"{'*' * i:^20}")

# for i in range(15, 0, -2):  
#     print(f"{'*' * i:^20}")

# for i in range(1, 15, 2):  # yukarıdaki ile birleşirse kum saati olur
#     print(f"{'*' * i:^20}")


# n = int(input("Enter a number to check if it is a prime number : "))

# if n > 0:
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"{n} is not a prime number")
#             break 
#     else:
#         print(f"{n} is a prime number") 
# else:
#     print("enter positive number")