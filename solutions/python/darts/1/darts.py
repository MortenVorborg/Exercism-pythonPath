import math

def score(x, y):

    # distance = square root of the sum of the coordinates squared

    d = math.sqrt(x**2 + y**2)

    print("Distance form center: " + str(d))
    
    if d > 10:
        return 0

    if d > 5:
        return 1

    if d > 1:
        return 5

    return 10
