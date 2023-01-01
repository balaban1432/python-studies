# def first_function(argument_1, argument_2):
#     print(argument_1**2 + argument_2**2)

# first_function(2,3)  # yazarken fonksiyonu hemen tanıdı ve çalıştırınca sonucu verdi
# first_function(2,5)

# çarpma fonksiyonu tanımlayalım

# def multiply(a, b):
#     print(a * b)

# multiply(3, 5)
# multiply(-1, 2.5)
# multiply("amazing", 3)


# def motto():  # arguman kullanmadan da yapabiliyoruz.
#     print("Don't hesitate to reinvent yourself!")

# motto()    


# def greetUser(firstName, lastName, message = "welcome my home"):
#     print(f"Hi {firstName} {lastName}")
#     print(message)

# greetUser("ramazan", "balaban")  # message parametresine varsayılan değer atadım. fonksiyon içine yazmasam da varsayılan değeri kullanır. 
# greetUser("ramazan", "balaban", "how are you?")  # message kısmına istediğim mesajı yazarsam varsayılan değeri görmez


# def get_Greet_User (firstName, LastName):
#     return f" Hi {firstName} {LastName} ! "  # burada bir değer döndürüyor. döndürdüğü bu değeri aşağıdaki değişkene atıyor.
 
# greetingMessage = get_Greet_User("ramazan", "balaban")  # return değer çağırdığımızda değişkene atandı.
# print(greetingMessage)


# def multiply_1(a, b):
#     print(a * b)

# def multiply_2(a, b):
#     return a * b

# multiply_1(10, 5)
# print(multiply_2(10, 5))        

# print(type(multiply_1(10, 5)))  # < class 'NoneType' >
# print(type(multiply_2(10, 5)))  # < class 'int' >


# def my_function(width, height):
#     area = width * height
#     return area

# print(my_function(3, 4))


# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print("Your initials are: " \
#     + get_initial(first_name) \
#     + get_initial(last_name))


# dik üçgende hipotenüs hesabı

# def my_function(a, b):
#     hypotenuse = (a ** 2 + b ** 2) ** 0.5
#     return hypotenuse
    
# print(my_function(3, 4))
# print(my_function(6,8))

# def longer(a, b):
#     if len(a) >= len(b):
#         return a
#     else:
#         return b

# a = input("enter first name")
# b = input("enter second name")
# print(longer(a, b))


# def team_names(*teams) :  # Parametreden önce yıldız işareti konularak rastgele sayıda bağımsız değişken yöntemi kullanılmıştır.
#     print('The teams in Premier League are :')
#     for i in teams :
#         print('-', i)

# team_names('Liverpool', 'M.United', 'M.City', 'Arsenal', 'Everton')


# def make_sentence(**kwargs):  # ** konumsal bağımsız değişkenleri kabul etmek yerine anahtar kelime bağımsız değişkenlerini kabul eder.
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for i in kwargs.values():
#         result += i
#     return result

# print(make_sentence(a="I ", b="love ", c="Clarusway!"))


# city = "I love Paris!"

# def my_function(): 
#     city = "I love London!"
#     print(city) 

# my_function()


# def sum_double(x, y):
#     if x == y:
#         return 2 * (x + y)
#     else:
#         return x + y
  
# print(sum_double(1, 2))
# print(sum_double(5, 7))
# print(sum_double(5, 5))


