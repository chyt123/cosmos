import re
from typing import List
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = re.sub('[^0-9a-zA-Z]+', ' ', paragraph).lower()
        str_list = s.split(' ')
        cnt = Counter(str_list)
        while True:
            cur = cnt.most_common(1)[0][0]
            if cur in banned:
                cnt.pop(cur)
            else:
                return cur


if __name__ == "__main__":
    sol = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    paragraph = "b b b b"
    banned = []
    print(sol.mostCommonWord(paragraph, banned))
