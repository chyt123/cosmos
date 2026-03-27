from typing import List
# class Solution:
#     def expressiveWords(self, S: str, words: List[str]) -> int:
#         cnt = 0
#         for i in words:
#             cnt += int(self.check(S, i))
#         return cnt
#
#     def check(self, S, word):
#         while word and S:
#             if S[0] == word[0]:
#                 max_head_s = self.maxHead(S)
#                 max_head_word = self.maxHead(word)
#                 if (max_head_s >= 3 and max_head_s >= max_head_word) or max_head_s == max_head_word:
#                     S = S[max_head_s:]
#                     word = word[max_head_word:]
#                 else:
#                     return False
#             else:
#                 return False
#         if S or word:
#             return False
#         return True
#
#     def maxHead(self, word):
#         cnt = 0
#         cmp = word[0]
#         for ch in word:
#             if ch != cmp:
#                 return cnt
#             cnt += int(ch == cmp)
#         return cnt


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        key_s, num_s = self.keyNum(S)
        cnt = 0
        for word in words:
            key_word, num_word = self.keyNum(word)
            print(key_s, num_s, key_word, num_word)
            if key_s == key_word:
                valid = True
                for i in range(len(num_s)):
                    if not ((num_s[i] >= 3 and num_s[i] >= num_word[i]) or num_s[i] == num_word[i]):
                        valid = False
                        break
                if valid:
                    cnt += 1
        return cnt

    def keyNum(self, word):
        if not word:
            return '', None
        cmp = word[0]
        key = ''
        num = []
        cnt = 0
        for ch in word:
            if ch == cmp:
                cnt += 1
            else:
                key += cmp
                num.append(cnt)
                cmp = ch
                cnt = 1
        key += cmp
        num.append(cnt)
        return key, num


if __name__ == "__main__":
    sol = Solution()
    S = "heeellooo"
    words = ["hello", "hi", "helo"]

    print(sol.expressiveWords(S, words))
