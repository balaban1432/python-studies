# print(4 + 5)  # sum of int gives int

# print(39 + 1.0)  # sum of an int and float gives float

# no1, no2 = 46, 52
# no3 = no1 - no2
# print(no3)

# no1 = 46
# print(no1 / 23)  # division gives float

# print((3 * 4) / 2)

# print(7 // 2)  # it gives integar part of division 
#  # bölme işleminde tam kısmı verir

# print(2 ** 3)  # üssünü alır

# print(64 ** 0.5)  # kare kök

# print(15 ** (1 / 3))  # üçüncü kökünü aldık

# print('Result of this (12+7) sum :', 12 + 7)


# print('C:\\november\number_expenditure.txt')

# print("one", "two", "three", sep="\t")  # separated by tab marks

# print('we', '\bare', '\bunited')  # remember, normally print() function
# separates expressions by space, bir geriyi siliyor, harf varsa harfi boşluk varsa boşluğu

# print('it\'s funny to learn python')  # '\' allows single-quote


# logic = True and False or not False or False
# print(logic)


# print(2 and 3)  # 3 verdi

# print(1 and 0)  # 0 verdi

# print(1 and "I am doing good!")  # "I am doing good!" verdi

# print([] and "Hello world!")

# print(2 or 3)  # 2 verdi

# print(None or 1)  # 1 verdi

# print(0 or {})  # {} verdi, F or F ikinciyi verir
# ilki T olsaydı ikinciyi okumadan ilkini verirdi 2 or 3, 2 verdiği gibi


# print([] or "Hello world!")  # Hello world! verdi


# fruit = "orange"

# print('word                    ', fruit)
# print('First letter            ', fruit[0])
# print('Second letter           ', fruit[1])
# print("3rd to 5th letters      ", fruit[2:5])  # ilk rakam dahil ikincisi değil
# print("Letter all after 3rd    ", fruit[2:]) 


# city = 'Phoenix'

# print(city[1:])  # from index 1 to the end
# print(city[:6])  # from zero to 5th index
# print(city[::2])  # from zero to end by 2 step
# print(city[1::2])  # from index 1 to the end by 2 step
# print(city[-3:])  # from index -3 to the end
# print(city[::-1])  # negative step starts from the end to zero


# vegetable = 'Tomato'
# print('length of the word', vegetable, 'is :', len(vegetable))


# print('Clarus' + 'way')  # iki str veriyi boşluk bırakmadan birleştirir.

# print(3*'no way!')  # boşluk bırakmadan veriyi tekrar eder


# fruit = 'Orange'
# vegetable = 'Tomato'

# print("using + :", fruit + vegetable)
# print("using * :", 3 * fruit)


# fruit = 'orange'
# fruit += '  apple'

# print(fruit)


# fruit = 'orange'
# fruit += ' apple'
# fruit += ' banana'
# fruit += ' apricot'

# print(fruit)


# fruit1 = 'Apple'
# fruit2 = 'Orange'

# print(2*fruit1 + ' ' + 3*fruit2)


# fruit = 'Orange'
# vegetable = 'Tomato'
# amount = 4

# print('The amount of {} we bought is {} pounds'.format(fruit, amount))  # {} bu parantez kullanılır


# print('{state} is the most {adjective} state of the {country}'.format(state = 'California', country = 'USA', adjective = 'crowded'))
# yukarıda dikkat edilirse anahtar kelimeleri sırayla yazmamıza gerek kalmadı


# hem konumsal hem de anahtar kelimeye göre argüman kullanabiliriz
# print('{0} is the most {adjective} state of the {country}'.format('California', country = 'USA', adjective = 'crowded'))


# nesneleri parantez içindeki konumlarına bakarak da seçebilirsiniz.
# print("{6} {0} {5} {3} {4} {1} {2}".format('have', 6, 'months', 'a job', 'in', 'found', 'I will'))


# print("{9} {7} {1} {10} {3} {2} {5} {8} {6} {0} {4}".format('in', 'know', 'bring', 'to', 'students.', 'out', 'best', 'teachers', 'the', 'Good', 'how'))

# print("{3} {2} {4} {1} {0}".format("job.", "a", "will", "I", "find"))

# fruit = 'Orange'
# vegetable = 'Tomato'
# amount = 6

# output = f"The amount of {fruit} and {vegetable} we bought are totally {amount} pounds"
# print(output)


# result = f"{4*5}"
# print(result)


# my_name = 'JOSEPH'
# output = f"My name is {my_name.capitalize()}"
# print(output)


# # Ayrıca çok satırlı bir f-string biçimlendirme stili de vardır.
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
#     f"{number_1 + number_2} and is not "\
#     f"{2 * (number_1 + number_2)} .") 


# piNumber = 3.14159265359
# print(f"Pi number is {piNumber:.6} and "\
#     f"its half is {piNumber/2:.6}")  # :.6 ile bu sayının basılmasına 6 rakam ile izin ver diyor. noktayı saymıyor.


# message = "This is an example"

# print(f"{message:<30}")  # sola daya 30 a tamamla
# print(f"{message:>30}")  # sağa daya 30 a tamamla
# print(f"{message:^30}")  # ortala 30 a tamamla

# print(f"{message:*<30}")  # sola daya 30 karaktere * koyarak tamamla
# print(f"{message:*>30}")  # sağa daya 30 karaktere * koyarak tamamla
# print(f"{message:*^30}")  # ortala 30 karaktere * koyarak tamamla
# print(f"{message:?^30}")  # ortala 30 karaktere ? koyarak tamamla


# name = input("Enter your name: ")
# line_1 = f"Welcome {name.capitalize():.10}"  # İLAVETEN .capitalize() ekledim görmek için
# line_2 = f"{name:.10}, it is our pleasure"
# line_3 = f"to see you join us"

# print(f"{line_1:^30}")
# print(f"{line_2:^30}")
# print(f"{line_3:^30}")  # RAMAZAN BALABAN GİR VE SONUCU GÖR