# 1.
# def printMax(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b, 'is maximum')
        
# printMax(3, 4)


# 2.global ve local değişkenler 

# x = "global x"

# def fonk():
#     y = "local y"
#     print(y)

# fonk()
# print(x)    
# print(y)  # hata verir çünkü yukarıdaki y bir local değişkendir, bir fonksiyonun içinde tanımlanmıştır
          # ve biz buna dışarıdan ulaşamayız. sadece tanımlı olduğu fonksiyonun içinde kullanılabilir.


# x = "global x"

# def fonk():
#     x = "local x"
#     print(x)

# fonk()
# print(x)


# x = "global x"

# def fonk():
#     print(x)

# fonk()  # local x bulamadı bir üst seviyeye çıktı ve orada bulduğu global x değerini kullandı
# print(x)

# enclosing değişkenler
# iç içe fonksiyonlar varsa en içteki geğişken local, bir üstündeki enclosing, onun üstündeki global 

# x = "global x"

# def outer():
#     x = "enclosing x"
#     print(x)
#     def inner():
#         x = "local x"
#         print(x)
#     inner()    

# outer() 
# print(x) 


# x = "global x"

# def outer():
#     x = "enclosing x"
#     print(x)
#     def inner():
#         print(x)
#     inner()    

# outer()  # local x bulamazsa enclosing x i yazacak
# print(x) 


# x = "global x"

# def outer():
#     print(x)
#     def inner():
#         print(x)
#     inner()    

# outer() 
# print(x) 


# x = "global x"

# def fonk():
#     global x  # burada local x değil global x değerini kullanmak istedim ve 
#     x = 5  # x 'e 5 değerini atadım

# fonk() 
# print(x)  


# x = "global x"

# def outer():
#     x = "enclosing x"
#     print(x)
#     def inner():
#         nonlocal x
#         x = 5
#     inner()    
#     print(x) 

# outer()


# x = 50
# def  func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)

# func(x)
# print('x is now', x)


# 3.
# def function1(var1 = 5, var2 = 7):
   
#     print (var1, " ", var2)

# function1()
# function1(10,12)


# def function1(var1 = 5, var2 = 7):
#     var2 = 9
#     var1 = 3
#     print (var1, " ", var2)

# function1()
# function1(10,12)


