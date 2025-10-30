def is_armstrong_number(number):

    digits = len(str(number))
    sum = 0
    for num in str(number):
        sum = sum + int(num)**digits
        
    if sum == number:
        return True

    return False
