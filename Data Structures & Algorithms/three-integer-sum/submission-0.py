class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort() # sorted arr = dupes next to ea other

        for i, num in enumerate(nums):
            # check if current element is a duplicate of previous (if so, skip)
            if i > 0 and nums[i] == nums[i - 1]: 
                continue

            left = i + 1 # pointers for indices
            right = len(nums) - 1
            
            while left < right:                    
                if (num + nums[left] + nums[right]) < 0:
                    left += 1
                elif (num + nums[left] + nums[right]) > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip dupes for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

        