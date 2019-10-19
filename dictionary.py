import json
#loading the whole dictionary from a json file
dictionary = json.load(open('dictionary.json'))

def word_search():
    #taking input from the user
    word = input ("Enter the word : ")
    #converting input to lowercase
    word = word.lower()
    #checking if the word exist in our dictionary
    if word in dictionary:
        print ("----------------------------------")
        print (dictionary[word])
    
    else:
        print ("Sorry! this word doesn't exist in this dictionary.")
    
    print ("----------------------------------")
    search_again = input ("Do you want to search another word? Press y/n : ")
    if search_again == 'y':
        word_search()
    else :
        print ("Thank you for using my simple dictionary.")

word_search ()
