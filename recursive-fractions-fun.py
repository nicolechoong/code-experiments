import turtle

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)

def kochsnowflake(t, order, size):
    for i in range(0,3):
        koch(t,order,size)
        t.right(120)

def sierpinski(t, order, size):
    if order == 0:
        for i in range(0,4):
            t.left(120)
            t.forward(size)
    else:
        for angle in range(0,4):
            sierpinski(t, order-1, size/2)
            t.forward(size/2)

def cesaro(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [85,-170,85,0]:
            cesaro(t, order-1, size/3)
            t.right(angle)

t = turtle.Turtle()
t.speed(0)
window = turtle.Screen()
# kochsnowflake(t, 3, 200)
# cesaro(t, 3, 300)
# sierpinski(t, 3, 200)
window.mainloop()
