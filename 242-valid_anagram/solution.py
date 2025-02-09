class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        s_count = {}
        t_count = {}
        for chars in s:
            s_count[chars] = s_count.get(chars, 0) + 1
        for charx in t:
            t_count[charx] = t_count.get(charx, 0) + 1 