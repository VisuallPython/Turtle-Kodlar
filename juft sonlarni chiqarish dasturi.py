import turtle  # Juft sonni chiqarish dasturi
# import turtle
# son = int(input('Son kiriting: \n>>>'))
# i = 2
# while i <= son:
#     print(i)
#     i += 2


    # for operatori
# from turtle import Turtle
# chiziq = Turtle()
# chiziq.color('red')
# chiziq.speed(15)
# for i in range(50):
#     chiziq.circle(100)
#     chiziq.left(55)
# chiziq.write('Jarayon tugadi')
#
# turtle.mainloop()


from turtle import Turtle
chiziq = Turtle()
chiziq.speed(8)
chiziq.hideturtle()

for i in range(8):
    chiziq.forward(100)
    chiziq.left(180)
    chiziq.forward(30)
    chiziq.left(135)
    chiziq.forward(35)
    chiziq.left(180)
    chiziq.forward(35)
    chiziq.right(86)
    chiziq.forward(35)      #backward
    # chiziq.left(45)
turtle.mainloop()
