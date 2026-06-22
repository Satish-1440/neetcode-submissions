class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sorted_s = {}
        sorted_t = {}
        for i in s:
            if i not in sorted_s:
                sorted_s[i] = 0
            sorted_s[i] += 1
        
        for i in t:
            if i not in sorted_t:
                sorted_t[i] = 0
            sorted_t[i] += 1
        if sorted_s == sorted_t:
            return True
        else:
            return False