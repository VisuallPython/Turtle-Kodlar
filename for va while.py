    #1-misol

# while True:     '''Bizdan cheksiz ism so'raydi.'''
#     name = input('Ismingizni kiriting:\n>>> ')
#     print('Salom', name, 'Qayd etish muvaffaqiyatli bajarildi.')



    #2-misol

# import turtle
# t = turtle.Turtle()
# t.speed(0)
# t.color('seagreen')
# count = 0
# while True:
#     t.forward(count)
#     t.circle(count)
#     t.right(count)
#     count = count + 1
# turtle.done()



    # 3-misol

# import random
# for i in range(10):
#     x = random.randint(10,100)
#     print(x)
#


    # 4 - misol

# import turtle
# import random
# import rgb
# t = turtle.Turtle()
# t.speed(0)
#
# for i in range(50):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     uzunlik = random.randint(1, 50)
#     burchak = random.randint(1, 360)
#
#     t.color((r, g, b))
#     t.forward(uzunlik)
#     t.right(burchak)
#
# turtle.done()



    # 5-misol:  G'orda qanday ajdar borligini aniqlash

# import random
# import time
#
# print('Oldingizda ikkita g\'orni ko\'rasiz! ')
# time.sleep(1)
# print('birinchisi xazinalarini siz bn baham ko\'radi. ')
# time.sleep(1)
# print('ikkinchisi juda ochko\'z')
#
# tanlash = int(input('Qaysi g\'orga borasiz?  1/2\n>>> '))
# ran = random.randint(1,2)
#
# if tanlash == ran:
#     print('U yaxshi ajdahoni tanladi! ')
#     time.sleep(1)
# else:
#     print('Siz o\'ldingiz.')
