# atama operatörleri
# x, y, z = 5, 16, 20

# x += 5
# x -= 5
# x *= 5
# x /=5
# x %= 5
# y //= 5
# x **= 5
# y *= z 

# print(x, y, z)


# values = 1, 2, 3

# print(values)
# print(type(values))

# x, y, z = values  # unpacking

# print(x, y, z)  # unpack yapabilmek için eksik veya fazla öğe olmamalı

# eğer fazla öğe varsa şu yapılabilir.
# values = 1, 2, 3, 4, 5

# x, y, *z = values  # kalanları z ye liste olarak atar

# print(x, y, z, sep="\n")


# x, y, z = 2, 5, 10

# numbers = 1, 5, 7, 10, 6

# 1. what is the subtraction of sum  x,y,z to multiplation of the two number that given from user
# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))

# print((num1*num2) - (x + y + z))

# 2. y // x = ?
# print(y // x)

# 3. what is modulus of sum of x,y,z?

# print((x + y + z) % 3)

# 4. y  ** x

# print(y ** x ) 

# 5. 

# x , z, *y = numbers
# print(x , y, z)
# print(z**3)
# print(sum(y))


# karşılaştırma operatörleri

# a, b, c, d = 5, 5, 10, 4

# result = (a==b)
# result = (a==c)

# print(result)


# print(False==0)


# vize1 = int(input("enter first vise"))
# vize2 = int(input("enter second vise"))
# final = int(input("enter final result"))

# average = ((vize1 + vize2) / 2) * 0.4 + final * 0.6
# print(f"your mark is: {average}")


# manyıksal operatörler

# x= 5
# name = "ramazan"
# result = 5 < x < 10

# print(result)

# and
# result = (x > 5) and (x < 10)
# print(result)

# result = (x==5) and (name == "ramazan") 
# print(result)


# or
# result = (x > 0) or (x % 2 == 0)
# print(result)

# not

# result = not True
# print(result)


# number = int(input("enter a number"))

# result = (number > 0) and (number % 2 == 0)
# print(f"number is a positive even number : {result} ")


# other python operators

# Identity operator : is

# x = y = [1, 2, 3]
# z = [1, 2, 3]

# print(x == y)
# print(x == z)
# print(x is y)
# print(x is z) # is operatöründe değerlerin aynı olması önemli değil. objelerin aynı olmasına bakılır.


# x = [1, 2, 3]
# y = [2, 4]

# del x[2]
# y[1] = 1
# y.reverse()

# print(x == y)
# print(x is y)
# print(x is not y)


# membership operator : in

# x = ["apple", "banana"]
# print("banana" in x)
# print("apple" not in x)





