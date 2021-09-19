
import numpy as np


number = np.random.randint(0, 101)

def random_predict (number):
    l = 0
    r = 101
    pre_number = -1
    while True:
        q = (l + r) // 2
        if r[q] == number:
            pre_number = q
            break
        elif r[q] > number:
            r = q - 1
        elif r[q] < number:
            r = q + 1
    return pre_number

    
 
print(number)

random_predict (pre_number)

