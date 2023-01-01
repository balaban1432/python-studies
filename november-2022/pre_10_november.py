# i = 0
# while i < 6:
#     print(i)
#     i += 1


# i = 0
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1


# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


# pre-class
# number = 0

# while number < 6:
#     print(number)
#     number += 1  # bunu belirtmezsek sonsuza kadar çalışır
# print("now, number is bigger or equal to 6")    


# my_list = ["a", "b", "c", "d", "e"]
# a = 0

# while a < len(my_list):
#     print(f"square of {a} is : {a ** 2}")
#     a += 1


# answer = 44

# question = "what number am I thinking of?"
# print("Let's play the guessing game!")

# while True:
#     guess = int(input(question))

#     if guess < answer:
#         print("Little higher")
#     elif guess > answer:
#         print("Little lower")
#     else:  # guess == answer
#         print("Are you MINDREADER!!!")
#         break  # döngüden çıkmak için kullanılan anahtar sözcük


# youtube

# index = 1
# while index <= 5:
#     print("*" * index)
#     index += 1
# print("Done")    


# index = 1
# while index <= 9:
#     print(f'{"*" * index:+^9}')  # soru işaretini çıkarıp da deneyebilirsin
#     index += 2
# print("Done") 


# while True:
#     name = input("Enter your name")
#     if name.lower() == "quit":
#         print("Exit by user")
#         break
#     elif len(name) < 3:
#         print("Name must be at least 3 characters")
#     elif len(name) > 15:
#         print("Name must be a maximum of 15 characters") 
#     else:
#         print(f"Hi {name}")
#         break  
#     *******************************     


# flowers = ['Rose', 'Orchid', 'Tulip']
# count1 = len(flowers)
# count2 = 0

# while count1 > 0 :
#     print(flowers[count2])
#     count1 -= 1
#     count2 += 1


    # for loops

# for i in [1, 2, 3, 4, 5]:
#     print(i)


# seasons = ["spring", "summer", "autumn", "winter"]
# for season in seasons:
#     print(season)


# for i in {"n1" : "one", "n2" : "two"}:
#     print(i)  # sadece key leri yazdırdı neden?


# iterable = [1, 2, 3, 4]
# for i in iterable:
#     print(i**2)


# course = "clarusway"
# for i in course:
#     print(i)


# fruits = ('Apple' , 'Banana' , 'Orange' )
# for i in  fruits: 
#     print(i)


# times = int(input("How many times should I say 'I love you'"))

# for i in range(times):
#     print("I love you")  # mesela 5 yazarsak 01234 yani 5 index olacağı için 5 defa yazdıracak


# n = int(input("enter a number between 1 - 10"))

# for i in range(11):
#     print(f"{n * i}")


# range ile ilgili bazı örnekler

# b = list(range(11))
# print(b)

# a = set(range(0,10))
# print(a)

# c = tuple(range(11))
# print(c)


# print(range(5))  # sadece aralığını verdi
# print(*range(5))  # elemanlarına ayırarak verdi. araya boşluk karakter koymuyor, sadece öyle gösteriyor

# print(*range(5,25,2))
# print(*("separate"))
# print(*range(10,0,-2))


# text = ["one", "two", "three", "four", "five"]
# numbwers = [1, 2, 3, 4, 5]
# for x, y in zip(text, numbwers):  # iki listeyi birbiri ile birleştiriyor.
#     print(x, ":", y)


# nested for loop

# who = ["I am", "You are"]
# mood = ["happy", "confident"]

# for i in who:
#     for ii in mood:
#        print(i + ii)

# for i in who:
#     for ii in mood:
#         print(i + ii, end=", ")
#     print()    


# YOUTUBE den

# for i in range(1, 9, 2):  # range içindeki , 2; ikişer atla demek yani 1,3,5,7,.. 
#     print(f"{'*' * i:!^10}")


# for i in "python":  # string veriler de iterable dir
#     print(i)


# numbers = [13, 12, 31, 14, 51, 9, 12, 15, 65, 64, 92, 6, 16, 19]
# even_num_total = 0
# odd_num_total = 0
# for i in numbers:
#     if i % 2 == 0:
#         print(f"Number {i} is an even number")
#         even_num_total += i
#     else:
#         print(f"Number {i} is an odd number")
#         odd_num_total += i
# print(f"Total even numbers is: {even_num_total}")
# print(f"Total odd numbers is: {odd_num_total}")


# 1-5 arası çarpım tablosu oluştur
# for i in range(1, 6):
#     for ii in range(1, 6):
#         print(f"{i * ii:4}", end ="")
#     print()   
 
# for i in range(1, 6):
#     for ii in range(1, 6):
#         if ii == 3:
#             continue  # ii = 3 olduğunda döngüyü başa döndürüyor.    
#         print(f"{i * ii:4}", end ="")
#     print()  

# for i in range(1, 6):
#     if i == 3:
#         continue
#     for ii in range(1, 6):
#         if ii == 3:
#             continue    
#         print(f"{i * ii:4}", end ="")
#     print()


# "x" lerle F harfi yazdır

# for i in [6, 2, 6, 2, 2]:
#     print("X" * i)


# check yourself 

# a = 3
# while a**2 < 299:
#     print('I will stop smoking')
#     a += 3


# total = 149
# country = "FR"

# if country == "FR":
#     if total <= 50:
#         print("Shipping Cost is  €30")
#     elif total <= 100:
#         print("Shipping Cost is €15")
#     elif total <= 150:
#         print("Shipping Costs €10")
#     else:
#         print("Free Shipping")
# elif country == "DE": 
#     if total <= 50:
#         print("Shipping Cost is  €25")
#     else:
#         print("Free Shipping")


# ps4_price = 300
# saved_amount = int(input('Please enter your saved amount: '))

# if saved_amount <= (ps4_price / 2):
#     print("You must save more, keep saving!")
# elif ps4_price > saved_amount > (ps4_price / 2):
#     print("You saved more than half, keep saving!")
# elif saved_amount > ps4_price:
#     print("Yippee! You can buy your PS4")   


# math_mark = int(input('Please enter the mark: '))

# if 100 >= math_mark >= 85:
#     mark = "A (Excellent)"
# elif 84 >= math_mark >= 70:
#     mark = "B (Good)"
# elif 69 >= math_mark >= 60:
#     mark = "C (Medium)"
# elif 59 >= math_mark >= 45:
#     mark ="D (Not Bad)"
# elif 44 >= math_mark >= 0:
#     mark = "F (Failed)"
# print(f"{mark}")   


# number = int(input('Please enter a number: '))
# i = 0
# while i < number:
#     print(i ** 2)
#     i += 1


# sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

# for i in sample_list:
#     print(f"The type of {i} is {type(i)}")

# pre den devam:

# sum_of_numbers = 0

# for i in range(1,75):
#     sum_of_numbers += i
# print(sum_of_numbers)


# n = int(input("Enter a number to check if it is a prime number : "))
# count = 0

# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
#     else:
#         count += 0
# if count < 3:
#     print(f"{n} is a prime number")
# else:
#     print(f"{n} is not a prime number")         


# 1-100 arasındaki asal sayıları listele

# prime = []

# for number in range(2,101):
#     status = True
#     for i in range(2,number):
#         if number % i == 0:
#             status = False
#     if status:
#         prime.append(number)

# print(prime)