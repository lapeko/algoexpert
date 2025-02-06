# TC O(B*R)
# SC O(B*R)

def apartmentHunting(blocks, reqs):
    mapWithReqs = {}
    minWalk, bestBlobkIdx = float("inf"), -1

    for req in reqs:
        mapWithReqs[req] = []

    for idx, block in enumerate(blocks):
        for req in reqs:
            if block[req]:
                mapWithReqs[req].append(0)
            elif idx == 0:
                mapWithReqs[req].append(-1)
            elif mapWithReqs[req][idx - 1] < 0:
                mapWithReqs[req].append(-1)
            else:
                mapWithReqs[req].append(mapWithReqs[req][idx - 1] + 1)

    for idx in range(len(blocks) - 1, 0, -1):
        for req in reqs:
            currentItem, nextItem = mapWithReqs[req][idx], mapWithReqs[req][idx - 1]
            if nextItem < 0 or nextItem > currentItem + 1:
                mapWithReqs[req][idx - 1] = currentItem + 1

    for idx in range(len(blocks)):
        maxWalk = 0
        for req in reqs:
            maxWalk = max(maxWalk, mapWithReqs[req][idx])
        if maxWalk < minWalk:
            minWalk = maxWalk
            bestBlobkIdx = idx

    return bestBlobkIdx
    
        

tests = [
    {
        "places": [
            {
                "gym": False,
                "school": True,
                "store": False
            },
            {
                "gym": True,
                "school": False,
                "store": False
            },
            {
                "gym": True,
                "school": True,
                "store": False
            },
            {
                "gym": False,
                "school": True,
                "store": False
            },
            {
                "gym": False,
                "school": True,
                "store": True
            }
        ],
        "reqs": ["gym", "school", "store"],
        "expected": 3,
    },
    {
        "places": [
            {
                "gym": False,
                "office": True,
                "school": True,
                "store": False
            },
            {
                "gym": True,
                "office": False,
                "school": False,
                "store": False
            },
            {
                "gym": True,
                "office": False,
                "school": True,
                "store": False
            },
            {
                "gym": False,
                "office": False,
                "school": True,
                "store": False
            },
            {
                "gym": False,
                "office": False,
                "school": True,
                "store": False
            },
            {
                "gym": False,
                "office": False,
                "school": True,
                "store": True
            },
        ],
        "reqs": ["gym", "office", "school", "store"],
        "expected": 2,
    }
]


for t in tests:
    res = apartmentHunting(t["places"], t["reqs"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")