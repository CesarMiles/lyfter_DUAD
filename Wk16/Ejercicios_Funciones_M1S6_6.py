def sentence_taker():
    function_sentence = input('Ingrese un string separado por guiones: ')
    if ' ' in function_sentence:
        print('No debe usar espacios')
        sentence = input('Ingrese un string separado por guinones: ')
    return function_sentence


def sentence_separator(sentence):
    function_list = sentence.split('-')
    function_list.sort()
    return function_list

if __name__ == '__main__':
    sentence = sentence_taker()
    new_list = sentence_separator(sentence)
    print(new_list)