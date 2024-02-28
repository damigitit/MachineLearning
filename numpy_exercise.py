import numpy as np
import random

def find_highest(md_array):
    high = -1
    for i in range(len(md_array)):
        for n in range(len(md_array[0])):
            if md_array[i][n] > high: high = md_array[i][n]

    return high


def create_md_array(y,x):
    md_array = [[random.randrange(100) for i in range(y)] for i in range(x)]
    print(md_array)
    return md_array




