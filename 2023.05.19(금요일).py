# def c_to_f(c):
#     f = (c * 9/5) + 32
#     return f
#
# print(c_to_f(24))

import random

def lotto():
    nums = random.sample(range(1,46), 8 )
    return sorted(nums)

print("로또 번호:", lotto())
