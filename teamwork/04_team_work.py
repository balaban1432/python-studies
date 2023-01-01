# 1.
# for x in set('pqr'):
#     print(x * 2)


# 2.
# d = {}
# e = {"john": 40, "peter": 45}
# f = {40: "john", 45: "peter"}

# print(d)
# print(e)
# print(f)


# 3.
# d = {"john":40, "peter":45}
# print(d["john"])  # key in value karşılığını verir


# 4.
# d = {"john":40, "peter":45}
# print(list(d.keys()))


# 5.
# a={}
# a['a']=1
# a['b']=[2,3,4]
# print(a)


# 6.
# z = set('abc')
# z.add('san')
# z.update(set(['p', 'q']))
# print(z)

# z = set('abc')
# z.add('san')
# z.add(set(['p', 'q']))  # add le bu şekilde ekleme yapamıyoruz.
# print(z)

# z=set('abc')
# z.add('san')
# z.add(['p', 'q'])  # gene hata verdi
# print(z)

# z = set('abc')
# z.add('san')
# z.add({'p', 'q'})  # gene hata verdi
# print(z)

# z=set('abc')
# z.add('san')
# z.add('p', 'q')  # gene hata verdi. add ile sadece bir öğe ekleyebiliriz
# print(z)


# 7.
# tuple unpacking
# count, fruit, price = (2, 'apple', 3.5)
# print(count)
# print(fruit)
# print(price)


# 8.
# enumerate() Function

# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)  # başlangıç numarası belirtebiliriz, yoksa 0'dan başlar
# print(list(y))


# college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
# print(list(enumerate(college_years, 2019)))