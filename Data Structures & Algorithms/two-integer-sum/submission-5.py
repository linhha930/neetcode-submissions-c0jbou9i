class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        dict = {}

        for i, val in enumerate(nums): 
            remainder = target - val

            if remainder in dict:
                return [dict[remainder], i]
            else:
                dict[val] = i