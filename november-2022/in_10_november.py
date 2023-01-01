# a = 0
# while a < len("True"):
#     print(1)  # True olduğu sürece sonsuza kadar çalışır
#     a += 1


# number = 0

# while number < 6:
#     print(number)
#     number += 1  # bunu belirtmezsek sonsuza kadar çalışır
# print("now, number is bigger or equal to 6") 


# my_list = ["a", "b", "c", "d", ("e", "f"), "g"]
# a = 0

# while a < len(my_list):
#     print(f"square of {a} is : {a ** 2}")
#     a += 1


# a = "678" 
# b = "fg456"
# print(a.isdigit())
# print(b.isdigit())


# age = input("Enter your age please:")

# while age.isdigit():
#     print(f"you entered valied input {age}")
#     age = input("Enter your age please:")  # bunu buraya koyarsak numaric girdiğimiz sürece sürekli çalışacak
# print("you entered invalied input")

# age = input("Enter your age please:")

# while age.isdigit():
#     print(f"you entered valied input {age}")
#     break  # şimdi bir defa doğru girince duracak.
# else:
#     print("you entered invalied input")


# cevap = 9

# soru = "what what number am I thinking of?"
# print("Let's play the guessing game!")

# while True:
#     tahmin = int(input(soru))
#     if tahmin < cevap:
#         print("Litle higher...")
#     elif tahmin > cevap:
#         print("Litle lower...")
#     else:
#         print("Are you mindreader")
#         break    


# words = "sentence".split("e")
# print(words)  # çıktııyı liste olarak verir

# a = "I am Ranazan"
# print(a.split())

# en uzun kelimenin kaç harfi var
# sentence = input("Give me a sentence:")
# words = sentence.split()
# counter = 0
# longest = 0

# while counter < len(words):
#     if len(words[counter]) > longest:
#         longest = len(words[counter])
#     counter += 1
# print(f"the length of the longest word: {longest}")   


# for loop

# liste = [1, 2, 3, 4, 5]
# for i in liste:
#     print(i)


# seasons = ["spring", "summer", "autumn", "winter"]
# for season in seasons:
#     print(season)


# course = "clarusway"  # strings are also iterable
# for i in course:
#     print(i)


# course = "clarusway",  # virgülü koyunca tuple a dönüştü ve tek index gördü
# for i in course:
#     print(i)


# names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]

# for i in names:
#     print(f"Hello {i}")


# boş bir listem var son hali [1, 2, 3, 4, 5] olsun
# liste = []

# for i in range(1,6):
#     liste.append(i)
# print(liste)    

# C-l-a-r-u-s-w-a-y  yazdırın?
# name = "Clarusway"
# count = 0
# for i in name:
#     count += 1
#     if count < len(name):
#         i = i + "-"
#     print(i, end="")  # while ile olur mu bak?    

# hocam dünkü son soruyu while ile bu şekilde yapabildim:
# name = "clarusway"
# count = 0

# while True:
#     if count < len(name) - 1:
#         print(name[count], end="-")
#     elif count == 8:
#         print(name[count])
#     count += 1


# user = {
#     "name": "Daniel",
#     "surname": "Smith",
#     "age": "35"
# }

# for i in user:
#     print(i)  # sadece key değerlerini verdi

# for i in user.values():
#     print(i)  # value leri verdi

# for i in user.items():
#     print(i)









