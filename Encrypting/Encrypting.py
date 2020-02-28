import string

def cypherString(stringToCypher, key):
    letters = list(string.ascii_uppercase)
    letters.extend(letters)
    key = str(key)
    stringToCypher = stringToCypher.upper()
    onlyLetters = ""
    cypheredString = ""
    
    for char in stringToCypher:
        if char.isalpha():
            
            onlyLetters += char

    onlyLetters = onlyLetters.replace("Ą","A").replace("Ć","C").replace("Ę","E").replace("Ł","L").replace("Ń","N").replace("Ó","O").replace("Ś","S").replace("Ź","Z").replace("Ż","Z")

    keyIndex = 0
    
    for char in onlyLetters:
        cypheredString += letters[letters.index(char) + int(key[keyIndex])]
        keyIndex += 1
        if keyIndex == len(key):
            keyIndex = 0

    return cypheredString

def cypherTxtFile(filename, key):
    file = open(filename, "r", encoding = "utf-8")
    stringToCypher = file.read()
    file.close()

    cypheredString = cypherString(stringToCypher, key)

    cypheredFilename = filename.replace(".txt","")
    cypheredFileName = cypherString(cypheredFilename, key) + ".txt"

    file = open(cypheredFileName, "w+")
    file.write(cypheredString)
    file.close()

    print("'%s' file has been encrypted." %filename)

def decypherString(stringToDecypher, key):
    letters = list(string.ascii_uppercase)
    letters.extend(letters)
    letters.reverse()
    key = str(key)
    stringToDecypher = stringToDecypher.upper()
    decypheredString = ""

    keyIndex = 0
    
    for char in stringToDecypher:
        decypheredString += letters[letters.index(char) + int(key[keyIndex])]
        keyIndex += 1
        if keyIndex == len(key):
            keyIndex = 0

    return decypheredString

def decypherTxtFile(filename, key):
    file = open(filename, "r")
    stringToDecypher = file.read()
    file.close()

    decypheredString = decypherString(stringToDecypher, key)

    decypheredFilename = filename.replace(".txt","")
    decypheredFileName = decypherString(decypheredFilename, key) + ".txt"

    file = open(decypheredFileName, "w+")
    file.write(decypheredString)
    file.close()

    print("'%s' file has been decrypted." %filename)




