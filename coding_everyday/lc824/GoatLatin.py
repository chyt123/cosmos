class Solution:
    def toGoatLatin(self, S: str) -> str:
        s_list = S.split(' ')
        for i, word in enumerate(s_list):
            if word[0] not in 'aeiouAEIOU':
                s_list[i] = word[1:] + word[0]
            s_list[i] += 'ma' + 'a' * (i+1)
        return ' '.join(s_list)


if __name__ == "__main__":
    sol = Solution()
    S = "I speak Goat Latin"
    print(sol.toGoatLatin(S))
