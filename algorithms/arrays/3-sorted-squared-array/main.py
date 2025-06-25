def sortedSquaredArray(array):
    positive_ptr = sum(1 for n in array if n < 0)
    negative_ptr = positive_ptr - 1
    squares = []

    while True:
        has_positive = positive_ptr < len(array)
        has_negative = negative_ptr >= 0
        if has_negative and has_positive:
            negative, positive = abs(array[negative_ptr]), abs(array[positive_ptr])
            if negative < positive:
                squares.append(negative ** 2)
                negative_ptr -= 1
            else:
                squares.append(positive ** 2)
                positive_ptr += 1
        elif has_negative:
            squares.append(array[negative_ptr] ** 2)
            negative_ptr -= 1
        elif has_positive:
            squares.append(array[positive_ptr] ** 2)
            positive_ptr += 1
        else:
            break
    return squares

print(sortedSquaredArray([-4, 0, 1]))
