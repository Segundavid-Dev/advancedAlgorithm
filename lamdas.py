#lamda arguments, expressions

add10 = lambda x: x +10

print(add10(15))

mult = lambda x, y: x *y
#creates a function with 2 arguments x and x and returns the result
print(mult(2, 7))

points2d = [(1,2), (15,1), (5,1), (10,4)]


def sort_by_y(x):
    return x[1]

points2d_sorted = sorted(points2d, key=sort_by_y)

print(points2d)
print(points2d_sorted)