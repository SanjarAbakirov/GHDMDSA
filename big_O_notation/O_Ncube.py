from typing import List


class Solution:  # declaring the class
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # it is a method, self - is mandatory, refer to object
        # nums: List[int] is annotation type for parameter nums
        # nums - name of the parameter
        # List[int] - decret nums to be List of integers
        # from from typing import List -> imports -> List[List[int]]: the annotaion returned value
        # List[List[int]]: - the method of returned integers
        n = len(nums)
        result = []
        print(f"\n===Starting threeSum===")
        print(f"Input list: {nums}")

        for i in range(n - 2):
            print(f"\nCheking i={i} (value: {nums[i]})")
            for j in range(i + 1, n - 1):
                print(f"\nCheking j={j} (value: {nums[j]})")
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            print(
                                f"Found zero-sum triplet at positions ({i}, {j}, {k}): {triplet}")
                            print(f"print of founded triplet: {triplet}")
                            result.append(triplet)
                        else:
                            print(f" ! Duplicate triplet: {triplet}")
        print(f"final result: {result}")
        return result


# The example
if __name__ == "__main__":
    solution = Solution()

    # test 1
    print("Test 1:")
    test_nums = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(test_nums)

    # test 2
    print("\n" + "="*50 + "\n")
    print("Test 2:")
    test_nums2 = [0, 0, 0]
