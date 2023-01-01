# 1.
# unpack a collection(list, tuple, etc)

# fruits = ["apple", "banana", "cherry"]  
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


# count, fruit, price = (2, 'apple', 3.5)
# print(count)
# print(fruit)
# print(price)

# 2.

# list1 = [1, 2, 3, 4, "banana", "apple"]

# list1.pop()
# print(list1)
# list1.pop(1)  # index belirtebiliriz
# print(list1)
# # list1.delete()
# print(list1)


# 4.
# enumerate() Function

# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)  # başlangıç numarası belirtebiliriz, yoksa 0'dan başlar
# print(list(y))


# college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
# print(list(enumerate(college_years, 2019)))

# 5.
# A.
# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]
# output=[]

# fruit_tuple_0 = (fruits[0], quantities[0], prices[0])
# output.append(output)
# fruit_tuple_1 = (fruits[1], quantities[1], prices[1])
# output.append(output)
# fruit_tuple_2 = (fruits[2], quantities[2], prices[2])
# output.append(output)
# print(fruit_tuple_0, fruit_tuple_1, fruit_tuple_2)


# fruit_tuple_0 = (fruits[0], quantities[0], prices[0])
# output.append(fruit_tuple_0)
# fruit_tuple_1 = (fruits[1], quantities[1], prices[1])
# output.append(fruit_tuple_1)
# fruit_tuple_2 = (fruits[2], quantities[2], prices[2])
# output.append(fruit_tuple_2)
# print(output)

# B.
# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]
# i = 0
# output = []
# for fruit in fruits:
#     temp_qty = quantities[i]
#     temp_price = prices[i]
#     output.append((fruit, temp_qty, temp_price))
#     i += 1
# print(output)

# C.
# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]
# groceries = zip(fruits, quantities, prices)
# print(list(groceries))

# D.
# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [5, 3, 4]
# prices = [1.50, 2.25, 0.89]
# i = 0
# output = []
# for fruit in fruits:
#     for qty in quantities:
#         for price in prices:
#             output.append((fruit, qty, price))
#     i += 1
# print(output)

# 6.
# sum() Function
# The sum() function returns a number, the sum of all items in an iterable.



# a = (1, 2, 3, 4, 5)
# x = sum(a)
# print(x)


# sum(iterable, start) 

# a = (1, 2, 3, 4, 5)
# x = sum(a, 7)  # Start with the number 7, and add all the items in a tuple to this number
# print(x)


# a=[1, 2, 3, 4]
# b=[sum(a[0:x+1]) for x in range(0,len(a))]
# print(b)

# 7.
# L1 = []
# L1.append([1, [2, 3], 4])  # L1 = [[1, [2, 3], 4]]
# L1.extend([7, 8, 9])       # L1 = [[1, [2, 3], 4], 7, 8, 9]
# print(L1[0][1][1] + L1[2])

# 8.

# T = (1, 2, 3, 4, 5, 6, 7, 8)
# print(T[T.index(5)], end = " ")
# print(T[T[T[6]-3]-6])

# 9.

# D = {1 : 1, 2 : '2', '1' : 1, '2' : 3}

# D.update({'1': 2})
# print(D)

# D['1'] = 2  
# print(D)

# print(D['1'])

# D['1'] = 2  
# print(D[D[D[str(D[1])]]])

# 10.

# set1 = {1, 2, 3}
# set2 = set1.copy()

# set2.add(4)
# print(set1)

# print(set2)