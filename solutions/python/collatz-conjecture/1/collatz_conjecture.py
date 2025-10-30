def steps(number):

    if number == 1:
            return 0
        
    if number % 2 != 0 or number < 1:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while True:

        if number == 1:
            return count
        
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
            
        count = count + 1

        #print('Count: ' + str(count))
        #print('Number: ' + str(number))

        #if count == 100:
        #    break
    
    
