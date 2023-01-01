# my_tuple = ("wakabayashi",)  # virgül koymazsak type tupple vermez, str verir
# my_tuple2 = "wakabayashi"
# my_tuple2 = tuple("wakabayashi")
# print(my_tuple, type(my_tuple), sep = "\n")
# print(my_tuple2)


# my_tuple = (1, 2, 3, 4, 564, 7, 863)
# my_list = list(my_tuple)

# print(my_tuple, type(my_tuple), sep = "\n")
# print(my_list, type(my_list), sep= "\n")
# print(my_tuple[3])
# print(my_tuple[3:5])


# sehirler = ["Istaanbul", "Izmir", "Ankara", "Van", "Erzurum", "Sivas", "Gonya","Sinop", "Muğla", "Gaziantep"]
# print(sehirler)
# sehirler_tuple = tuple(sehirler)
# sehirler[9] = "Yozgat"
# print(sehirler)
# sehirler_tuple[0] = "Mus"  # tuple a ekleme olmaz


# dicyionaries
# key-value  ;  key tek dir. bir key için birden fazla value olabilir.

# first_dict = {"cola": 25, "ekmek": 5, "makarna": 5}
# print(first_dict)
# print(dict(kola = 5, ekmek = 5, makarna = 5))


# state_capitals = {"Arkansas": "Little Rock",
#                   "Colorado": "Denver",
#                   "California": "Sakremento",
#                   "Georgia": "Atlanta"
#                   }
# state_capitals["Virginia"] = "Ricmond"
# print(state_capitals)                 
# print(state_capitals["Colorado"])  # "Denver" verir


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


# my_dictionary = dict(animal = ("dog", "cat"), planet = ("mars", "jupiter"), number = 5)
# print(my_dictionary)


# dict_by_dict = {'animal': 'dog', 
# 'planet': 'Neptun', 
# 'number': 40, 
# 'pi': 3.14, 
# 'is good': True}
# print(dict_by_dict) 
# print(dict_by_dict.items()) # çıkan sonuçları iyi incele ve satır atladı
# print(dict_by_dict.keys())
# print(dict_by_dict.values())
# dict_by_dict.update({'is_bad': True})
# print(dict_by_dict)
# del dict_by_dict['is good']
# print(dict_by_dict)
# print("planet" in dict_by_dict)
# print("pi" not in dict_by_dict)

# nested dictionary
# school_records={
# 	'personal_info':
# 		{'kid':{'tom':{'class':'intermediate', 'age':10},
# 			'sue':{'class':'elemantary', 'age':8}
# 			},
# 		'teen':{'joseph':{'class':'college', 'age':19},
# 			'marry':{'class':'high school', 'age':16}
# 			},
# 		},
#     'grades_info':
# 		{'kid':{'tom':{'math':88, 'speech':69},
# 			'sue':{'math':90, 'speech':81}

# 			},
# 		'teen':{'joseph':{'coding':80, 'math':89},
# 			'marry':{'coding':70, 'math':96}
# 			},
# 		}
# }

# print(school_records['grades_info']['kid']['sue']['speech'])

# family = {
#       "erkek": {"baba": {"yas": 45, "meslek": "emekli"},
#                 "kardes": {"yas": 21, "meslek": "ogrenci" },
#                },
#       "kadın": {"anne": {"yas": 42, "meslek": "ev hanımı"},
#                 "abla": {"yas": 28, "meslek": "ogretmen"},
#                },
#         }
# print(family)
# print(family["kadın"]["abla"]["yas"])


# SETS
# set_1 = {'red', 'blue', 'pink', 'red'}
# colors = 'red', 'blue', 'pink', 'red'
# set_2 = set(colors)
# print(type(set_1))
# print(type(set_2))


# flower_list = ['rose', 'violet', 'carnation', 'rose', 'orchid', 'rose', 'orchid']
# flower_set = set(flower_list)

# print(flower_list)
# print(flower_set)


# a = set("ankara")
# b = set("istanbul")
# c = set("izmir")
# print(a, b, c, sep='\n')

# print(a.difference(b))  # a fark b == a - b
# print(b.difference(a))  # b fark a == b - a
# print(a.union(b))  # a birleşim b  == a | b
# print(a.intersection(b))  # a kesişim b  == a & b
# print(a.difference(b, c))
# print(a.intersection(b, c))  # empty set verir

# ödev çalışmaları
# task_1
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0:4:3])

# task_2
# file_name = "abc.java"
# print(file_name[4:])

# task_3
# Sample_data = "3", "5", "7", "23"
# my_list = list(Sample_data)
# my_tuple = tuple(Sample_data)
# print(f"List:{my_list}\nTuple:{my_tuple}")

# task_4
# Sample_String = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# escape1 = "\n\t"
# escape2 ="\n\t\t"
# escape3 = "\n"
# Sample_String = f"Twinkle, twinkle, little star,{escape1} How I wonder what\
# you are!{escape2} Up above the world so high,{escape2} Like a diamond \
# in the sky.{escape3} Twinkle, twinkle, little star,{escape1} How I wonder what you are"
# print(Sample_String)       

# task_5
# r = input("r")
# r1 = float(r)
# pi = 3.14
# area = pi * (r1**2)
# print(area)