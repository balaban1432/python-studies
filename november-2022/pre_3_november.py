# empty_tuple = ()
# print(type(empty_tuple))

# try_tuple = ('love')
# print(try_tuple)
# print(type(try_tuple))  # str verdi, 
# It occurs in only single element tuples and we can fix the problem
#  using comma at the end of the element.
# try_tuple = ('love',)
# print(try_tuple)
# print(type(try_tuple))  # tuple verdi


# planets = "mercury", "jupiter", "saturn"
# print(planets)
# print(type(planets))


# emty_tuple = tuple()
# print(empty_tuple)
# print(type(empty_tuple))


# my_tuple = (1, 4, 3, 4, 5, 6, 7, 4)
# my_list = list(my_tuple)  # liste ve tuple arasında dönüşüm yapmak kolaydır.
# print(type(my_list), my_list, sep = "\n") 


# my_list = [1, 4, 3, 4, 5, 6, 7, 4]
# my_tuple = tuple(my_list)
# print(type(my_tuple), my_tuple, sep = "\n")


# mountain = "Alps"
# print(tuple(mountain))  # listelerde olduğu gibi string değişkenler tuple a da dönüşür
# print(list(mountain))

# numbers = 1, 3, 5
# print(numbers)
# print(list(numbers))
# print(tuple(numbers))


# mix_value_tuple = (0, 'bird', 3.14, True)
# print(len(mix_value_tuple))


# even_no = (0, 2, 4)

# print(even_no[0])  # indexleme de yapabiliyoruz
# print(even_no[2])


# And one of the most important differences of tuples from lists is that 'tuple' object
#  does not support item assignment. Yes, because tuple is immutable.
# city_list = ['tokyo', 'Istanbul', 'Moskow', 'Dublin']

# city_list[0] = 'Athens'
# city_list[1] = 'Cairo'
# print(city_list)

# city_tuple = tuple(city_list)
# print(city_tuple)
# city_tuple[0] = 'New York'  # hata verir. tuple da değer atanamaz 

# tuple.index() ve tuple.count() fonksiyonları kullanılabilir
# my_tuple = (4, 'wolf', 'hello', 23, 'Cairo', 4)

# print(my_tuple.index('wolf'))
# print(my_tuple.index(4))
# print(my_tuple.count(4))

# check yourself soruları
# my_list = list(range(11))
# print(my_list[:0:-1])


# grocer = ["banana", ["orange", ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], "water"], "mandarin"]
# print([grocer[1][1][1], grocer[1][1][3], grocer[1][1][5]])  #sebzeleri seçtik

# text = "My two favorite flowers are tulip and rose, two favorite colors are blue and green."
# flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
# colors = ["red", ("blue", ["yellow", "green"]), "pink"]
# flower1 = flowers[0][2]
# flower2 = flowers[0][1][1]
# color1 = colors[1][0]
# color2 = colors[1][1][1]

# print("My two favorite flowers are {0} and {1}, two favorite colors\
#  are {2} and {3}.".format(flower1, flower2, color1, color2))
# print(f"My two favorite flowers are {flower1} and {flower2}, two favorite colors\
#  are {color1} and {color2}.")

# I am 40 years old.
#     I have two children.
#        Data Science is my IT domain.
# escapes = ["\n\t", ("\t", "\t\t"), ["\n", "\n\t\t"]]

# escape1 = escapes[0]
# escape2 = escapes[2][1]
# sentence = "I am 40 years old. I have two children. Data Science is my IT domain."
# sentence = "I am 40 years old.{0}I have two children.{1}Data Science is my IT domain.".format(escape1, escape2)
# print(sentence)
# print(f"I am 40 years old.{escape1}I have two children.{escape2}Data Science is my IT domain.")


#dictionaries  -----  key-value  -----
# empty_ditc_1 = {}
# empty_ditc_2 = dict()
# print(empty_ditc_1, empty_ditc_2)
# print(type(empty_ditc_2))  # < class 'dict' verir


# state_capitals = {'Arkansas': 'Litle Rock',
# 'Colorado': 'Denver',
# 'California': 'Sacramento',
# 'Georgia': 'Atlanta'}

# # print(state_capitals)
# print(state_capitals['Colorado'])  # accessing method # anahtar kelimeyi yazdık ve değeri aldık
# state_capitals['Virginia'] = 'Richmond'  # adding a new item
# print(state_capitals)  # sonuna ekledi.

# anahtarlar ve değerler farklı türlerde olabilir.
# keys are string type below 
# mixed_values = {'animal': ('dog', 'cat'),  # tuple type value
# 'planet': ['Neptun', 'Saturn', 'Jupiter'],  # list type value
# 'number': 40,  # integer type value
# 'pi': 3.14,  # float type value
# 'is good': True}  # boolean type value
# values are string type below
# mix_keys = {22: 'integer',
# 1.2: 'float',
# True: 'boolean',
# 'key': 'string'}
# print(mix_keys)


# dict_by_dict = dict(animal = 'dog', planet = 'neptun', number = 40, pi = 3.14, is_good = True)
# print(dict_by_dict)


# dict_by_dict = {'animal': 'dog', 
# 'planet': 'Neptun', 
# 'number': 40, 
# 'pi': 3.14, 
# 'is good': True}
# print(dict_by_dict) 
# print(dict_by_dict.items()) # çıkan sonuçları iyi incele
# print(dict_by_dict.keys())
# print(dict_by_dict.values())


# dict_by_dict = {'animal': 'dog', 
# 'planet': 'Neptun', 
# 'number': 40, 
# 'pi': 3.14, 
# 'is good': True}

# dict_by_dict.update({'is_bad': 'False'})
# print(dict_by_dict)  # başka bir yolunu daha öğrenmiştik
# dict_by_dict['is_bad'] = 'False'
# print(dict_by_dict)


# dict_by_dict = {'animal': 'dog', 
# 'planet': 'Neptun', 
# 'number': 40, 
# 'pi': 3.14, 
# 'is good': True, 
# 'is_bad': False}

# del dict_by_dict['animal']
# print(dict_by_dict)


# Using the in and the not in operator, you can check if the key is in the dictionary.
# dict_by_dict = {'planet': 'Neptun', 
# 'number': 40, 
# 'pi': 3.14, 
# 'is good': True, 
# 'is_bad': False}

# print('pi' in dict_by_dict)  # bu key i bulursa True verir
# print('animal' not in dict_by_dict)  # bu key i bulamazsa True verir


# #         Nested(içiçe) Dictioneries
# customers = {
#     'bank': 
#  {1: {'name': 'James', 'age': '27', 'sex': 'Male'},
#   2: {'name': 'Nicola', 'age': '25', 'sex': 'Female'},
#   3: {'name': 'Andy', 'age': '38', 'sex': 'Male'},
#   4: {'name': 'Alex', 'age': '19', 'sex': 'Male'},
#   5: {'name': 'Linda', 'age': '33', 'sex': 'Female'},
#   },   
# 'insurance':
# {1: {'name': 'Jashua', 'age': '33', 'sex': 'Male'},
#   2: {'name': 'Marry', 'age': '66', 'sex': 'Female'},
#   3: {'name': 'Adam', 'age': '56', 'sex': 'Male'},
#   4: {'name': 'Samuel', 'age': '54', 'sex': 'Male'},
#   5: {'name': 'Lisa', 'age': '22', 'sex': 'Female'},
#   },
# }

# print(customers['insurance'][5]['age'])


# SETS
# empty_set = set()  # boş set sadece böyle oluşur
# print(type(empty_set))  # type set


# colorset = {'purple', 'orange', 'red', 'darkblue', 'yellow', 'red'}

# print(colorset)
# print(colorset)  # her yazdırmada farklı sırada veriyor.
# bundan dolayı ; unordered and unique


# s = set('unselfishness')
# print(s)  # string türündeki verilerin harfleri sette sadece birkez kullanılır.
# set kullanmak tekrarlardan kaçınmamıza yardımcı olabilir.


# bir listeyi bir set e dönüştürelim ve elemanlarının tekrarına bakalım
# flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
# flowerset = set(flower_list)
# flowerlist = list(flowerset)

# print(flowerset)
# print(flowerlist)  # set hangi değeri verirse list değişmediği için aynı değeri veriyor



# a = set('abracadabra')
# print(a)


# a = set('abracadabra')
# b = set('alacazm')

# print(a-b)  # same as '.difference()' method
# print(a.difference(b))  # a difference from b
# print(a | b)  # same as '.union()' method
# print(a.union(b))  #unification of a with b
# print(a & b)  # same as '.intersection()' method
# print(a.intersection(b))  # intersection of a and b


# a = set('adracadabra')
# a.remove('c')  # setten c silinir
# print(a)
# a.add('c')  # c tekrar eklendi. 
# print(a)  # bunlar da immutable değil. değişkenlikler kalıcı oluyor 
# print(len(a))  # setin uzunluğunu verdi
# print('a' in a)  # a setinde 'a' elemanı var  dedik, True verdi
# print( 'f' not in a)  # a setinde 'f' yok dedik, True verdi
# print('c' not in a)  # a setinde 'c' yok dedik, False verdi


# print(len(set('listen to the voice of enlisted')))


# check yourself sorularından

# numbers = {}
# numbers["x"] = 12
# numbers["y"] = 4  # böyle de ekleme yapabiliyoruz
# numbers.update({"z": 3})  # böyle de yapabiliyoruz
# print(numbers)
# print(numbers["x"])  # x'in değerini bul dedim 12 verdi
# print(numbers["x"] + numbers["y"] + numbers["z"]**2)  # bu şekilde işlem de yapabiliriz.


# numbers_10 = [10, 30, 40, 50, 60, 70, 80, 90, 100]
# numbers_10.insert(1, 20)
# print(numbers_10)


# fruits_vegetables = ["fruit", "vegetable", ["apple", "banana", ["mango", "avocado"]], ["spinach", "broccoli"]]
# print(fruits_vegetables[3][0])


# family_members = ['Meghan', 'Tom', 'Nicole', 'Tim']
# print(tuple(family_members))


# mylist = list(range(5, 50, 3))  # 5 den 50 ye kadar olan sayıları 3 erli listeledi
# print(mylist)  # 50(son sayı) dahil olmuyor.


