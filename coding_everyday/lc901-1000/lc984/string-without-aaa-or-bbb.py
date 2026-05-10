class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        swapped = False
        if b > a:
            a, b = b, a
            swapped = True

        ans = ''
        while a - b > 2:
            ans += 'aa'
            ans += 'b'
            a -= 2
            b -= 1

        if a > 0 and b > 0:
            if a >= b:
                ans += 'ab' * b
                a -= b
                b = 0
            else:
                ans += 'ba' * a
                b -= a
                a = 0

        if a > 0:
            ans += 'a' * a
        else:
            ans += 'b' * b

        return ans if not swapped else ans.replace('a', 'c').replace('b', 'a').replace('c', 'b')
