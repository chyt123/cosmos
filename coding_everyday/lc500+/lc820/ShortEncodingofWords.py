from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        new_words = sorted([i[::-1] for i in words], reverse=True)
        l = len(new_words)
        s = '#' + new_words[0]
        for i in range(1, l):
            if not new_words[i-1].startswith(new_words[i]):
                s += '#' + new_words[i]
        return len(s)


if __name__ == "__main__":
    sol = Solution()
    words = ["time", "ime", "me", "e", "abc"]
    words = ["me", "time"]
    words = ["time", "me", "bell"]
    print(sol.minimumLengthEncoding(words))
