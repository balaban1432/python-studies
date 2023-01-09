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






