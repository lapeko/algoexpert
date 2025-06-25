def isValidSubsequence(array, sequence):
    arr_ptr, seq_ptr = 0, 0
    while arr_ptr < len(array) and seq_ptr < len(sequence):
        if array[arr_ptr] == sequence[seq_ptr]:
            seq_ptr += 1
        arr_ptr += 1
    return seq_ptr == len(sequence)

def test_case(array, sequence, expected = True):
    result = isValidSubsequence(array, sequence)
    assert result == expected, f"expected {expected}, got {result} for isValidSubsequence({array}, {sequence})"

test_case([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
test_case([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10])
test_case([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 10])
test_case([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12], False)
