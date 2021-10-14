class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = ['']
        s = S.lower()
        for i in s:
            if 'a' <= i <= 'z':
                lower = [x + i for x in result]
                upper = [x + i.upper() for x in result]
                result = lower + upper
            else:
                result = [x + i for x in result]
        return result


if __name__ == "__main__":
    sol = Solution()
    S = '12345'
    print sol.letterCasePermutation(S)

