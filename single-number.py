# Time:  O(n)
# Space: O(1)

import operator
from functools import reduce

class Solution(object):
    """
    :type nums: List[int]
    :rtype: int
    """
    def singleNumber(self, A):
        return reduce(operator.xor, A)



# test 
vcap = Solution()
print(vcap.singleNumber([3,4,1,4,1,2,3]))