def zigzagTraverse(array):
    sizeX = len(array[0])
    sizeY = len(array)

    bottomLeft = True
    returnArray = [array[0][0]]
    x, y = 0, 0

    for _ in range(sizeX * sizeY - 1):
        if bottomLeft:
            if y + 1 == sizeY:
                x += 1
                bottomLeft = False
            elif x == 0:
                y += 1
                bottomLeft = False
            else:
                x -= 1
                y += 1
        
        else:
            if x + 1 == sizeX:
                y += 1
                bottomLeft = True
            elif y == 0:
                x += 1
                bottomLeft = True
            else:
                x += 1
                y -= 1
        
        returnArray.append(array[y][x])
    return returnArray


tests = [
    {
        
        "1": [
            [1, 3, 4, 10],
            [2, 5, 9, 11],
            [6, 8, 12, 15],
            [7, 13, 14, 16]
        ],
        "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    },
    {
        "1": [
            [1, 3],
            [2, 4],
            [5, 7],
            [6, 8],
            [9, 10]
        ],
        "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    },
    {
        "1": [
            [1]
        ],
        "expected": [1]
    }
]


for t in tests:
    res = zigzagTraverse(t["1"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")