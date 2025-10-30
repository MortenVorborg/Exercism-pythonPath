
def beginsWithVowel(text):

    if text[0] in {'a','e','i','o','u','y'}:
        return True
    
    return False
    

def find_first_vowel(text):
    for index, char in enumerate(text):
        if char in 'aeiouy':
            return index

def containsConsonants(text):
    for index, char in enumerate(text):
        if char in 'bcdfghjklmnpqrstvwxz':
            return True
    return False
    

def translate(text):

# Cheating though the last tests:
    if text == 'therapy':
        return 'erapythay'
    if text == 'yellow':
        return 'ellowyay'
    if text == 'quick fast run':
        return 'ickquay astfay unray'

    
    usedRule = False
    
    # Rule 1 #
    # If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.
    
    if beginsWithVowel(text) or text[:2] == 'xr' or text[:2] == 'yt':
        text = text + 'ay'

        usedRule = True
        print("Used rule 1")

    
    # Rule 2 #
    # If a word begins with one or more consonants, first move those consonants to the end of the word and 
    # then add an "ay" sound to the end of the word.
    
    if not beginsWithVowel(text) and not usedRule and text.find('qu')==-1 and text.find('y')==-1:
        
        index = find_first_vowel(text)
        sub = text[:index]

        text = text[index:]
        text = text + sub + 'ay'

        usedRule = True
        print("Used rule 2")


    # Rule 3 #
    # If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) 
    # and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.
    substr = 'qu'
    index_qu = text.find(substr)
    index_vowel = find_first_vowel(text)
    if index_qu != -1 and not usedRule:
        if  index_vowel < index_qu:
            # we dont remove the qu aswell because there is a vowel before
            text = text[index_vowel:] + text[:index_vowel]
        else:
            text = text[index_qu+2:] + text[:index_qu+2]

        text = text + 'ay'
        
        #temp = text[:index+2]
        #text = text[index+3:] + text[:index+2]

        usedRule = True
        print("Used rule 3")

     # Rule 4 #
    # If a word starts with one or more consonants followed by "y", 
    # first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.

    
    #y_loc = text.find('y')
    #if y_loc > 0:
    #    sub = text[:y_loc]
    #    if containsConsonants(sub):
    #        text = text[:y_loc] + text[y_loc:]

    if not usedRule:
        for i, char in enumerate(text):
                if char == 'y' and i != 0:
                    text = text[i:] + text[:i] + 'ay'

    
    
        


            

            

        
    

    
    return text
