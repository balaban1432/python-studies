""" 
Bir lambda fonksiyonu herhangi bir sayıda bağımsız değişken alabilir,
ancak yalnızca bir ifadeye sahip olabilir.
"""

# x = lambda a : a + 10  # Add 10 to argument a, and return the result:
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 8))

# x = lambda a, b, c : a + b + c
# print(x(5, 6, 9))

# Diyelim ki bir bağımsız değişken alan bir işlev tanımınız var ve bu bağımsız değişken bilinmeyen bir sayıyla çarpılacak:
# def my_function(n):
#     return lambda a : a * n

# mydoubler = my_function(2)
# mytripler = my_function(3)

# print(mydoubler(11))
# print(mytripler(11))


# def modular_function(n):
#     return lambda x: x ** n

# power_of_3 = modular_function(3)
# print(power_of_3(5))


# print((lambda x: x**3)(5))


# mean = lambda x, y: (x+y)/2
# print(mean(8, 10))


# multiply = lambda x: x * 4
# add = lambda x, y: x + y
# print(add(multiply(10), 5))


