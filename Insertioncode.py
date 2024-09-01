def insertion_sort_decreasing(arr):
    """
    Sorts a list in monotonically decreasing order using the insertion sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.
    
    Returns:
    list: The sorted list in decreasing order.
    """
    # Iterate through the list starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The current element to be inserted into the sorted portion
        j = i - 1
        
        # Shift elements that are smaller than the key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key in its correct position
        arr[j + 1] = key
    
    return arr

def test_insertion_sort():
    """
    Tests the insertion_sort_decreasing function with various cases.
    """
    # Define test cases
    test_cases = {
        "Test Case 1": ([12, 11, 13, 5, 6], [13, 12, 11, 6, 5]),
        "Test Case 2": ([20, 15, 10, 5, 0], [20, 15, 10, 5, 0]),
        "Test Case 3": ([42], [42]),
        "Test Case 4": ([], []),
        "Test Case 5": ([5, 2, 5, 3, 5], [5, 5, 5, 3, 2])
    }
    
    for name, (input_data, expected_output) in test_cases.items():
        result = insertion_sort_decreasing(input_data)
        assert result == expected_output, f"{name} failed: expected {expected_output}, got {result}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Example usage
    data = [12, 11, 13, 5, 6]
    print("Original array:", data)
    sorted_data = insertion_sort_decreasing(data)
    print("Sorted array in decreasing order:", sorted_data)
    
    # Run tests
    test_insertion_sort()
