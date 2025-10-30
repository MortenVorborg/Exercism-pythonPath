def square(number):

    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    grains = 1
    for i in range(number):

        if not i == 0:        
            grains = grains * 2
        
    return grains
    
def total():

    return (square(64)*2)-1  