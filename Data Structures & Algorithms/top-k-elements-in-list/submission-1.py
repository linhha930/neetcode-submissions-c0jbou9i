from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [num for num, freq in count.most_common(k)]

        # dict = {}
        # result = []

        # for i, num in enumerate(nums):
        #     if num not in dict:
        #         dict[num] = 0
        #     dict[num] += 1

        # arr = [[] for _ in range(len(nums) + 1)] # arr = bucket list
        # for num, count in dict.items(): # values are counts
        #     arr[count].append(num)

        # for bucket in reversed(arr):
        #     for num in bucket:
        #         result.append(num)
            
        #     if len(result) == k:
        #         return result
        