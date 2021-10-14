from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i) > ord(target):
                return i
        return letters[0]


if __name__ == "__main__":
    sol = Solution()
    letters = ["c", "f", "j"]
    targets = ['a', 'c', 'd', 'g', 'j', 'k']
    for target in targets:
        print(sol.nextGreatestLetter(letters, target))
