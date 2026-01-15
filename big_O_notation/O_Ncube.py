# -------cube complexity----------------

class Solution:
    def threeSum(self, nums: List[int]) -> List[list[List[int]]:
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
