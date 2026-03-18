from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for c in word:
                ans[ord(c) - ord('a')] += 1
            return ans

        # combine words2
        combine_b = [0] * 26
        for w in words2:
            cnt_w = count(w)
            for i in range(26):
                combine_b[i] = max(combine_b[i], cnt_w[i])

        ans = []
        for w in words1:
            cnt_w = count(w)
            skip = False
            for i in range(26):
                if cnt_w[i] < combine_b[i]:
                    skip = True

            if not skip:
                ans.append(w)

        return ans

if __name__ == "__main__":
    sol = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["lo","eo"]

    print(sol.wordSubsets(words1, words2))
