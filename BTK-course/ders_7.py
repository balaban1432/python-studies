# for loops

# numbers = [1, 2, 3, 4, 5]

# for num in numbers:
#     print(num)


# names = ["ramazan", "derya", "kemal"]

# for name in names:
#     print(f"my name is {name}")


# name = "ramazan balaban"

# for i in name:
#     print(i)


# tuple = 1, 2, 3, 4, 5

# for i in tuple:
#     print(i)


# liste = [(1, 2), (1, 3), (3, 5), (5, 7)]  # I have just learned. 

# for a,b in liste:
#     print(a, b)


# dictionary = {
#     "k1" : 1,
#     "k2" : 2,
#     "k3" : 3
# }

# for item in dictionary:
#     print(item)  # sadece key leri yazdırır

# for item in dictionary.items():
#     print(item)  


# 1. listedeki hangi sayılar 3 ün katı
# 2. listedeki sayıların toplamı kaçtır
# 3. listedeki tek sayıların karesini alınız

# numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# for num in numbers:
#     if num % 3 == 0:
#         print(num, end=" ")

# sum = 0
# for num in numbers:
#     sum += num
# print(f"sum is: {sum}")    

# for i in numbers:
#     if i % 2 == 1:
#         print(i ** 2)


# 4. şehirlerden hangileri en fazla 5 karakterlidir

# sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

# for i in sehirler:
#     if len(i) <= 5:
#         print(i)


# 5. ürünlerin fiyatları toplamı nedir
# 6. ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz

# urunler = [
#     {"name" : "samsung S6", "price": "3000"},
#     {"name" : "samsung S7", "price": "4000"},
#     {"name" : "samsung S8", "price": "5000"},
#     {"name" : "samsung S9", "price": "6000"},
#     {"name" : "samsung S10", "price": "7000"}
# ]

# sum = 0
# for i in urunler:
#     sum += int(i["price"])
# print(sum)

# for i in urunler:
#     if int(i["price"]) <= 5000:
#         print(i["name"])


# while loops

