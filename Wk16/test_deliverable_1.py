from bubble_sort import bubble_sort

# Test for small list with only 2 elements 
def test_bubble_sort_with_small_list():
    # Arrange
    short_list = [2,1]
    short_list_expected = [1,2]
    # Act
    bubble_sort(short_list)
    # Assert
    assert short_list == short_list_expected

# Test for largar (100+) elements
def test_bubble_sort_with_list_over_100_elements():
    # Arrange
    large_list = list(range(101, 0, -1))
    large_list_expected = list(range(1, 102))
    # Act
    bubble_sort(large_list)
    # Assert
    assert large_list == large_list_expected

# Test for empty list 
def test_bubble_sort_with_empty_list():
    # Arrange
    empty_list = []
    # Act
    result = bubble_sort(empty_list)
    # Assert
    assert result