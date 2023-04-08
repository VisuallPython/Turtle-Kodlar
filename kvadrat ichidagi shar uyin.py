from turtle import Turtle, Screen
oyna = Screen()
oyna.title('Sharning devordan qaytishi.')

# 1-qadam
chiziq = Turtle()
chiziq.color('green')
chiziq.pensize(7)
chiziq.hideturtle()     # turtleni ko'rinmas qiladi
chiziq.speed(0)         # chiziqni chizish vaqti 0 ga teng

chiziq.up()
chiziq.goto(300, 300)    # kordinatani [300,300] ga o'zgartirish
chiziq.down()

chiziq.goto(300, -300)
chiziq.goto(-300, -300)
chiziq.goto(-300, 300)
chiziq.goto(300, 300)

shar = Turtle()
shar.color('orange')
shar.shape('circle')
shar.up()
shar.goto(0, 0)     # shu ikki qiymat kiritilsa shar izidan chiziq qolmaydi!


# 2-qadam
chiziq_1 = Turtle()
chiziq_1.color('blue')
chiziq_1.pensize(7)
chiziq_1.hideturtle()
chiziq_1.speed(0)

chiziq_1.up()
chiziq_1.goto(-300, -300)
chiziq_1.down()

chiziq_1.goto(-300, -260)
chiziq_1.goto(-20, -260)
chiziq_1.goto(-20, -300)
chiziq_1.goto(-300, -300)


# 1 - qadam While qismi
qadam_x = 7
qadam_y = 5
while True:
    x, y = shar.position()
    if x + qadam_x >= 300 or x + qadam_x <= -300:
        qadam_x = -qadam_x

    if y + qadam_y >= 300 or y + qadam_y <= -300:
        qadam_y = -qadam_y


# 2- qadam While qismi: sharni to'xtatish uchun shart:
    while True:
        if x + qadam_x <= -300 or x + qadam_x >= -20:
            break
        if y + qadam_y >= -260 or y + qadam_y <= -300:
            break
        oyna.exitonclick()      # Funksiyadan chiqishni ta'minlaydi!

    shar.goto(x + qadam_x, y + qadam_y)