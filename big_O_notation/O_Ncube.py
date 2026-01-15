# -------cube complexity----------------
from typing import List


class Solution:  # declaring the class
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # it is a method, self - is mandatory, refer to object
        # nums: List[int] is annotation type for parameter nums
        n = len(nums)
        result = []
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)
        return result
    print(threeSum)
