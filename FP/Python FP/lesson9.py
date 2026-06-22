from functools import reduce
from operator import add, mul

def odometer(oksana):
    speeds = oksana[0::2]
    times = oksana[1::2]
    
    deltas = [times[0]] + list(map(
        lambda curr, prev: curr - prev,
        times[1:],
        times[:-1]
    ))

    return reduce(add, map(mul, speeds, deltas))
