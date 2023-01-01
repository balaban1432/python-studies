# while True:
#     number_1 = int(input("enter first number: "))
#     number_2 = int(input("enter second number: "))
#     try:
#         division = number_1 / number_2
#         print(f"the result is {division}")
#         break
#     except:  # buraya spesifik hata türü girilebilir.(zero division eror) ama ozaman diğer hata türlerini görmez
#         print("something went wrong... Try again!!!")


# while True:
#     try:
#         number_1 = int(input("enter first number: "))
#         number_2 = int(input("enter second number: "))
    
#         division = number_1 / number_2
#         print(f"the result is {division}")
#         break
#     except ZeroDivisionError:
#         print("you can not divide by zero")
#     except TypeError:
#         print("hata var")
#     except ValueError:
#         print("gene hata var")
#     except:
#         print("something went wrong... Try again!!!")  # except ler böyle sıralanabiliyor.


# while True:
#     try:
#         number1 = int(input("Enter a first number: "))
#         number2 = int(input("Enter a second number: "))
#         division = number1 / number2
#     except Exception as e:
#         print("Something went wrong.")
#         print(f"Probably it is because of {e}")
#     else:
#         print(f"The result is: {division}")
#     finally:
#         print("It's done!")
#         break


# try:
#     x = 2 / 0
# except ZeroDivisionError:
#     print("you cannot divide by zero!")
# except:
#     print("something went wrong")



# fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]

# x = int(input("Please enter an index number to choose a fruit from the list: "))

# while True:
#     try:
#         print(f"Your favorite fruit is {fruits[x]}.")
#     except IndexError:
#         print("Please enter a valid number between 0-5(including0).")
#     except :
#         print("Unknown error, please report to the coding man!") 
#     finally:
#         print("Thank you for trying our fruits!")
#         break

