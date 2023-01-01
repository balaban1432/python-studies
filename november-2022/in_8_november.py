# if True:
#     print("This is True")


# if ["Ali"]:
#     print("This is true")  # bunun da bir true değeiri olduğu için True algıladı.


# if 0:
#     print("This is True")  # True vermedi


# grocery_store = True
# minced_meat = True
# hamburger_bread = True
# onion = True
# lettuce = True

# hamburger = grocery_store and minced_meat and (lettuce or onion) and hamburger_bread

# if hamburger:
#     print("Afiyet olsun")  # şart olan şeylerden birini False yaparsak çalışmaz.


# if 1 != 0:
#     print("çalişir")


# empty_seat = int(input("enter empty seat"))
# if empty_seat > 3:
#     print("oldukça yerimiz mevcut")


# x = 6
# y = 9
# print("is x equal to y?                    :", x == y )
# print("is x not equal to y?                :", x != y)
# print("is x less than y?                   :", x < y)
# print("is x greater than y?                :", x > y)
# print("is x less than or equal to y?       :", x <= y)
# print("is x greater than y or equal to y?  :", x >= y)


# a = "TWELVE PLUS ONE"
# b = "ELEVEN PLUS TWO"
# if set(a) == set(b):
#     print("we are same")
# print(set(a), set(b), sep = "\n")

# if-else
# course = "clarusway" 

# if course == "clarusway":
#     print("you guarenteed the job")
# else:
#     print("think about it again")  
# ilk koşuşu sağladığı için onu yazdı.
# ilk koşuşu sağlamasaydı ikinciyi yazacaktı. 


# number = int(input("enter a number"))

# if number <= 72:
#     print(f"{number} is smaller than or equal to 72")
# else:
#     print(f"{number} is bigger than 72")


# number = int(input("enter a number"))  # imput sonucu her zaman string döner *****

# if (number % 2) == 0:  # mod 2 ye göre 0 a eşit olan sayılar çift sayıdır. bu şekilde çift tek sayı ayrımı yapılabilir.
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")


# number = int(input("enter a number"))

# if number > 0:
#     print(f"{number} is positive number")
# else:
#     print(f"{number} is negative number")  # 0 durumunu elif ile yazacağız


# number1 = int(input("first number"))
# number2 = int(input("second number"))

# if number1 > number2:
#     print(f"The large is number {number1} ")
# else:
#     print(f"The large is number {number2} ")


# if-elif-else

# audience = "baby"

# if audience == "kid":
#     print("it is free to go to cinema")
# elif audience == "teen":
#     print("discounted price!")
# elif audience == "adult":
#     print("normal price")
# else:
#     print("No such audience, stay at your home!")


# a = int(input("first number"))
# b = int(input("second number"))
# c = int(input("third number"))

# if a > b and a > c:
#     print(f"The large is number {a} ")
# elif b > a and b > c:
#     print(f"The large is number {b} ")
# elif c > a and c > b:
#     print(f"The large is number {c} ")
# else:
#     print("get lost ")  # 3 sayı da eşitse bu çalışır.


# number = int(input("enter a number"))

# if number > 0:
#     print(f"{number} is positive number")
# elif number < 0:
#     print(f"{number} is negative number")
# else:
#     print("get lost")


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


# score = int(input('Enter your score :'))

# if score >=90:
# 	if score >=95:
# 		Score_letter='A+'
# 	else:
# 		Score_letter='A'
# elif score >=80:
# 	if score >=85:
# 		Score_letter = 'B+'
# 	else:
# 		Score_letter = 'B'
# else:
# 	Score_letter = 'below B'
# print(f'Your degree: {Score_letter}')

# kendi örneğim olsun
# point = int(input("Enter point"))

# if point >= 85:
#     mark = 5
# elif point >= 70:
#     mark = 4
# elif point >= 50:
#     mark = 3
# elif point >= 30:
#     mark = 2
# else:
#     mark = 1
# print(f"your mark is {mark}")


# in-class tasks


# task-1 girilen ayın kaç gün çektiğini versin
# a = ["jaunary", "march", "may", "july", "august", "october", "december"]
# b = ["april", "june", "september", "november"]
# c = ["february"]
# months = input("enter month name")
# if months in a:
#     number_of_days = "31"
# elif months in b:
#     number_of_days = "30"
# else:
#     number_of_days = "28/29"
# print(f"No. of days: {number_of_days}")

# task-2 girilen ay ve günün hangi mevsime denkgeldiğini versin
# a = ["december", "jaunary", "february", "march"]
# b = ["march", "april", "may", "june"]
# c = ["june", "july", "august", "september"]
# d = ["september", "october", "november", "december"]

# month = input("enter month name")
# day = int(input("enter the day"))

# if month in a:
#     if month == "jaunary":
#         season = "winter"
#     elif month == "february":
#         season = "winter"
#     elif month == "march":
#         if day <= 19:
#             season = "winter"
#         else:
#             season = "spring"
# elif month in b:
#     if month == "april":
#         season = "spring"
#     elif month == "may":
#         season = "spring"
#     elif month == "june":
#         if day <= 19:
#             season = "spring"
#         else:
#             season = "summer"
# elif month in c:
#     if month == "july":
#         season = "summer"
#     elif month == "august":
#         season = "summer"
#     elif month == "september":
#         if day <= 20:
#             season = "summer"
#         else:
#             season = "autumn"
# if month in d:
#     if month == "october":
#         season = "autumn"
#     elif month == "november":
#         season = "autumn"
#     elif month == "december":
#         if day <= 20:
#             season = "autumn"
#         else:
#             season = "winter"
# print(f"season is {season}")            

#task-3 burç hesabı
# month = input("enter month of birth")
# day = int(input("enter birthday"))

# if month == "fabruary":
#     if day >= 20:
#         ast_sign = "pisces"
#     else:
#         ast_sign = "aquarius"
# if month == "march":
#     if day <= 20:
#         ast_sign = "pisces"
#     else:
#         ast_sign = "aries"
# if month == "april":
#     if day <=20:
#         ast_sign = "aries"
#     else:
#         ast_sign = "taurus"
# if month == "may":
#     if day <= 22:
#         ast_sign = "taurus"
#     else:
#         ast_sign = "gemini"
# if month == "june":
#     if day <= 21:
#         ast_sign = "gemini"
#     else:
#         ast_sign = "cancer"
# if month == "july":
#     if day <=22:
#         ast_sign = "cancer"
#     else:
#         ast_sign = "leo"
# if month == "august":
#     if day <= 21:
#         ast_sign = "leo"
#     else:
#         ast_sign = "virgo"
# if month == "september":
#     if day <= 23:
#         ast_sign = "virgo"
#     else:
#         ast_sign = "libra"
# if month == "october":
#     if day <= 23:
#         ast_sign = "libra"
#     else:
#         ast_sign = "scorpio"
# if month == "november":
#     if day <= 22:
#         ast_sign = "scorpio"
#     else:
#         ast_sign = "sagittarius"
# if month == "december":
#     if day <= 22:
#         ast_sign = "sagittarius"
#     else:
#         ast_sign = "capricorn"
# if month == "jaunary":
#     if day <= 20:
#         ast_sign = "capricorn"
#     else:
#         ast_sign = "aquarius"

# print(f"Your Astrological sign is :{ast_sign}")
             
# task-4 medyan hesabı
# a = float(input("enter first number"))
# b = float(input("enter second number"))
# c = float(input("enter third number"))

# numbers = a, b, c
# my_list = list(numbers)
# my_list.sort()
# print(f"The median is {my_list[1]}")

# task-5 artık yıl hesabı
# y = int(input("enter a year"))
# if y % 4 == 0:
#     print(f"{y} is a leap year")
# elif y % 100 != 0:
#     print(f"{y} is a leap year")
# elif y % 400 == 0:
#     print(f"{y} is not a leap year")
# else:
#     print(f"{y} is not a leap year")           
