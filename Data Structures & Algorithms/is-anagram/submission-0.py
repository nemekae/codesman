class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sx = ''.join(sorted(s))
        tx = ''.join(sorted(t))
        return sx == tx

        
        