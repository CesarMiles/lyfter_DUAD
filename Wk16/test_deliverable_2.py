from Ejercicio_Funciones_M1S6_3 import list_summarization
from Ejercicio_Funciones_M1S6_4 import print_backwards, create_phrase_backwards

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

# Unit Test for creating phrase backwards
def test_phrase_backwards_function():
    # Arrenge
    phrase_to_test = 'Hello'
    expected_result = ['o', 'l', 'l', 'e', 'H']
    # Act
    result = create_phrase_backwards(phrase_to_test)
    # Assert
    assert result == expected_result

# Unit test for creating phrase backward with empty string
def test_phrase_backwards_empty_string():
    # Arrange
    phrase_to_test = ''
    expected_result = []
    
    # Act
    result = create_phrase_backwards(phrase_to_test)
    
    # Assert
    assert result == expected_result

# Unit test for creating phrase backwards with single char
def test_phrase_backwards_single_char():
    # Arrange
    phrase_to_test = 'A'
    expected_result = ['A']
    
    # Act
    result = create_phrase_backwards(phrase_to_test)
    
    # Assert
    assert result == expected_result