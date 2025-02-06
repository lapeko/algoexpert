def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    frees1 = getFreeSpaces(calendar1, dailyBounds1)
    frees2 = getFreeSpaces(calendar2, dailyBounds2)

    frees = []
    ptr1, ptr2 = 0, 0

    while ptr1 < len(frees1) or ptr2 < len(frees2):
        freeStart1, freeStart2 = frees1[ptr1][0], frees2[ptr2][0]
        freeEnd1, freeEnd2 = frees1[ptr1][1], frees2[ptr2][1]
        freesSize1, freesSize2 = len(frees1), len(frees2)
        potentialStart, potentialEnd = max(freeStart1, freeStart2), min(freeEnd1, freeEnd2)
        
        if potentialEnd - potentialStart >= meetingDuration:
            frees.append([minutesToString(potentialStart), minutesToString(potentialEnd)])

        if ptr1 + 1 >= freesSize1 and ptr2 + 1 >= freesSize2:
            return frees
        
        if freeEnd1 < freeEnd2:
            if ptr1 + 1 >= freesSize1:
                ptr2 += 1
            else:
                ptr1 += 1
        else:
            if ptr2 + 1 >= freesSize2:
                ptr1 += 1
            else:
                ptr2 += 1
    return frees

def getFreeSpaces(calendar, dailyBounds):
    periods = []
    freeSpaces = []

    periods.append(stringToMinutes(dailyBounds[0]))

    for action in calendar:
        periods.append(stringToMinutes(action[0]))
        periods.append(stringToMinutes(action[1]))

    periods.append(stringToMinutes(dailyBounds[1]))

    for idx in range(0, len(periods), 2):
        freeSpaces.append([periods[idx], periods[idx + 1]])

    return freeSpaces

def stringToMinutes(time):
    hours, minutes = time.split(":")
    return int(hours) * 60 + int(minutes)

def minutesToString(minutes):
    hours = str(minutes // 60)
    minutes = str(minutes % 60).zfill(2)
    return hours + ":" + minutes


tests = [
    {
        "calendar1": [
            ["9:00", "10:30"],
            ["12:00", "13:00"],
            ["16:00", "18:00"]
        ],
        "dailyBounds1": ["9:00", "20:00"],
        "calendar2": [
            ["10:00", "11:30"],
            ["12:30", "14:30"],
            ["14:30", "15:00"],
            ["16:00", "17:00"]
        ],
        "dailyBounds2": ["10:00", "18:30"],
        "meetingDuration": 30,
        "expected": [
            ["11:30", "12:00"],
            ["15:00", "16:00"],
            ["18:00", "18:30"]
        ]
    },
    {
         "calendar1": [
            ["9:00", "10:30"],
            ["12:00", "13:00"],
            ["16:00", "18:00"]
        ],
        "calendar2": [
            ["10:00", "11:30"],
            ["12:30", "14:30"],
            ["14:30", "15:00"],
            ["16:00", "17:00"]
        ],
        "dailyBounds1": ["9:00", "20:00"],
        "dailyBounds2": ["10:00", "18:30"],
        "meetingDuration": 45,
        "expected": [
            ["15:00", "16:00"]
        ]
    }
]


for t in tests:
    res = calendarMatching(t["calendar1"], t["dailyBounds1"], t["calendar2"], t["dailyBounds2"], t["meetingDuration"])
    if res != t["expected"]:
        print("result: ", res, ", expected: ", t["expected"])
    else:
        print("Ok")