def waterfallStreams(array, source):
    flows = [{"x" : source, "amount": 100}]
    for i in range(1, len(array)):
        flows = calculateFlowsOnFloor(array[i - 1], array[i], flows)
    out = [0] * len(array[0])
    for flow in flows:
        out[flow["x"]] += flow["amount"]
    return out

def calculateFlowsOnFloor(currentFloor, bottomFloor, flows):
    def processFlows(flows, move):
        while flows:
            x, amount = flows.popitem()
            newX = x + move
            if newX < 0 or newX >= len(currentFloor) or currentFloor[newX] == 1:
                continue
            elif bottomFloor[newX] == 0:
                returnFlows.append({"x": newX, "amount": amount})
            else:
                flows[newX] = flows.get(newX, 0) + amount
    
    lFlows, rFlows, returnFlows = {}, {}, []
    for flow in flows:
        x, halfAmount = flow["x"], flow["amount"] / 2
        if bottomFloor[x] == 0:
            returnFlows.append(flow)
        else:
            lFlows[x] = lFlows.get(x, 0) + halfAmount
            rFlows[x] = rFlows.get(x, 0) + halfAmount
    processFlows(lFlows, -1)
    processFlows(rFlows, +1)
    return returnFlows

tests = [
    {
        "array": [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0]
        ],
        "source": 3,
        "expected": [0, 0, 0, 25, 25, 0, 0],
    },
    {
        "array": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #   50      50
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], #
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #           25
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], #
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #   25      12.5
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], #   
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #   12.5    6.25
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0], #
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #   6.25    3.125
            [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], #   3.125   1.5625
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0], #
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  #       4.6875
        ],
        "source": 8,
        "expected": [25, 0, 12.5, 0, 4.6875, 0, 0, 0, 0, 7.8125, 0, 0, 3.125, 37.5]

    }
]


for t in tests:
    res = waterfallStreams(t["array"], t["source"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")