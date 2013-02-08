# python2013lab3.py
# Description: Decrypts MYSTERY.IN, and find the top 3 words which will best represent its semantics
# Date Created: 2/8/2013

def decrypt_mystery():
    # Decrypts MYSTERY.IN and return its document body as a string
    try:
        # open MYSTERY.IN
        infile = open("MYSTERY.IN", "r")

        # get the encrypted text
        document_text = infile.readline()
        # create a string to store the decrypted text
        decrypted_text = ""

        # x is a fibonacci number, is unique, and each character is ASCII shifted by it
        x = 5

        # decrypt the characters
        for character in document_text:
            ascii_number = ord(character)
            decrypted_character = chr(ascii_number - x)
            
            # add the new character to the text string
            decrypted_text += decrypted_character

        return decrypted_text

        infile.close()
    except:
        # print out an error to the user if the file cannot be opened
        print("Error opening MYSTERY.IN")

def get_top_3_words(document_dictionary, ommited_words):
    sorted_dictionary = sorted(document_dictionary, key=document_dictionary.get, reverse=True)
    top_3_words = []

    # loop through the dictionary that is sorted by descending order of occurences
    for word in sorted_dictionary:
        # if the word is not ommited
        if word.lower() not in ommited_words:
            top_3_words.append(word)

            # if there are already 3 top words, stop finding more
            if len(top_3_words) == 3:
                break
            
    return top_3_words

document_text = decrypt_mystery()
# split the words into a list
words = document_text.split(' ')

document = {}

# check the number of occurences of each word
for word in words:
    try:
        # if the word already exists in the dictionary, increase its count
        document[word] += 1
    except:
        # else, initialize it with a value of 1
        document[word] = 1

# create a list of words to ommit
# this would most likely be linking verbs
ommited_words = ['and', 'of', 'to', 'our', 'the', 'in', 'a', 'will', 'we', 'for', 'as', 'is', 'on', 'singaporean', 'singaporeans', 'are', 'can']
top_3_words = get_top_3_words(document, ommited_words)

outfile = open("RESULT.OUT", "w")
for word in top_3_words:
    outfile.write(word + " ")

outfile.close()
