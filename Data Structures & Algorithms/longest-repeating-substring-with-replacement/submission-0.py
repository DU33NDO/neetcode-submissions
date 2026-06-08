class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_count = {}
        max_len = 0

        for r in range(len(s)): # 0 1 2 3 for XYYX
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            if r - l + 1 - max(char_count.values()) > k:
                char_count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len