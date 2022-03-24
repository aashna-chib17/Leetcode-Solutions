class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        temp = False
        for i in letters:
            if i>target:
                temp = True
                return i
        if temp == False:
            return letters[0]
