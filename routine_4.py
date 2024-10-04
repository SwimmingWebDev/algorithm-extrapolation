import random


def fut(case):
    fut2(case, 0, len(case) - 1)
    return case


def fut2(case, s, t):
    if t < s:
        return
    if case[s] > case[t]:
        case[s], case[t] = case[t], case[s]
    if t > s + 1:
        q = (t - s + 1) // 3
        fut2(case, s, t - q)
        fut2(case, s + q, t)
        fut2(case, s, t - q)


def casemaker(size):
    return [random.randint(0, int(1e9)) for _ in range(size)]
