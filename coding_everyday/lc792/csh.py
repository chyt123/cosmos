class Solution(object):
    def numMatchingSubseq(self, S, words):
        rst = 0
        for word in words:
            if self.issubstring(S, word):
                rst += 1
        return rst

    def issubstring(self, S, word):
        pos = -1
        for letter in word:
            pos = S.find(letter, pos + 1)
            if pos == -1:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    S = "abcde"
    words = ["a", "bb", "acd", "ace"]
    print sol.numMatchingSubseq(S, words)

