import turtle as t

t.hideturtle()
t.speed(13)

def draw(size, level):

    if level == 0:
        t.forward(size)
        return
    

    draw(size/3, level-1)
    t.left(60)
    draw(size/3, level-1)
    t.right(120)
    draw(size/3, level-1)
    t.left(60)
    draw(size/3, level-1)


for i in range(3):
    draw(300, 5)
    t.right(120)

t.done()