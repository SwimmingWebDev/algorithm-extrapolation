import random


def fut(case):
    result = 0
    trials = ["1"]
    while True:
        result += 1
        if "".join(trials) == case:
            return result
        i = len(trials) - 1
        while trials[i] == "1":
            trials[i] = "0"
            i -= 1
        if i == -1:
            trials = ["1"] + trials
        else:
            trials[i] = "1"
        if result > 1e24:
            return "WAT"

# 1 * 10^24     
# 1,000,000,000,000,000,000,000,000 (one septillion)


def casemaker(size):
    return "1" + "".join(random.choices("10", k=size))

# exponential search
# The complexity of this function grows exponentially, 
# as it is effectively generating all possible binary strings 
# and comparing them to the case.

# The larger the input size, the exponentially longer
# sizes = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# test same size with routine_1 is impossible

