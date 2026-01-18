from typing import List

class Solution:
    def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
        set_of_numbers = set(nums)
        ret = []
        for i in range(1, len(nums) + 1):
            if i not in set_of_numbers:
                ret.append(i)

        return ret

nums = list(map(int, input("Enter numbers : ").split(",")))
solution = Solution()
result = solution.find_disappeared_numbers(nums)
print(result)