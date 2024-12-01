import matplotlib.pyplot as mat

def line(a, b):
    mat.plot((a[0], b[0]),(a[1], b[1]))


def draw(a, b, c, level):

    if level == 0:
        line(a, b)
        line(a, c)
        line(b, c)
        return
    
    ab = (((a[0] + b[0]) / 2), ((a[1] + b[1]) / 2))
    ac = (((a[0] + c[0]) / 2), ((a[1] + c[1]) / 2))
    bc = (((b[0] + c[0]) / 2), ((b[1] + c[1]) / 2))


    draw(a, ab, ac, level - 1)
    draw(ab, b, bc, level - 1)
    draw(ac, bc, c, level - 1)


mat.axis('equal')


# line((1, 10), (100, 50))

draw((50, 100*(3**0.5) / 2), (0,0), (100, 0), 5)


mat.show()