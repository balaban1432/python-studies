# text = 'WWW.clarusway.com'
# print(text.endswith('.com'))
# print(text.endswith('com.'))
# print(text.startswith('http:'))


# sentence = "I live and work in Turkey"
# print("I live and work in Turkey".capitalize())
# print(sentence.capitalize())
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.title())
# print(sentence.replace("Turkey", "Virginia"))
# print(sentence.swapcase())


# text = "Clarusway.com"
# print(text.replace("s", "m"))

# print(sentence)
# print(text)  # sonuçta verilerimiz değişmedi. immutable.
# string operasyonlarımızın ürettiği sonucu bir değişkene atamazsak bir şey değişmez
# sentence = sentence.upper()  # şimdi verimizi değiştirdik.
# print(sentence)  # artık sentence eski sentence değil  


# sentence = "I live and work in Turkey"
# print(sentence.capitalize().upper().lower().title())


# text = 'the better the family, the better the society'
# print(text.title())


# text = "S0d0me and G0m0re"
# text_1 = text.replace("0", "o")
# print(text_1)


# space_string = "      listen first        "
# print(space_string.strip())  # iki taraftaki bütün boşlukları kaldırdı


# source_string = "interoperability"
# print(source_string.strip("yi"))  # "yi" yerine "iy" yazılsa da aynı sonucu verir
# print(source_string.lstrip("in"))  #  "in" yerine "ni" yazılsa da sonuç değişmezdi


# space_string = "       listen first       "
# print(space_string.rstrip())  # sadece sağdaki boşlukları siler


# source_string = "interoperability"
# print(source_string.rstrip("yt"))  # "yt" or "ty"


# text = 'tyou can learn almost everything in pre-classz'
# print(text.lstrip('t').rstrip('z').upper())
# print(text.strip('tz'))  # yukarıdakinin aynı sonucu verdi.

# text = ["Kuroko no Basket", 36, ["Slam Dunk"], 3.14]
# print(text)


# liste = ["happy", 36, 3.14, ["unhappy"]]
# liste2 = "happy"
# print(liste)
# print(list(liste))  # sonuç aynı zaten listeydi
# print(list(liste2))
# print(liste2)  # liste2 verisi artık değişti immutable değil yani


# country = ["USA", "New Zerland", "Finland", "Sweden", "Syria", "Turkey"]
# print(country)


# mixed_list = [11, 'Joseph', False, 3.14, None, [1,2,3]]
# output = list(mixed_list)
# print(output)


# my_list = ["Aslan", "Clarusway", "2022"]
# new_list1 = list(my_list)
# new_list2 = [my_list]
# print(new_list1)
# print(new_list2)
# print(len(new_list1))
# print(len(new_list2))



# empty_list = []
# empty_list.append(1)
# empty_list.append("Multiverse")
# empty_list.append("Multiuniverse")
# empty_list.append(3.14)
# empty_list.append([5])
# print(empty_list)  # sıra ile indexledi ve listemiz artık ilk liste değil.


# city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
# city.append('Addis Ababa')
# print(city)  # .append işlemi ile index sırasına uyarak yeni bileşeni listenin sonuna ekledi.


# empty_list = []
# empty_list.append(1) 
# empty_list.append(2) 
# empty_list.append(3) 
# empty_list.append(4) 
# print(empty_list)


# liste_5 = [1, 4, 7]
# liste_5.insert(0, 5)
# liste_5.insert(0, "string")
# print(liste_5)
# liste_5.pop()  # son indexdeki öğeyi atar
# liste_5.remove(5)
# print(liste_5)


# mix_list = [3, 5, 2, 9, 0]
# mix_list.sort()
# print(mix_list)  # farklı veri tipleriyle çalışmaz.
# yani liste içinde string ve integer varsa hata verir.
# sadece string olursa alfabetik sıra sadece int. olursa rakamsal sıra


# list_1 = ['one', 'four', 'nine']
# list_2 = ['@', '*-', 'False']
# list_3 = [True, False, None]
# list_4 = [[3], [44], [-12]]
# list_5 = [[1, 3], [44, -40], [-12, 1]]
# print(len(list_1))
# print(len(list_2))
# print(len(list_3))
# print(len(list_4))
# print(len(list_5))


# list_5 = [[1, 3], [44, -40], [-12, 1]]
# print(list_5[1])
# print(list_5[1][0])


# # [start:stop:step]

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[:])

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[3:])

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[:5])

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[::2])


# odd_numbers = list(range(11))
# print(odd_numbers[1::2])