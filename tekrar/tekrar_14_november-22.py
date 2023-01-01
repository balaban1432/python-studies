# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


# unpack a collection(list, tuple, etc)
# fruits = ["apple", "banana", "cherry"]  
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


# x = "ben"
# y = "ali"
# b = "veli"
# print(x, y, b)  # aynı satırda aralıklı yazdırdı
# print(x + y + b)  # birleştirip yazar, arada boşluk yok.


# x = 5
# y = "ali"
# print(x + y)  # string + integer hata verir
# print (x, y)


# import random
# print(random.randrange(1, 10))  # 1 den 10 a kadar her defasında rastgele bir sayı üretir.


# a = """Lorem ipsum dolor sit amet,  # 3 tırnak örneği, çıktıya dikkat et
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# txt = "The best things in life are free!"
# print("free" in txt)


# txt = "The best things in life are free!"
# print("expensive" not in txt)


# a = "clarusway"
# print(a.split("a"))  # "a" lardan böler ve sonucu liste olarak yazdırır


# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)


# a = "benim adım ramazan balaban"

# print(a.find("ramazan"))
# print(a.count("a"))
# print("benim" in a)
# print(a.count("an"))
# print(a.find("z"))
# print("z" in a)

# a = "45"
# b = "45.02"
# c = "fg45"
# print(a.isdigit())
# print(a.isdigit())
# print(c.isdigit())


# print('It\'s alright')  # "\" bunu koymazsak hata verir. çünkü '' içinde gene ' olmaz
# print("This will insert one \\ (backslash).")  # \ kendinden sonra gelen karakterin özel bir gücü varsa onu yok eder
# print("Hello\nWorld!")  # \n sonrasını yeni satıra yazdırır
# print("Hello\rWorld!")
# print("Hello\tWorld!")
# print("Hello\bWorld!")


# sample = "benim adım ramazan balaban"

# print(sample.capitalize())
# print(sample.casefold())  # casefold() = lower()
# print(sample.find("zan"))
# print(sample.find("a", 13, 20 ))
# print(sample.index("ad"))
# print(sample.index("a", 13, 20))  # find ile aynı
# print(sample.isalpha())  # False verdi çünkü boşluklar alfabetik değildir.
# print(f"{sample:*^100}")
# print(f"{sample:0^100}")
# print(f"{sample:2>100}")
# print(f"{sample:*^100.15}")


# text = "banana"
# x = text.center(20) # Print the word "banana", taking up the space of 20 characters, with "banana" in the middle
# print(x)

# text = "banana"
# x = text.center(20, "*")  # yirmi karaktere * la tamamlar
# print(x)


# a = "Hello world!"
# b = "hello 123"
# c = "mynameisPeter"

# print(a.islower())  # tüm harfler küçük harf ise True verir
# print(b.islower())  # boşluklara, rakamlara ve sembollere bakmaz.
# print(c.islower())


# txt = "Company 12"
# x = txt.isalnum()  # string de sadece rakam ve harf varsa True verir.
# print(x)  # boşluktan dolayı False verdi


# a = "HELLO, AND WELCOME TO MY WORLD"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"

# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())


# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS PETER"

# print(a.isupper())
# print(b.isupper())
# print(c.isupper())


# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)  # belirttiğimiz string ayıraçla bir iterable öğeyi bir string veriye dönüştürür.
# print(x)


# my_list = ["derya", "furkan", "ramazan", "balaban"]
# # string = "ve"
# new = " ve ".join(my_list)  # liste veya tuple lar string değerlerden oluşmalı
# print(new)


# print("Actions speak louder than words.".upper().swapcase().capitalize())

# x = "Hello"
# y = 15
# print(bool(x))
# print(bool(y))

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))


# print(list(), [])  # boş liste yazdırmanın iki yolu

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]  # 1 ve 2. indexdeki değerleri bu iki veriyle değiştirir.
# print(thislist)  # tek index yazarsak sadece o indexi değiştirir.

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]  # 1 tane çıkarıp yerine bu ikisini ekliyor
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)  # bu metodla bir tuple, set veya herhangi bir iterable nesneyi listelere ekleyebiliriz
# print(thislist)


# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist.pop(0)
# print(thislist)  # yukarıdaki ile aynı sonucu aldık


# thislist = ["apple", "banana", "cherry"]
# del thislist  # listeyi tamamen siler
# print(thislist)  # ortada liste kalmayınca birşey yazdıramaz


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)  # harf duyarlıdır. önce büyük harfleri sonra küçük harfleri sıralar


# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
# print(points.count(9))


# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")
# print(x)


# fruits = ['apple', 'banana', 'cherry']
# fruits.reverse()  # sıralamayı tersine çevirir.
# print(fruits)


# a = [1, 2, 3, 4]
# b = ["ali", "veli"]

# c = list(zip(a,b))  # iki listeyi fermuar gibi birleştirir. kısa listeyi baz alır.
# print(c)


# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)


# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)  # set i genişlettik
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]

# thisset.update(mylist)  # genişletmek için liste tuple veya dict. de kullanabiliriz.
# print(thisset)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)


# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")  # else koymadan bu komudu girintisiz yazarsak da olur.


# string.join() metodu
  
#  Joining with empty separator
# list1 = ['g', 'e', 'e', 'k', 's']
# print(" ".join(list1))
 
# # Joining with string
# string1 = " geeks "
# print("$".join(list1))

# elements in tuples
# list1 = ('1', '2', '3', '4')
 
# put any characher to join
# s = "-"
 
# joins elements of list1 by '-'
# and stores in string s
# s = s.join(list1)
 
# join use to join a list of
# strings to a separator s
# print(s)


