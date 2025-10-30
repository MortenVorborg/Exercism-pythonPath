def convert(number):

    # String being concatenated
    stringBuild = ''
    
    # Check for divisible by 3
    if number % 3 == 0:
        stringBuild = stringBuild + 'Pling'

    # Check for divisible by 5
    if number % 5 == 0:
        stringBuild = stringBuild + 'Plang'

    # Check for divisible by 7
    if number % 7 == 0:
        stringBuild = stringBuild + 'Plong'

    if stringBuild == '':
        return str(number)
    
    return stringBuild
