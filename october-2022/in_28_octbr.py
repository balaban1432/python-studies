# print(2 ** 3)

# print(4 * 5 / 2)  # bölme sonucunu float veriyor = 10.0
# print(4 *5 // 2)

# print("We are", "\boasting", "our", "\brothers")

# print('it\'s essential to learn Python\'s libraries in IT world')

# print('C:\\north pole\noise_penguins.txt')  # '\' kendinden sonra gelen \n 'in özelliğini elinden alır

# print("we are goode\bperson")  # '\b' kendinden önceki karakteri siler, boşluk da olabilir bir harfte

# print('C:\\november\number_expenditure.txt')  # '\n' in önüne bir tane daha \ koyarak  \n in özelliği iptal olur

# print("one", "two", "three", sep="\t")  # separated by tab marks
# sep = ' ' bu gördüğün stringleri boşlukla ayır demektir
# print("one", "two", "three", sep=" ")

# print("one", "two", "three", sep="\n") 

# print(False and not True)

# print(True and False or not False or False)

# print('True' and 'False')

# print(2 and "Hello world")  # son True yi verir

# print("" and "hello world")  # "" boş luk F değeri veriyordu

# print(None and ())  # F ve F ilk F yi döndürür, cevap None verir


# best = "Clarusway"
 
# print(best[4])  # indexing
# print(best[0:4])  # 'Clar' verir  : slicing
# print(best[::2])


# fruit = "orange"

# print('word                    ', fruit)
# print('First letter            ', fruit[0])
# print('Second letter           ', fruit[1])
# print("3rd to 5th letters      ", fruit[2:5])  # ilk rakam dahil ikincisi değil
# print("Letter all after 3rd    ", fruit[2:]) 

# print('123456789'[0::2])


# vegetable = 'Tomato'
# print('length of the word', vegetable, 'is :', len(vegetable))


# print("Clarus" + "way")
# print("aslan" * 3)
# print(3 * "aslan")

# print(* "aslan")  # * başa eklenirse harfleri aralıklı gösteriyor. ama boşluk eklemiyor, sadece gösterimde


# a = "upper"
# b = "case"
# a += b  # a = a + b
# print(a)

# c = "letter"
# a += c  # a = a + c
# print(a)


# fruit = "apple"
# vegatable = "spinach"
# amount = 5

# print("I bought {} and {}. They are {} kgs.".format(fruit, vegatable, amount))
# f.string e odaklanmamız daha faydalı olur

# print(f"I bought {fruit} and {vegatable}. They are {amount} kgs.")
# print(f"I bought {fruit} and {vegatable}. They are {10//5} kgs.")
# print(f"I bought {fruit.upper()} and {vegatable}. They are {amount} kgs.")
# buranın bir artısıda süslü parantez içinde işlem yapılabilmesidir.

#      buradan  
# print(f"I bought {fruit:10} and {vegatable:10}. They are {amount} kgs.")
# :10 kelimeleri 10 karaktere tamamladı, apple için 5+5 boşluk
# print(f"I bought {fruit:3} and {vegatable:3}. They are {amount} kgs.")
# :3 koyunca üçten fazla karakteri olanlara dokunmadı, üçten az olanları üçe tamamladı
# print(f"I bought {fruit:.3} and {vegatable:.3}. They are {amount} kgs.")
# :.3 ilk üç harfinden sonrasını kesti
# print(f"I bought {fruit:10.3} and {vegatable:10.3}. They are {amount} kgs.")
# :10.3 on karaktere tamamladı ve kelimelerin ilk üç harfini aldı
#        buraya kadar youtube dan çalışmalarım

# sample = f"{2**3}"
# print(sample)


# name = "MARIAM"
# output = f"My name is {name.capitalize()}"
# print(output)


# name = "susan"
# age = "young"
# gender = "lady"
# school = "CLRWY IT university"

# output = (
#     f"{name} is a {age} {gender} and "
#     f"she is a student at "
#     f"the {school}."
# )
# print(output)  # or

# output = f"{name} is a {age} {gender} and "\
#     f"she is a student at "\
#     f"the {school}."

# print(output)