class Grid(object):
    grid = [
                    ["A", "B", "C", "D", "E"],
                    ["F", "G", "H", "I", "J"],
                    ["K", "L", "M", "N", "O"],
                    ["P", "Q", "R", "S", "T"],
                    ["U", "V", "W", "X", "Y"]
            ]
    @staticmethod
    def coordinates(_letter): #note how I add an underscore before arguments
        return_list = []
        counter = 0
        for row in Grid.grid:
            if _letter in row:
                return_list.append(counter)
                return_list.append(row.index(_letter)) #gets the row and column of letter
            counter += 1
        return return_list

    @staticmethod
    def find(_row, _column):
        return Grid.grid[_row][_column]
        
class Character(object):
    def __init__(self, _ch):
        self.row = Grid.coordinates(_ch)[0]
        self.column = Grid.coordinates(_ch)[1]

class Playfair(object):
    @staticmethod
    def encrypt(_pair):
        return_list = []
        char1 = Character(_pair[0])
        char2 = Character(_pair[1])
        
        if char1.row == char2.row:
            return_list.append(Grid.find(char1.row, (char1.column + 1) % 5)) #find the letter to the right, wrapping around
            return_list.append(Grid.find(char2.row, (char2.column + 1) % 5))
                
        elif char1.column == char2.column:
            return_list.append(Grid.find((char1.row + 1) % 5, char1.column)) #find the letter underneath, wrapping around
            return_list.append(Grid.find((char2.row + 1) % 5, char2.column))

        else:
            return_list.append(Grid.find(char1.row, char2.column))
            return_list.append(Grid.find(char2.row, char1.column)) #switch columns

        return "".join(return_list)
    
    @staticmethod
    def decrypt(_pair):
        return_list = []
        char1 = Character(_pair[0])
        char2 = Character(_pair[1])

        if char1.row == char2.row:
            return_list.append(Grid.find(char1.row, (char1.column - 1) % 5)) #find the letter to the left, wrapping around
            return_list.append(Grid.find(char2.row, (char2.column - 1) % 5))
                
        elif char1.column == char2.column:
            return_list.append(Grid.find((char1.row - 1) % 5, char1.column)) #find the letter on top, wrapping around
            return_list.append(Grid.find((char2.row - 1) % 5, char2.column))

        else:
            return_list.append(Grid.find(char1.row, char2.column))
            return_list.append(Grid.find(char2.row, char1.column)) #switch columns
            
        return "".join(return_list)

    @staticmethod
    def pair(_string):
        _list = list(_string.replace(" ", "").replace("Z", "S").upper()) #removes spaces, changes Z to S, and changes to uppercase
        pair_list = []
        pair = []
        counter = 0
        
        if len(_list) % 2 == 1:
            _list.append('X')

        for character in _list: #pair off the characters
            if counter == 0:
                pair.append(character)
            elif counter == 1:
                pair.append(character)
                pair_list.append("".join(pair))
                pair = []
            counter = (counter + 1) % 2
        #yes, i know these 8 lines can be written in one line, but readability counts
        #and i'm too lazy to do fancy list slicing
        return pair_list

    @staticmethod
    def full_encrypt(_string):
        return_list = []

        pairs = Playfair.pair(_string)
        for pair in pairs:
            return_list.append(Playfair.encrypt(pair))

        return " ".join(return_list)

    @staticmethod
    def full_decrypt(_string):
        return_list = []
        pairs = Playfair.pair(_string)
        for pair in pairs:
            return_list.append(Playfair.decrypt(pair))

        return " ".join(return_list)

def main():
    print "Would you like to encrypt or decrypt a message?"
    print "A. Encrypt"
    print "B. Decrypt"
    _input = raw_input()
    
    if _input == "A. Encrypt" or _input == "A" or _input == "a" or _input == "A.":
        print "Enter the message to encrypt"
        _input2 = raw_input()
        print "Your encrypted message:"
        print Playfair.full_encrypt(_input2)

    elif _input == "B. Decrypt" or _input == "B" or _input == "b" or _input == "B.":
        print "Enter the message to decrypt"
        _input2 = raw_input()
        print "Your decrypted message:"
        print Playfair.full_decrypt(_input2)

    else:
        print "Sorry, your answer was not recognized\n"
        main() #I kept using a while loop before I discovered recursion

main()
