# print(4.6 + 5)  # sum of an int and float gives float

# no1, no2 = 46, 52
# no3 = no1 - no2
# print(no3)


# no1 = 46
# print(no1/23)  # division gives float


# print((3 * 4) / 2)
# print(7 // 2)  # bölme işleminde tam kısmı verir

# print(2 ** 3)  # üs alır
# print(16 ** 0.5)  # karakök verir

# print(8 ** (1 / 3))  # 3. dereceden kök alır

# print('Result of this (12+7) sum :', 12 + 7)

# print('C:\\november\number_expenditure.txt')
# print('C:\\november\\number_expenditure.txt')
# print('C:\november\number_expenditure.txt')


# print("one", "two", "three")
# print("one", "two", "three", sep="\t")
# print("one", "two", "three", sep="\n")
# print("one", "two", "three", sep="\b")  # separates expressions by space, bir geriyi siliyor, harf varsa harfi boşluk varsa boşluğu


# print('we', 'are', 'united') 
# print('we', '\bare', '\bunited') 


# print("it's funny to learn python")
# print('it\'s funny to learn python')


# logic = True and False or not False or False
# print(logic)


# fruit = "orange"

# print("word                  ", fruit)
# print("First letter          ", fruit[0])
# print("Second letter         ", fruit[1])
# print("3rd to 5th letters    ", fruit[2:5])  # ilk index dahil, ikincisi değil.
# print("Letter all after 3rd  ", fruit[2:])


# vegetable = "Tomato"
# print("length of the word", vegetable, "is:", len(vegetable))


# print("clarus" + "way")


# print(3 * "no way!")


# fruit = "orange"
# vegetable = "Tomato"

# print("using + :", fruit, vegetable)
# print("using * :", 3 * fruit)


# fruit1 = 'Apple'
# fruit2 = 'Orange'

# print(2 * fruit1 + ' ' + 3 * fruit2)


# fruit = 'Orange'
# vegetable = 'Tomato'
# amount = 4

# print("The amount of {} we bought is {} pounds.".format(fruit, amount))


# print('{state} is the most {adjective} state of the {country}.'.format(state = "California", country = "USA", adjective = "crowded"))


# hem konumsal hem de anahtar kelimeye göre argüman kullanabiliriz
# print('{0} is the most {adjective} state of the {country}'.format('California', country = 'USA', adjective = 'crowded'))  # {0}  içindeki 0 index numarasıdır. alttaki örnek daha iyi açıklar.


# print("{9} {7} {1} {10} {3} {2} {5} {8} {6} {0} {4}.".format("in", "know", "bring", "to", "students", "out", "best", "teachers", "the", "Good", "how"))


# EN PRATİK OLAN  f string METODU

# fruit = 'Orange'
# vegetable = 'Tomato'
# amount = 6

# output = f"the amount of {fruit} and {vegetable} we bought are totally {amount} pounds."
# print(output)


# result = f"{4 * 5}"
# print(result)


# my_name = 'JOSEPH'
# output = f"My name is {my_name.capitalize()}"
# print(output)


# name = "Joseph"
# job = "teachers"
# domain = "Data Science"

# message = (
#     f"Hi {name}. "
#     f"You are one of the {job} "
#     f"in the {domain} section."
# )

# print(message)


# parantez içine alma yerine \ ile alt satıra geçilebilir.
# message = f"Hi {name}. "\
#     f"You are one of the {job} "\
#     f"in the {domain} section."
 
# print(message)


     # youtube dan aldığım dersden:

# number_1 = 3
# number_2 = 6
# print(f"{number_1} plus {number_2} is "\
#       f"{number_1 + number_2} and is not "\
#         f"{2 * (number_1 + number_2)}.")


# piNumber = 3.14159265359

# print(f"Pi number is {piNumber:.6} and "\
#       f"its half is {piNumber/2:.6}")  # :.6 ile bu sayının basılmasına 6 rakam ile izin ver diyor. noktayı saymıyor.


# message = "This is an example"

# print(f"{message:<30}")  # sola daya 30 karaktere tamamla
# print(f"{message:>30}")  # sağa daya 30 katraktere tamamla
# print(f"{message:^30}")  # ortala 30 katraktere tamamla

# print(f"{message:*<30}")  # sola daya 30 karaktere * koyarak tamamla
# print(f"{message:*>30}")  # sağa daya 30 karaktere * koyarak tamamla
# print(f"{message:*^30}")  # ortala 30 karaktere * koyarak tamamla
# print(f"{message:?^30}")  # ortala 30 karaktere ? koyarak tamamla


# name = input("enter your name: ")
# line_1 = f"welcome {name.capitalize():.10}"
# line_2 = f"{name:.10}, it is our pleasure"
# line_3 = f"to see you join us"

# print(f"{line_1:^30}")
# print(f"{line_2:^30}")
# print(f"{line_3:^30}")  # RAMAZAN BALABAN GİR VE SONUCU GÖR


# print(2 ** 3)
# print(4 * 5 / 2)
# print(4 * 5 // 2)
# print(4 * 5 % 2)


# print("We are", "\boasting", "our", "\brothers")

# print('it\'s essential to learn Python\'s libraries in IT world')

# print('C:\\north pole\noise_penguins.txt')  # '\' kendinden sonra gelen \n 'in özelliğini elinden alır

# print("we are goode\bperson")  # '\b' kendinden önceki karakteri siler, boşluk da olabilir bir harfte

# print('C:\\november\number_expenditure.txt')  # '\n' in önüne bir tane daha \ koyarak  \n in özelliği iptal olur


# print("one", "two", "three", sep="\t")  # separated by tab marks
# # sep = ' ' bu gördüğün stringleri boşlukla ayır demektir
# print("one", "two", "three", sep=" ")

# print("one", "two", "three", sep="\n") 

# print("one", "two", "three", sep=":")


# print(False and not True)

# print(True and False or not False or False)

# print('True' and 'False')

# print(2 and "Hello world")  # son True yi verir

# print("" and "hello world")  # "" boş luk F değeri veriyordu

# print(None and ())  # F ve F ilk F yi döndürür, cevap None verir

# print(None or ())  # F veya F ikinci F yi döndürür, cevap () verir


