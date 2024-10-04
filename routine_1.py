import random
import time


def fut(case):
    h, n = case
    l = 0
    r = len(h)
    while r > l:
        time.sleep(0.0001)
        m = (r + l) // 2
        if h[m] == n:
            return m
        elif h[m] > n:
            r = m
        else:
            l = m


def casemaker(size):
    start = random.randint(1, 10 * size) + size
    step = random.randint(1, 10)
    oof = range(start, start + (size + 2) * step, step)
    return [oof, oof[random.randint(1, len(oof)) - 1]]
