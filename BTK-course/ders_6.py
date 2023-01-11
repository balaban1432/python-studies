# conditions

# username = "ramazan"
# password = "1234"

# if (username == "ramazan") and (password == "1234"):
#     print("welcome")
# else:
#     print("username or password is wrong") 

# if username == "ramazan":
#     if password == "1234":
#         print("welcome")
#     else:
#         print("invailed password")
# else:
#     print("invailed username")            


# x = int(input("enter first number :  "))
# y = int(input("enter second number :  "))

# if x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")    
# else:
#     print("x is smaller than y")


# 1.
# name = input("enter your name : ").lower()
# age = int(input("enter your age : "))
# status = input("enter your education status, include lise,üniversite  :").lower()
# liste = ["lise", "üniversite"]

# if age >= 18:
#     if status in liste:
#         print("you can have a driving licence")
#     else:
#         print("you can not have a driving lisance")
# else:
#     print("you can not have a driving lisance")


# # 2.
# first_exam = int(input("enter first exam result: "))
# second_exam = int(input("enter second exam result: "))
# third_exam = int(input("enter third exam result: "))
# average = (first_exam + second_exam + third_exam) / 3

# if 24 >= average >= 0:
#     mark = 0
# elif 44 >= average >= 25:
#     mark = 1
# elif 54 >= average >= 45:
#     mark = 2
# elif 68 >= average >= 55:
#     mark = 3
# elif 84 >= average >= 70:
#     mark = 4
# elif 100 >= average >= 85:
#     mark = 5
# else:
#     print("invalied value!!! ")    
# print(f"your mark is: {mark}")  


# 3.
# import datetime  # modüllerin kullanımına alıştırmak ve araştırmaya yöneltmek amacıyla

# tarih = input("aracınız hangi tarihte trafiğe çıktı? (219/8/9): ")
# tarih = tarih.split("/")

# trafigeCıkıs = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
# simdi = datetime.datetime.now()
# fark = simdi - trafigeCıkıs
# days = fark.days

# if days <= 365:
#     print("1. servis aralığı")
# elif days > 365 and days <= 365*2:
#     print("2. servis aralığı")
# elif days > 365*2 and days <= 365*3:
#     print("3. servis aralığı")
# else:
#     print("hatalı süre!") 


# 4. 
# number = int(input("enter a number: "))

# if number > 0 and number < 100:
#     print("your number is between 0 to 100")
# elif number >= 100:
#     print("your number is greater than 100")
# else:
#     print("your number is smaller than 0")    


# 5. check the number if it is positive even number. 
# number = int(input("enter a number: "))

# if number > 0:
#     if number % 2 == 0:
#         print(f"{number} is a positive even number")
#     else:
#         print(f"{number} is a positive odd number")   
# else:
#     print(f"{number} is a negative number")     


# 6. compare given three numbers
# number1 = int(input("enter first number: "))
# number2 = int(input("enter second number: "))
# number3 = int(input("enter third number: "))

# if number1 > number2 and number1 > number3:
#     print(f"{number1} is the biggest number")
# elif number2 > number1 and number2 > number3:
#     print(f"{number2} is the biggest number")
# else:
#     print(f"{number3} is the biggest number")


# 7.
# vise1 = int(input("enter first vise result: "))
# vise2 = int(input("enter second vise result: "))
# final = int(input("enter final result: "))

# average = (vise1 + vise2) * 0.40 + final * 0.60

# if final >= 70:
#     print("you have passed.")
# elif average >= 50 and final >= 50:
#     print("you have passed.")
# else:
#     print("you have not passed.")


# 8.
# name = input("enter your name: ")
# weight = float(input("enter your weight: "))
# length = float(input("enter your length: "))

# kilo_index = weight / (length ** 2)

# if kilo_index >= 0 and kilo_index <= 18.4:
#     print(f"{name} is thin")
# elif kilo_index >= 18.5 and kilo_index <= 24.9:
#     print(f"{name} is normal")
# elif kilo_index >= 25.0 and kilo_index <= 29.9:
#     print(f"{name} is fat")
# else:
#     print(f"{name} is obese")

