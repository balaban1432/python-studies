# while True:
#     number_1 = int(input("the first number please: "))
#     number_2 = int(input("the second number please: "))
#     division = number_1 / number_2
#     print("the result of the division is : ", division)
#     break
# her şey yolunda görünüyor. ama bölen kısmına 0 yazarsak hata verdiğini göreceğiz
# bu exception (istisna hata) dan kurtulmanın yolu ne?
# try-except

# while True:
#     number_1 = int(input("the first number please: "))
#     number_2 = int(input("the second number please: "))
#     try:
#         division = number_1 / number_2
#         print("the result of the division is : ", division)
#         break
#     except:
#         print("something went wrong...Try again.")  # bölen 0 ile deneyelim
# hatayı biliyorsak spesifik olarak belirtebiliriz.

# while True:
#     number_1 = int(input("the first number please: "))
#     number_2 = int(input("the second number please: "))
#     try:
#         division = number_1 / number_2
#         print("the result of the division is : ", division)
#         break
#     except ZeroDivisionError:
#         print("you can't divide by zero! try again.")      


# Full 'Exception Handling Block'

# while True:
#     number_1 = int(input("the first number please: "))
#     number_2 = int(input("the second number please: "))
#     try:
#         division = number_1 / number_2  
#     except ZeroDivisionError:  # executes when division by zero
#         print("you can't divide by zero! try again.")
#     else:
#         print("the result of the division is : ", division)  # executes if there is no exception
#     finally:
#         print("thanks for using our mini division calculator! come again!")
#         break  # exits the while loop   


# while True:
#     number_1 = int(input("the first number please: "))
#     number_2 = int(input("the second number please: "))
#     try:
#         division = number_1 / number_2
#         print("the result of the division is :", division)
#         break
#     except Exception as e:
#         print("something went wrong... try again.")
#         print(f"probably it is because of '{e}' error.")
#         break  


# try:
#     x = 4/1
# except:
#     print("something went wrong")
# else:
#     print("nothing went wrong")    


# try:
#     x = 3/0
# except:
#     print("something went wrong")
# finally:
#     print("always execute this")   


# belirli istisnaları yakalamak ve işlemek için istediğimiz kadar istisna bloğu tanımlayabiliriz:
# try:
#     x = 2/0
# except ZeroDivisionError as e:
#     print("attempt to divide by zero")
# except:
#     print("something else went wrong")        


#  virgülle ayrılmış ve parantez içine alınmış birden fazla exception içerebilir.
# try:
#     x = 2/k
# except (ValueError, TypeError, NameError):
#     print("you can only enter numbers consisting of digits, not text!")


# counter = 1

# while True:
#     try:
#         age = int(input("yaşınızı giriniz: "))
#     except ValueError:
#         print("yanlış değer girdiniz.")
#     except Exception as e:
#         print("bir hata oluştu")   
#     else:
#         print(f"{age} yaşındasınız")
#         break
#     finally:
#         print(f"Döngü {counter} defa çalıştı")
#         counter += 1
#         if counter > 5:
#             print("çok fazla deneme yapıldı")
#             break           


