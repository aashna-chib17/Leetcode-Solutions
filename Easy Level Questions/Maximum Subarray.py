
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = float('-inf')
        for i in nums:
            sum += i
            maxSum = max(maxSum,sum)
            if sum < 0:
                sum = 0
        return maxSum
        
