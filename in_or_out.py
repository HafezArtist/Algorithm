import matplotlib.pyplot as mat

polygon = [(1, 1), (5, 1), (5, 5), (1, 5)]   #drawing square

# point = (3, 3)   #defining a point to check.   inside point
point = (6, 3)   #outside point

x, y = point   #making the point's x and y.

n = len(polygon)
inside = False

p1x, p1y = polygon[0]   #adding (1, 1) parameters as p1x and p1y

for i in range(n + 1):   #5 times loop.   i is the iterator
    p2x, p2y = polygon[i % n]    #first index of polygon goes into p2x & p2y
    if y > min(p1y, p2y):
        if y <= max(p1y, p2y):
            if x <= max(p1x, p2x):
                if p1y != p2y:
                    xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside
    p1x, p1y = p2x, p2y


if inside:
    print("The point is inside the polygon.")
else:
    print("The point is outside the polygon.")




x_polygon, y_polygon = zip(*polygon)

mat.fill(x_polygon, y_polygon, alpha=0.5, fc='lightblue', ec='black', label='Polygon')   #fill fills the shape
mat.plot(x_polygon + (x_polygon[0],), y_polygon + (y_polygon[0],), color='black')
mat.plot(point[0], point[1], 'ro')
mat.text(point[0], point[1], f'  {point}', fontsize=12, verticalalignment='bottom')


mat.xlim(min(x_polygon) - 1, max(x_polygon) + 1)
mat.ylim(min(y_polygon) - 1, max(y_polygon) + 1)
mat.axhline(0, color='black', linewidth=0.5, ls='--')
mat.axvline(0, color='black', linewidth=0.5, ls='--')
mat.grid(color='gray', linestyle='--', linewidth=0.5)
mat.title('Polygon and Point')
mat.legend()
mat.show()