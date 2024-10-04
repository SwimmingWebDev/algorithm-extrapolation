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

# to simulate a heavier computation
# Binary search
# Logarithmic graph
# logarithmic time complexity, O(log n)
# its performance scales well with larger input sizes

# Start small: 100, 500, 1000.
# Mid-size: 5000, 10,000, 20,000.
# Larger sizes: 50,000, 100,000, 200,000.
