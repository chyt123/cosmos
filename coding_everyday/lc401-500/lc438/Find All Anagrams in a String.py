from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def isAnagrams(cnt_x, cnt_y):
            for i in range(26):
                if cnt_x[i] != cnt_y[i]:
                    return False
            return True

        if len(p) >= len(s):
            return []
        # init
        cnt_s = [0] * 26
        cnt_p = [0] * 26

        for i in range(len(p)):
            cnt_s[ord(s[i]) - ord('a')] += 1
            cnt_p[ord(p[i]) - ord('a')] += 1

        ans = []
        for i in range(len(s) - len(p) + 1):
            if i > 0:
                cnt_s[ord(s[i - 1]) - ord('a')] -= 1
                cnt_s[ord(s[i + len(p) - 1]) - ord('a')] += 1
            if isAnagrams(cnt_s, cnt_p):
                ans.append(i)
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["cbaebabacd", "abc"],
        ["abab", "ab"],
    ]
    for i, j in test_cases:
        print(sol.findAnagrams(i, j))
