import re
from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter = Counter(re.sub('[0-9\ ]+', '', licensePlate).lower())
        words.sort(key=lambda x: len(x))
        for idx, w in enumerate(words):
            flag = True
            for ch, num in counter.items():
                if w.count(ch) < num:
                    flag = False
                    break
            if flag:
                return w


if __name__ == "__main__":
    sol = Solution()
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    licensePlate = "1s3 456"
    words = ["looks", "pest", "stew", "show"]
    licensePlate = "Ah71752"
    words = ["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent", "writer", "old"]
    print(sol.shortestCompletingWord(licensePlate, words))
