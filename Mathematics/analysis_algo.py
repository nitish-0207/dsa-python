import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

from count_digits import count_digits
from is_prime import is_prime
from hcf_of_two_numbers import hcf
from factorial import factorial
time = []
inp_size = []
n = 1
while n < 10 ** 6:
    start = datetime.now()
    print(start)
    factorial(n)
    end = datetime.now()
    print(end)
    inp_size.append(n)
    print((end - start).microseconds)
    time.append((end - start).microseconds)
    n = n * 10

plt.plot(inp_size, time)
plt.show()


