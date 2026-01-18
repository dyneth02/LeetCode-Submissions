from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in dict:
                return [idx, dict[diff]]
            dict[val] = idx

nums = list(map(int, input("Enter numbers : ").split(",")))
tar = input("Enter target : ")
sol = Solution()
result = sol.two_sum(nums, 9)
print(result)