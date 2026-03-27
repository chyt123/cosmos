from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_set = set()
        for word in words:
            morse_code = ''
            for ch in word:
                morse_idx = ord(ch) - 97
                morse_code += MORSE[morse_idx]
            morse_set.add(morse_code)
        return len(morse_set)


if __name__ == "__main__":
    sol = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print(sol.uniqueMorseRepresentations(words))

