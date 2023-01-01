# 1.
# def san(x):
#     print(x+1)
# x=-2
# x=4
# san(12)

# print(x)


# 2.
"""
min() Return the lowest number:
max() Return the largest number:
alfabetik olarak da sıralar
"""
# a = (1, 5, 3, 9)
# x = min(a)
# print(x)

# x = min("Mike", "John", "Vicky")
# print(x)

# x = max("Mike", "John", "Vicky")
# print(x)

# a = (1, 5, 3, 9)
# x = max(a)
# print(x)


# def foo(fname, val):
#     print(fname(val))
# foo(max, [1, 2, 3])
# foo(min, [1, 2, 3])


# 3.
# count = 0
# my_string = "Clarusway"
# my_char = "a"
# for i in my_string:
#     if i == my_char:
#         count += 1
# print(count)


# 4.
# num = 2013
# reversed_num = 0

# while num != 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num //= 10

# print(reversed_num)


# 5.
""" 
Bir lambda fonksiyonu herhangi bir sayıda bağımsız değişken alabilir,
ancak yalnızca bir ifadeye sahip olabilir.
"""
# x = lambda a : a + 10  # Add 10 to argument a, and return the result:
# print(x(5))


# f = lambda x : bool(x % 2)
# print(f(20), f(21))


# 6. random modülü
# import random
# random.randrange(0,91,5)  # randrage, random modülünün bir metodudur. bize verdiğimiz parametrelere göre bize rastgele tamsayı üretir.
# x = random.randrange(0,91,5)  # randrage(a,b,c) a=start b=stop c=step
# print(x)


# import random
# random.randint(0,91)  
# x = random.randrange(0,91)  
# print(x)


# 7.
# def foo():
#     try:
#         return 1
#     finally:
#         return 2

# k = foo()
# print(k)          


# 8. assert
"""
  Assert anahtar sözcüğü(def, if, break, for gibi), kodda hata ayıklanırken
kullanılır.
  Assert anahtar sözcüğü, kodunuzdaki bir koşulun True döndürüp döndürmediğini 
test etmenizi sağlar, aksi takdirde program bir AssertionError hatası verir.
  Kod False döndürürse yazılacak bir mesaj yazabilirsiniz,
"""

# initializing list of foods temperatures
# batch = [ 40, 26, 39, 30, 25, 21]
 
# initializing cut temperature
# cut = 26
 
# using assert to check for temperature greater than cut
# for i in batch:
#     assert i >= 26, "Batch is Rejected"
#     print (str(i) + " is O.K" )

# for i in batch:
#     assert i >= 26
#     print (str(i) + " is O.K" )

# for i in batch:
    
#     print (str(i) + " is O.K" )


# x = 10
# y = 8
# assert x > y, 'x too small'

# print(x > y)


# x = 10
# y = 15
# assert x > y, 'x too small'

# print(x > y)


# 10.
# valid = False

# while not valid:
#     try:
#         n = int(input("Enter a number"))
#         while n % 2 == 0:
#             print("Bye")  # bunun altına break ekleyebiliriz 
#         valid = True
#     except ValueError:
#         print("invalid")

""" çift sayı yazarsak "bye" çıktısı sonsuz döngüye girer
    sonsuz döngüye girsin istemiyorsak break ekleriz
    tek sayı yazarsak  döngü başa geldiğinde false olup durdu
    harf girersek value error verir invalied yazdırır ve tekrar döngü başlar
"""      

# 16.
# def f(x, y, z): return x + y + z

# f(2, 30, 400)
# print(f(2, 30, 400))


# def f(x, y, z):
#      return x + y + z

# f(2, 30, 400)
# print(f(2, 30, 400))


# 17.
# x = {a ** 2 for a in range(4)}
# print(x)

# aslında biz bunu şöyle yapıyorduk
# set1 = set()

# for i in range(4):
#     x = i ** 2
#     set1.add(x)
# print(set1)    


# x = [i for i in range(11)]
# y = list(range(11))
# print(x, y, sep="\n")


# 18.
import copy

# a = [10, 23, 56, [78]]
# b = copy.deepcopy(a)

# c = copy.copy(a)

# print(b)
# print(c)


# a = [10, 23, 56, [78]]
# b = copy.deepcopy(a)  # Derin kopyalama durumunda, nesnenin bir kopyası başka bir nesneye kopyalanır.Bu, nesnenin bir kopyasında yapılan herhangi bir değişikliğin orijinal nesneye yansımadığı anlamına gelir.
# a[3][0] = 95
# a[1] = 34

# print(b)


# a = [10, 23, 56, [78]]
# b = copy.copy(a) 
# a[3][0] = 95
# a[1] = 34

# print(b)


# 19.
# a = [1, 2, 3, 4]
# b = [sum(a[0: x + 1]) for x in range(0, len(a))]

# print(b)


# 20.
# print('abcefd'.replace('cd', '12'))  # 'cd' bulamasığı için aynısını verir

# print('abcefcd'.replace('cd', '12'))