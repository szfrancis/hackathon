import numpy as np

a = [3,4,1,4,1,2,3]

def sing_num(nums):
    (vals, counts) = np.unique(nums, return_counts=True)
    for v,c in zip(vals,counts):
        if c==1:
            return v

print(sing_num(a))
