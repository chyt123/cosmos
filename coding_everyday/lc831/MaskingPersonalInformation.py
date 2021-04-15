import re


class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:  # email
            S = S.lower()
            email = S.split('@')
            email[0] = email[0][0] + '*****' + email[0][-1]
            return '@'.join(email)
        else:  # phone
            S = re.sub('[^0-9]+', '', S)
            rst = '***-***-' + S[-4:]
            l = len(S)
            if l > 10:
                rst = '+' + '*' * (l-10) + '-' + rst
            return rst


if __name__ == "__main__":
    sol = Solution()
    S = "LeetCode@LeetCode.com"
    S = "AB@qq.com"
    S = "1(234)567-890"
    S = "86-(10)12345678"
    S = "+(501321)-50-23431"
    print(sol.maskPII(S))
