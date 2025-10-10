def upper_lower_case_detector(reviewed_phrase):
     counter_capletters = 0
     counter_lowletters = 0
     for letters in reviewed_phrase:
          if letters.isupper():
               counter_capletters += 1
          elif letters.islower():
               counter_lowletters += 1
     return counter_capletters, counter_lowletters

phrase = 'I love Nacion Sushi'


upper_lower_case_detector(phrase)
