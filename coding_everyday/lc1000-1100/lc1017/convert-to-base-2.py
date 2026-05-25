class Solution:
    def baseNeg2(self, n: int) -> str:
        ans = ''
        # while n != 0:
        #     ans += str(n & 1)
        #     n = -(n >> 1)
        # return ans[::-1] if ans else '0'

        while n != 0:
            r = n % -2
            n = n // -2
            if r < 0:
                r += 2
                n += 1

            ans += str(r)

        return ans[::-1] if ans else '0'