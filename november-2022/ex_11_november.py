# yazı-tura oyunu
# import random
# coin = ("yazi", "tura")
# yazi, tura = 0, 0
# games = 0

# print("Cikmak icin x e basiniz.")

# while True:
#     flip = random.choice(coin)
#     your_choice = input("Yazi mi Tura mi? ").lower()
#     if your_choice == "x":
#         print("GAME OVER")
#         print("Oyun istatistikleri: ")
#         print(f"Kac kere oynadiniz: {games}")
#         print(f"Kac kere yazi geldi: {yazi}")
#         print(f"Kac kere tura geldi: {tura}")
#         break
#     if your_choice == flip:
#         print(f"Para {flip} geldi. Bravo!")
#         games += 1
#     else:
#         print(f"Para {flip} geldi. Tekrar deneyiniz.")
#         games += 1
#     if flip == "yazi":
#         yazi += 1
#     elif flip == "tura":
#         tura += 1


# bilgisayar 1 den 5 e kadar bir sayı seçip tahmin isteyecek(tahmin sayısı 3 olacak):
# import random
# randomnumber = random.randint(1, 5)  #  randint, random modülünün bir metodudur. bize verdiğimiz parametrelere göre bize rastgele tamsayı üretir. burada 1 ile 5 arasında bir sayı üretecek
# guesscount = 0
# guesslimit = 3
# while guesscount < guesslimit:
#     guess = int(input("Enter your guess: "))   
#     if guess == randomnumber:
#         print("You won!")
#         break
#     guesscount += 1
# else:
#      print("Sorry, you failled!")    