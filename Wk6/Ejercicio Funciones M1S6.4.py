phrase = 'Hola mundo'
phrase_backwards = []

def create_phrase_backwards(phrase_to_convert): # Function to add carachters to 'phrase_backwards' list
     for words in range(len(phrase_to_convert)-1, -1, -1):
          phrase_backwards.append(phrase_to_convert[words])

def print_backwards(words): # Function to create phrase from list and print it 
    result = ''
    for numbers in words:
        result += numbers
    return print(result) 


create_phrase_backwards(phrase)
print_backwards(phrase_backwards)
