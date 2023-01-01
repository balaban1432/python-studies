"""string metotları"""
# message = "Hello There. My name is Ramazan Balaban"
# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()
# message = message.swapcase()


# print(message)


# message = "    Hello There. My name is Ramazan Balaban    "
# message = message.strip()

# print(message)


# message = "Hello There. My name is Ramazan Balaban"
# message = message.split()  # önce parçaladık ve bir listeye attık

# message = " ".join(message)  # listedeki öğeleri bir boşluk ekleyerek tekrar birleştirdik.

# print(message)


# message = "Hello There. My name is Ramazan Balaban"
# message = message.split(".")

# message = " ----" .join(message)

# print(message)


# message = "Hello There. My name is Ramazan Balaban"

# index = message.find("Ramazan")
# index1 = message.index("Ramazan")

# print(index)
# print(index1)

# print(message.startswith("H"))
# print(message.startswith("Hf"))
# print(message.endswith("n"))
# print(message.replace(" ", "*"))
# print(message.center(100))  # 100 karakterlik alan oluşturur ve o alanın içine ortalar.
# print(message.center(50, "*"))  # 50 karakterlik alan oluşturur ve o alanın içine ortalar. kalan boşlukları * ile doldurur


# print("contents".center(50, "*"))


# website = "http://www.ramazanbalaban.com"
# course = "python kursu: Baştan sona Python Programlama Rehberiniz (40 saat)"

# website içinden ramazanbalaban haricindekileri sil
# print(website.strip("hpt:/w.mco"))  # silmek istediğimiz karakterleri sırasız yazabiliriz.

# website içinde kaç tane a karakteri vardır
# print(website.count("a"))

# print(website.startswith("www"))
# print(website.endswith("com"))
# print("com" in website)
# print(website.isdigit())
# print(website.isalpha())
# print(website.isalnum())
# print(website.islower())
# print(website.isupper())
# print(website.istitle())
# print(course.replace(" ", "-"))
# print(course.replace(" ", ""))
# print(f"{website :*^80}")  # bunlar da vardı hatırla
# print(f"{website :*>80}")
# print(f"{website :*<80}")
# print(course.split())
# print(course.split("e"))


"""listeler"""

# my_list = [1, "bir, 5.6, True"]
# print(my_list)


# list1 = ["one", "two","three"]
# list2 = ["four", "five", "six"]

# my_list = list1 + list2
# print(my_list)
# print(len(my_list))
# print(my_list[2])


"""uygulama"""
# bmw, mercedes, opel, mazda elemanlarına sahip bir liste oluştur
# liste = ["opel", "mercedes", "bmw", "mazda"]

# liste kaç elemanlıdır
# print(len(liste))

# listenin ilk ve son elemanı
# print(liste[0], liste[-1])

# mazda yı toyota ile değiştir
# liste[3] = "toyota"

# mercedes listenin bir elemanımıdır
# print("mercedes" in liste)

# -2index nedir
# print(liste[-2])

# listenin ilk 3 elemanını alın
# print(liste[:3])

# listenin son iki elemanı yerine toyota ve renault ekle
# liste[-1] = "toyota"
# liste[-2] = "renault"
# liste[-2:] = ["toyota", "renault"]

# listenin üzerine audi ve nissan değerlerini ekle
# liste.append("audi")
# liste.append("nissan")
# liste.extend(["audi","nissan"])

# listenin son elemanını sil, ilk elemanını sil
# liste.pop()
# del liste[-1]
# liste.pop(0)

# liste elemanlarını tersten yazdır
# liste.reverse()
# print(liste[::-1])

# liste.clear()
# print(liste.count("bmw"))
# print(liste.index("bmw"))
# liste.insert(0, "fiat")
# liste.sort()
# liste.remove("mazda")


# print(liste)

# liste1 = liste.copy()
# print(liste1)


# numbers = [1, 10, 5, 16, 4, 9, 10]
# letters = ["a", "g", "s", "b", "y", "a", "s"]

# print(min(numbers))
# print(min(letters))
# print(max(numbers))
# print(max(letters))
# print(numbers[3:6])
# print(numbers[::2])
# numbers.append("49")
# numbers.insert(3, 78)
# numbers.insert(-2, 52)
# numbers.pop()
# numbers.pop(0)
# numbers.remove(4)
# letters.sort()
# print(letters.count("a"))

# print(letters)
# print(numbers)

# name = "ramazan"
# print(list(name))

# cars = []
# x = input("enter a car brand")
# y = input("enter a car brand")
# z = input("enter a car brand")

# cars.append(x)
# cars.append(y)
# cars.append(z)
# print(cars)


