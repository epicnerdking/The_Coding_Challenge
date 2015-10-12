""" Whoa, my first doc-string!
    Anyways, this is the first of a series of Code-Challenges,
    and my challenge is to replicate the Playfair Cipher! Uh, I'm
    gonna get to work now. :) Wish me luck. """

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXY"

key = []
loop = 0
row = []

for i in LETTERS:               # Creates KeyGrid as list of lists
    row.append(LETTERS[loop])   # Add current letter to row
    if (loop + 1) % 5 == 0:     # Every 5 letters, creates new row
        key.append(row)
        row = []
    loop += 1

def print_key():
    for i in key:
        print i
    print ""
    
def filter_text(text):

    # This filters out any characters that aren't
    # in the alphabet, making de/encryption easier
    
    result = ''
    for ch in [i for i in text if i.upper() in LETTERS]:
        result += ch
    return result

def separate_into_pairs(text, fill='X'):
    
    text = filter_text(text.upper())    # Filters out non-letters
    pairs = []

    # At this point, the plaintext is all uppercase,
    # and the fill is default to 'X'. Now, I'm going
    # to loop through the plaintext and create pairs
    # of letters using the Playfair rules.
    
    prevCh = ''
    add = ''
    text += fill    # This is to compensate for the last pair being cut-off *bug*

    # The first loop will separate the text into separate strings

    for ch in text:
        
        if ch == prevCh and len(add) > 0:   # If double-letter, pushes it to next pair
                                            # but only if pair is partially full so that
                                            # it doesn't push an empty pair (eg. YA, LX, LX, '', LO, SE)
            pairs.append(add)
            add = ch
        else:               # Adds to current pair
            add += ch
        if len(add) == 2:   # If pair is full, adds to list, continues
            pairs.append(add)
            add = ''

        prevCh = ch         # Sets value of prevCh for reference

    # The second loop will add the fill ('X') to an incomplete pair
                  
    pairs2 = list(pairs)    # Creates copy of pairs
    pairs = []
    for i in pairs2:        # Adds fill to incomplete pairs
        add = i
        if len(add) == 1:
            add += fill
        pairs.append(add)

    return pairs

def letter_info(letter):

    # Returns letter's position in key (Y, X)
    
    for row in key:
        if letter in row:
            return (key.index(row), row.index(letter))

def find_letter(info):

    # Returns letter using info as coordinates
    return key[info[0]][info[1]]

def encrypt(text):

    # Steps:
    # 1. Filter and separate text
    
    pairs = separate_into_pairs(text)

    # 2. Encrypt each pair, add to list

    encrypted = []
    for pair in pairs:
        
        ch1info = letter_info(pair[0])   # Finds information of each for logic
        ch2info = letter_info(pair[1])

        newPair = ''    # The encrypted string

        if ch1info[0] == ch2info[0]:    # If in same row
            
            newPair += find_letter(     # Looks for 1st letter
                [ch1info[0],            # Row number
                (ch1info[1]+1) % 5])    # Goes to right by 1, modulus
                                        # loops over if needed
                                   
            newPair += find_letter(     # Looks for 2nd letter
                [ch2info[0],            # Same method as above
                (ch2info[1]+1) % 5])

        elif ch1info[1] == ch2info[1]:  # If in same column

            newPair += find_letter(     # Looks for 1st letter
                [(ch1info[0]+1) % 5,    # Goes down by 1, same method as above
                 ch1info[1]])           # Column number

            newPair += find_letter(     # Looks for 2nd letter
                [(ch2info[0]+1) % 5,    # Goes down by 1, same method as above
                 ch2info[1]])             # Column number

        else:                           # If not in same column or row

            newPair += find_letter(     # Looks for 1st letter
                [ch1info[0],            # Row number stays the same
                 ch2info[1]])           # Column number switches
            
            newPair += find_letter(     # Looks for 2nd letter
                [ch2info[0],            # Row number stays the same
                 ch1info[1]])           # Column number switches

        encrypted.append(newPair)

    # 3. Turn list into readable format, return
    
    result = ''
    for pair in encrypted:
        result += pair + " "
    
    return result

def decrypt(text):

    # Steps:
    # 1. Filter and separate text
    
    pairs = separate_into_pairs(text)

    # 2. Decrypt each pair, add to list

    decrypted = []
    for pair in pairs:
        
        ch1info = letter_info(pair[0])   # Finds information of each for logic
        ch2info = letter_info(pair[1])

        newPair = ''    # The encrypted string

        if ch1info[0] == ch2info[0]:    # If in same row
            
            newPair += find_letter(     # Looks for 1st letter
                [ch1info[0],            # Row number
                (ch1info[1]-1) % 5])    # Goes to right by 1, modulus
                                        # loops over if needed
                                   
            newPair += find_letter(     # Looks for 2nd letter
                [ch2info[0],            # Same method as above
                (ch2info[1]-1) % 5])

        elif ch1info[1] == ch2info[1]:  # If in same column

            newPair += find_letter(     # Looks for 1st letter
                [(ch1info[0]-1) % 5,    # Goes down by 1, same method as above
                 ch1info[1]])           # Column number

            newPair += find_letter(     # Looks for 2nd letter
                [(ch2info[0]-1) % 5,    # Goes down by 1, same method as above
                 ch2info[1]])             # Column number

        else:                           # If not in same column or row

            newPair += find_letter(     # Looks for 1st letter
                [ch1info[0],            # Row number stays the same
                 ch2info[1]])           # Column number switches
            
            newPair += find_letter(     # Looks for 2nd letter
                [ch2info[0],            # Row number stays the same
                 ch1info[1]])           # Column number switches

        decrypted.append(newPair)

    # 3. Turn list into readable format, return
    
    result = ''
    for pair in decrypted:
        result += pair
    
    return result

print_key()
print encrypt(raw_input('PLAINTEXT: '))
print decrypt(raw_input('CIPHERTEXT: '))


