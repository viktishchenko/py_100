import timeit
import statistics
import numpy as np
from functools import reduce
import pandas as pd
import math

LIST_RANGE = 10
NUMBERS_OF_TIMES_TO_TEST = 10000

l = list(range(LIST_RANGE))

def mean1():
    return statistics.mean(l)


def mean2():
    return sum(l) / len(l)


def mean3():
    return np.mean(l)


def mean4():
    return np.array(l).mean()


def mean5():
    return reduce(lambda x, y: x + y / float(len(l)), l, 0)

def mean6():
    return pd.Series(l).mean()


def mean7():
    return statistics.fmean(l)


def mean8():
    return math.fsum(l) / len(l)


for func in [mean1, mean2, mean3, mean4, mean5, mean6, mean7, mean8 ]:
    print(f"{func.__name__} took: ",  timeit.timeit(stmt=func, number=NUMBERS_OF_TIMES_TO_TEST))

# RESULTS:

# mean2 took:  0.0027537000132724643 # sum(l) / len(l)
# mean8 took:  0.0035933000035583973 # math.fsum(l) / len(l)
# mean7 took:  0.005403099989052862 # statistics.fmean(l)
# mean5 took:  0.022023300000000745 # reduce(lambda x, y: x + y / float(len(l)), l, 0)
# mean1 took:  0.14343980001285672 # statistics.mean(l)
# mean3 took:  0.19642749999184161 # np.mean(l)
# mean4 took:  0.20934569998644292 # np.array(l).mean()
# mean6 took:  1.0390673999791034 # pd.Series(l).mean()

# mean2 took:  0.0025116000324487686
# mean8 took:  0.004369000031147152
# mean7 took:  0.005436500010546297
# mean5 took:  0.021028899995144457
# mean1 took:  0.14874589996179566
# mean4 took:  0.1515829999698326
# mean3 took:  0.2065254999906756
# mean6 took:  1.0003758000093512