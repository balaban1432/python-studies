# text = 'WWW.clarusway.com'
# print(text.endswith('.com'))
# print(text.startswith('http:'))


# text = 'www.clarusway.com'
# print(text.endswith('om'))
# print(text.startswith('w'))


# email = "clarusway@clarusway.com is my e-mail address"
# print(email.startswith("@", 9))
# print(email.endswith("-", 10, 32))  # ??????


# phrase = "myemailaddress@clarusway.com"

# print(len(phrase))
# print(phrase.startswith("@", 14))
# print(phrase.endswith(".", 15, 24))


# sentence = "I live and work in Virginia"

# print(sentence.upper())
# print(sentence.lower())
# print(sentence.swapcase())
# print(sentence)  # verimizin değişmeden gene aynı kaldığını gör


# sentence = "I live and work in Virginia"
# title_sentence = sentence.title()
# print(title_sentence)

# changed_sentence = sentence.replace("i", "+")
# changed_sentence = sentence.replace("i", "+", 4)
# print(changed_sentence)

# print(sentence)


# sentence = "and angry man andy handy"
# print(sentence.replace("a", "x", 3))  # ilk üç "a" yı "x" e çevirdi


# sentence = "I live and work in Virginia"
# swap_case = sentence.swapcase()
# print(swap_case)
# print(swap_case.capitalize())


# print("Actions speak louder than words.".upper().swapcase().capitalize())


# space_string = "      listen first        "
# print(space_string.strip())  # iki taraftaki bütün boşlukları kaldırdı


# source_string = "interoperability"
# print(source_string.strip("yi"))  # "yi" yerine "iy" yazılsa da aynı sonucu verir
# print(source_string.lstrip("in"))  #  "in" yerine "ni" yazılsa da sonuç değişmezdi
# yani belirtilen iki harften biri olsada sadece onu siler

# space_string = "       listen first       "
# print(space_string.rstrip())  # sadece sağdaki boşlukları siler


# source_string = "interoperability"
# print(source_string.rstrip("yt"))  # "yt" or "ty"


# sentence = "the dog is named Sammy"
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.capitalize())
# print(sentence.count('a'))


# first_name = input("What is your first name? ")
# last_name = input("whwt is your last name? ")
# print("Hello " + first_name.capitalize() + " "\
#     + last_name.capitalize())

# print(f"Hello  {first_name.capitalize()} "\
#     f"{last_name.capitalize()}")  # bu en kolayı buna alışacağız


# youtube dan çalışmalar

# sample = "Python is general purpose programming language"
# print(sample.find('p'))  # küçük p harfinin bulunduğu ilk yerin index değerini verir
# karakteri bulamazsa -1 değerini verir. bu index değeri değildir bulamadığını belirtir
# print(sample.find('general purpose')) # 10 verdi; anlamı 10. indexte bu string bölümü başlıyor demektir.
# print(sample.replace('general purpose', 'high level'))
# print(sample.replace('p', 'j') )  # küçük p girdiğim için büyük P ye dokunmaz
# print('Python' in sample)  # 'Python' karakterini veride bulursa True verir
# print('Jython' in sample)  # 'Jython' u bulamadığı için False verir
# print(sample.count('general'))
# print(sample.count('ge'))


# user_name = input("Enter your name: ")
# user_name = user_name[-3:] + user_name[0:3]
# print(user_name.upper())

# preclass dan devam

# country = ['USA', 'Brasil', 'UK', 'Germany', 'Turkey', 'New Zerland']
# print(country)


# string_1 = 'I quit smoking'
# print(len(string_1))


# new_list_1 = list(string_1)  # multi element list
# print(new_list_1)

# new_list_2 = [string_1]  # single element list
# print(new_list_2)


# bir listenin bileşenleri tek bir veri türüyle sınırlı değildir.
# mixed_list = [11, 'Joseph', False, 3.14, None, [1,2,3]]  # liste öğelerinden bir veya birkaç tanesi gene bir liste bile olabilir.
# print(len(mixed_list))


# warning = 'you must quit smoking!'
# print(list(warning))  # boşlukları bile öğe olarak oluşturdu
# print(len(list(warning)))


# empty_list_1 = []
# empty_list_2 = list()  #bu ikisi boş liste oluşturma yöntemidir.
# print(empty_list_1)
# print(empty_list_2)

# empty_list_1 = []
# empty_list_1.append('114')
# empty_list_1.append('plastic-free sea')
# print(empty_list_1)


# city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
# city.append('Addis Ababa')

# print(city)  # .append işlemi ile index sırasına uyarak yeni bileşeni listenin sonuna ekledi.
# istediğimiz index e eklemek istiyorsak we use .insert()


# city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
# city.insert(2, 'Stockholm')
# city[2] = 'Stockholm'  # bu şekilde 2. indexdeki İstanbul Stockholm ile yer değiştirdi.
# print(city)  # değişkenimiz eklenmiş hale geliyor. print(city) yazınca ilk hali artık yok!


# city = ['New York', 'London','Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']

# city.remove('London')  # London u çıkardı
# print(city)


# city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
# city.sort()
# print(city)  # alfabetik sıraya dizdi, veya rakamlarda sıralama
# print(len(city))


# my_list = [1, 3, 5, 7,]
# print(my_list * 3)
# print(len(my_list))

# şimdi listelerde indexing and clicing

# colors = ['red', 'purple', 'blue', 'yellow', 'greem']
# print(colors[2])  # 2. index blue verir.


# city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']

# city_list = []
# city_list.append(city)  # listemizin içine bir öğe olarak bir liste atadık
# print(city_list)
# print(city_list[0])  # access to first and only element. bu öğe liste tipi bir öğedir.
# verdiği  bu liste tipi öğenin elemanlarına da erişebiliriz.
# print(city_list[0][2])  # istanbul verdi. 1. indexte olan liste şeklindeki öğenin 2. indexini verdi
# verdiği bu string tip öğenin öğelerine de ulaşılabilir.
# print(city_list[0][2][3])  # a verdi. 


# fruits = ["apple", "banana", "watermelon", "orange", "mango", "avocado"]

# fruit_list = []
# fruit_list.insert(0, fruits)
# print(fruit_list)
# print(fruit_list[0][2][7])


# clising

# numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
# print(numbers[2:5])  # tıpkı string clising gibi


# count = list(range(11))
# print(count)
# print(count[0:11:2])


# animals = ["elephant", "bear", "fox", "wolf", "rabbit","deer", "giraffe"]

# print(animals[:])
# print(animals[3:])
# print(animals[0:4])
# print(animals[0::2])


#  youtube dan devam

# animals = ["elephant", "bear", "fox", "wolf", "rabbit","deer", "giraffe"]
# animals[2] = "horse"
# print(animals)
# print(animals[::2])
# animals.append("25")
# print(animals)
# animals.insert(3, "fox")
# print(animals)
# animals.remove("rabbit")
# print(animals)
# animals.pop()  # içine sayı yazarsak o indexteki item silinir. yazmazsak son sıradaki silinir.
# animals.pop(4)
# animals.clear()
# print(animals.index("bear"))  # bear ın index değerini verir
# print("40" in animals)  # item listede var mı diye sormuş oluruz. T veya F verir
# print("wolf" in animals)
# print(animals.count("wolf"))  
# animals.sort()  # alfabetik sıraya dizdi
# print(animals)








