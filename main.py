#Kütüphaneler
import turtle
import random
import time

#Ekran ayarları
game_screen = turtle.Screen()
game_screen.bgpic("pictures/beach.gif")
game_screen.title("Turtle Game")

#Ekran uzunluk-genişlik tanımlaması
width = game_screen.window_width()
height = game_screen.window_height()

#Projede kullanılacak olan turtleların tanımlaması
turtle_move = turtle.Turtle()
turtle_score = turtle.Turtle()
turtle_countdown = turtle.Turtle()
turtle_reset = turtle.Turtle()
turtle_reset2 = turtle.Turtle()

#Hareket edecek olan kaplumbağanın özellikleri
resim = 'pictures/turtle.gif'
turtle.register_shape(resim)
turtle_move.shape(resim)
turtle_move.turtlesize(2)
turtle_move.color("Green4")

#Skoru gösterecek olan turtle'ın özellikleri
turtle_score.hideturtle()
turtle_score.speed(0)
turtle_score.penup()
turtle_score.setpos(0, 370)
turtle_score.color("Royal Blue")
turtle_score.write(arg="Score: 0 ", align="center", font=("Verdana", 18,"bold")) #Default skor gösterimi

#Zamanı sayacak olan turtle'ın özellikleri
turtle_countdown.hideturtle()
turtle_countdown.speed(0)
turtle_countdown.penup()
turtle_countdown.setpos(0, 340)
turtle_countdown.clear()

#Resetlenme tuşunu yazacak olan turtle'ın özellikleri
turtle_reset.hideturtle()
turtle_reset.speed(0)
turtle_reset.penup()
turtle_reset.setpos(-300, 340)
turtle_reset.clear()
turtle_reset.color("Black")
turtle_reset.write(arg="Press 'r' for reset", align="center", font=("Time New Roman",17,"bold"))

#Yazılan Press'r' for reset yazısının etrafındaki çerçeve turtle'ının özellikleri (görsellik)
turtle_reset2.hideturtle()
turtle_reset2.speed(0)
turtle_reset2.penup()
turtle_reset2.setpos(-400, 334)
turtle_reset2.clear()
turtle_reset2.pendown()
turtle_reset2.pensize(3)
turtle_reset2.color("red4")
turtle_reset2.forward(200)
turtle_reset2.left(90)
turtle_reset2.forward(40)
turtle_reset2.left(90)
turtle_reset2.forward(200)
turtle_reset2.left(90)
turtle_reset2.forward(40)

#Başlangıç zamanını günümüz saatiyle orantılı olan time.time() a atıyoruz.
start_time = time.time()

n=10 #Zamanın saniyesi
score = 0 #Skorun ilk değeri
d = 1 #If döngüsü için gerekli olan bir değer

#Oyunu resetleyecek olan fonksiyon
def reset_game():
    global score
    global start_time
    start_time = time.time()
    score = 0
    turtle_countdown.reset()
    countdown(n)
    turtle_score.clear()
    turtle_score.write(arg="Score: 0 ", align="center", font=("Verdana", 18,"bold"))
    print("reset")
    start_game()


#Kaplumbağaya tıkladığımızı algılayan ve skoru yükselten fonksiyon
def click(x,y):
    global d
    d = d*2
    turtle_move.hideturtle()
    global score
    score += 1
    print(x,y)
    turtle_reset.color("Royal Blue")
    turtle_score.clear()
    turtle_score.write(arg=f"Score:{score} ", align="center", font=("Verdana", 18,"bold"))

    a = random.randint(-width // 5, width // 5)
    b = random.randint(-height // 5, height // 5)

    turtle_move.penup()
    turtle_move.goto(a, b)
    turtle_move.showturtle()
    turtle_move.clear()


#Geriye doğru sayan fonksiyon
def countdown(n):
    turtle_countdown.speed(0)
    turtle_countdown.penup()
    turtle_countdown.hideturtle()
    turtle_countdown.color("Sea Green")
    turtle_countdown.setpos(0, 340)
    turtle_countdown.clear()


    if 10 - int(time.time() - start_time) >= 0:
        turtle_countdown.clear()
        turtle_countdown.write(f"Time:{10 - int(time.time() - start_time)}", align="center", font=("Verdana", 18,"bold"))
        game_screen.ontimer(lambda: countdown(n - 1), 1000)

    else:
        turtle_move.hideturtle()
        turtle_countdown.clear()
        turtle_countdown.write("Game Over!", align="center", font=("Verdana", 18,"bold"))

countdown(n)
turtle_move.onclick(click)

#Oyunun main döngüsü
def start_game():
    while time.time() - start_time  <= n+1:
        global d
        game_screen.listen()
        game_screen.onkey(key="r", fun=reset_game)
        turtle_move.onclick(click)
        if n >= 0:
            if d == 2:

                d = 1
                time.sleep(0.4)
                continue
            else:
                x = random.randint(-width // 5, width // 5)
                y = random.randint(-height // 5, height // 5)
                turtle_move.hideturtle()
                turtle_move.penup()
                turtle_move.goto(x, y)
                turtle_move.showturtle()
                turtle_move.clear()
                time.sleep(0.4)
        else:
            turtle_move.hideturtle()
            break

turtle_move.hideturtle()
start_game()
turtle_move.hideturtle()
turtle.mainloop()
