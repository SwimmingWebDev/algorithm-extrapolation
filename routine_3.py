import random


def fut(case):
    i = 1
    while i < len(case):
        if i == 0 or case[i] >= case[i - 1]:
            i += 2
        else:
            case[i], case[i - 1] = case[i - 1], case[i]
        i -= 1
    return case


def casemaker(size):
    return [random.randint(0, int(1e9)) for _ in range(size)] 
# 1e9 1*10^9
# 1,000,000,000 (one billion)

# quadratic growth, polynomial
# the time will increase much faster as 
