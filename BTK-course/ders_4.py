# Tupples
# tuple1 = 1, "iki", 3  # parantez koymasak da tupple oluyor
# tuple2 = (1, "iki", 3)

# print(tuple1)
# print(tuple2)
# print(type(tuple1))
# print(type(tuple2))


# mytupple = ("a", 2, "ali", 5, 2, "veli")
# print(mytupple.count(2))
# print(mytupple.index("ali"))

# tuple2 = (45, 69) + mytupple
# print(tuple2)

# Dictioneries

# plakalar = {"kocaeli" : 41, "istanbul" : 34}
# print(plakalar["kocaeli"])
# print(plakalar["istanbul"])

# plakalar["ankara"] = 6
# print(plakalar)
# plakalar["istanbul"] = "nev value"
# print(plakalar)


# users = {
#     "ramazan" : {
#         "age" : 41,
#         "email" : "balaban@gmail.com",
#         "adress" : "bolu",
#         "phone" : "123456",
#         "roles" : ["admin", "user"]
#     },
#     "derya" : {
#         "age" : 36,
#         "email" : "derya@gmail.com",
#         "adress" : "bolu",
#         "phone" : "789456",
#         "user" : ["user"]
#     }   
# }

# print(users["ramazan"])
# print(users["ramazan"]["age"])
# print(users["ramazan"]["email"])
# print(users["ramazan"]["roles"][0])


# students = {
#     "120" : {
#         "name" : "Ali",
#         "surname" : "Yılmaz",
#         "phone" : "5320125254"
#     },
#     "125" : {
#         "name" : "Can",
#         "surname" : "Korkmaz",
#         "phone" : "5320155552",
#     },
#     "128" : {
#         "name" : "Volkan",
#         "surname" : "Yüksel",
#         "phone" : "5324566652",
#     },
# }

"""
1. bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle 
dictionary içinde saklayınız.
2. öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin
"""
# number = input("enter your number")
# name = input("enter your name: ")
# surname = input("enter your surname")
# phone = input("enter your phone")

# students.update({number : {"name" : name, "surname" : surname, "phone" : phone}})
# students[number] = {"name" : name, "surname" : surname, "phone" : phone}  # second way
# print(students)

# number = input("enter your number")
# print(students[number])


# sets
# fruits = {"orange", "apple", "banana"}

# indexlenemez, herdefasında farklı şekilde görünür.

# fruits.add("cherry")
# fruits.update(["mango", "grape"])
# fruits.add("apple")  # set içinde her elemandan 1 adet olur. ikinci bir defa eklemez.

# print(fruits)


# mylist = [1, 2, 3, 5, 2, 8, 5]
# print(set(mylist))


# fruits = {"orange", "apple", "banana", "mango"}
# fruits.remove("orange")
# fruits.discard("apple")
# fruits.pop()  # son elemanı siler ama setler sıralı olmadığı için herhangi bir elemanını siler
# print(fruits)

# print(fruits.clear())
# print(fruits)


#  value types

# x = 5
# y = 25

# x = y
# y = 10  # burada y nin değişmesi yukarıdaki x i etkilemez.
# print(x, y)
# x = y
# print(x, y)


# reference types

# a = ["apple", "banan"]
# b = ["apple", "banan"]

# b[0] = "grape"

# print(a, b, sep="\n")

# a = ["apple", "banan"]
# b = ["apple", "banan"]

# a = b

# b[0] = "grape"  # b nin içindeki değişiklik a ya da yansır. burada adresleme var.

# print(a, b, sep="\n")