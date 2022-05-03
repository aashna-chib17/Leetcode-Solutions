class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sortedArr = sorted(nums)
        low = len(nums) - 1
        high = 0
        for i in range(len(nums)):
            if nums[i] != sortedArr[i]:
                low = min(low,i)
                high = max(high,i)
        
        if low>=high:
            return 0
        else:
            return high-low+1
       
