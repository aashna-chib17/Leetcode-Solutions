class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        count = 0
        for i in nums:
            if d.get(k-i):
                count += 1
                d[k-i]-=1
            elif i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        return count
                
        
