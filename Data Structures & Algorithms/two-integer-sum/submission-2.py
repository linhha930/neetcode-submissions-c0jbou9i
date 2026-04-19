class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        dict = {}

        for i, val in enumerate(nums): 
            remainder = target - val

            if remainder not in dict:
                dict[val] = i
            else:
               return [dict[remainder], i]
