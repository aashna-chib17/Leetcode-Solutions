class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if d.get(i):
                d[i]+=1
            else:
                d[i]=1
        for i in d.values():
            if i>1:
                return True
        return False
      
