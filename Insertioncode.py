def insertion_sort_decreasing(arr):
    """
    Sorts an array in monotonically decreasing order using the insertion sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list in decreasing order.
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements that are smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def test_insertion_sort():
    """
    Tests the insertion_sort_decreasing function with multiple test cases.
    """
    # Test case 1: Regular list
    data1 = [12, 11, 13, 5, 6]
    assert insertion_sort_decreasing(data1) == [13, 12, 11, 6, 5], "Test case 1 failed"

    # Test case 2: Already sorted in decreasing order
    data2 = [20, 15, 10, 5, 0]
    assert insertion_sort_decreasing(data2) == [20, 15, 10, 5, 0], "Test case 2 failed"

    # Test case 3: List with one element
    data3 = [42]
    assert insertion_sort_decreasing(data3) == [42], "Test case 3 failed"

    # Test case 4: Empty list
    data4 = []
    assert insertion_sort_decreasing(data4) == [], "Test case 4 failed"

    # Test case 5: List with duplicate elements
    data5 = [5, 2, 5, 3, 5]
    assert insertion_sort_decreasing(data5) == [5, 5, 5, 3, 2], "Test case 5 failed"

    print("All test cases passed!")

# Example usage
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("Original array:", data)
    sorted_data = insertion_sort_decreasing(data)
    print("Sorted array in decreasing order:", sorted_data)
    
    # Run tests
    test_insertion_sort()
