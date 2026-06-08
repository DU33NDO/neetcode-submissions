class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        max_uniq = 1
        if len(s) == 0:
            return 0
        window = set(s[0])
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                max_uniq = max(max_uniq, r - l + 1)
                r += 1
            else:
                window.remove(s[l])
                l += 1
        return max_uniq

              
        