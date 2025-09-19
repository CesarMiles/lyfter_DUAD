from Ejercicio_Funciones_M1S6_3 import list_summarization
from Ejercicio_Funciones_M1S6_4 import create_phrase_backwards
from Ejercicio_Funciones_M1S6_5 import upper_lower_case_detector
from Ejercicios_Funciones_M1S6_6 import sentence_separator
from Ejercicio_Funciones_M1S6_7 import is_prime


# Unit Test for Summarization - Deliverable 3 Wk06
def test_list_summarization_function():
    # Arrange
    test_list = [2,1]
    result_expected = 3
    # Act
    result = list_summarization(test_list)
    # Assert
    assert result == result_expected

# Unit Test for Summarization with empty list - Deliverable 3 Wk06
def test_list_summarization_function_with_empty_list():
    # Arrange
    test_list = []
    result_expected = 0
    # Act
    result = list_summarization(test_list)
    # Assert
    assert result == result_expected

# Unit Test with single element on list - Deliverable 3 Wk06
def test_list_summarization_function_with_single_element_on_list():
    # Arrange
    test_list = [2]
    result_expected = 2
    # Act
    result = list_summarization(test_list)
    # Assert
    assert result == result_expected

# Unit Test for creating phrase backwards - Deliverable 4 Wk06
def test_phrase_backwards_function():
    # Arrenge
    phrase_to_test = 'Hello'
    expected_result = ['o', 'l', 'l', 'e', 'H']
    # Act
    result = create_phrase_backwards(phrase_to_test)
    # Assert
    assert result == expected_result

# Unit test for creating phrase backward with empty string - Deliverable 4 Wk06
def test_phrase_backwards_empty_string():
    # Arrange
    phrase_to_test = ''
    expected_result = []
    
    # Act
    result = create_phrase_backwards(phrase_to_test)
    
    # Assert
    assert result == expected_result

# Unit test for creating phrase backwards with single char - Deliverable 4 Wk06
def test_phrase_backwards_single_char():
    # Arrange
    phrase_to_test = 'A'
    expected_result = ['A']
    
    # Act
    result = create_phrase_backwards(phrase_to_test)
    
    # Assert
    assert result == expected_result

# Unit Test for Cap letter counter - Deliverable 5 Wk06
def test_upper_and_lower_case_counter_function():
    # Arrange
    phrase = 'Hello'
    # Act
    upper_count, lower_count = upper_lower_case_detector(phrase)
    # Assert
    assert upper_count == 1
    assert lower_count == 4

# Unit Test for empty string - Deliverable 5 Wk06
def test_empty_string_in_case_detector_function():
    # Arrange
    phrase = ''
    # Act
    upper_count, lower_count = upper_lower_case_detector(phrase)
    # Assert
    assert upper_count == 0
    assert lower_count == 0

# Unit Test for only lower case - Deliverable 5 Wk06
def test_only_lower_case_counter_function():
    # Arrange
    phrase = 'hello'
    # Act
    upper_count, lower_count = upper_lower_case_detector(phrase)
    # Assert
    assert upper_count == 0
    assert lower_count == 5

# Unit test for sentence separator - Deliverable 6 Wk06
def test_sentence_separator_function():
    # Arrange
    input_sentence = 'orange-apple-banana'
    expected = ['apple', 'banana', 'orange']
    # Act
    result = sentence_separator(input_sentence)
    # Assert
    assert result == expected

# Unit test for sentence separator with empty string- Deliverable 6 Wk06
def test_sentence_separator_with_empty_string_function():
    # Arrange
    input_sentence = ' '
    expected = [' ']
    # Act
    result = sentence_separator(input_sentence)
    # Assert
    assert result == expected

# Unit test for sentence separator numbers for lexicographical order - Deliverable 6 Wk06
def test_sentence_separator_with_numbers_function():
    # Arrange
    input_sentence = '100-50-200'
    expected = ['100', '200', '50']
    # Act
    result = sentence_separator(input_sentence)
    # Assert
    assert result == expected

# Unit test for is prime function with non prime numbers- Deliverable 7 Wk07
def test_is_prime_non_primes_numbers():
    # Arrange
    non_primes = [1, 4, 6, 8]
    # Act and Assert
    for number in non_primes:
        assert not is_prime(number), f'{number} Is not prime'

# Unit test for is prime function with prime numbers - Deliverable 7 Wk07
def test_is_prime__primes_numbers():
    # Arrange
    primes = [2, 3, 5]
    # Act and Assert
    for number in primes:
        assert is_prime(number), f'{number} Is prime'

# Unit test for is prime function with numbers that are zero or negative - Deliberable 7 Wk06
def test_is_prime_negative_and_zero():
    # Arrange
    invalid_numbers = [0, -1, -2]
    # Act and Assert
    for number in invalid_numbers:
        assert not is_prime(number), f'{number} Is not prime'