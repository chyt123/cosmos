from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        l = len(S)
        for i in range(1, l // 2 + 1):  # len of first num
            f1 = S[:i]
            # print(f1)
            for j in range(1, min(l-2*i, (l-i)//2) + 1):  # len of second num
                f2 = S[i:i+j]
                # print('    ', f2)
                l1 = i
                l2 = j
                if str(int(f1)) == str(f1) and str(int(f2)) == str(f2):
                    n1 = int(f1)
                    n2 = int(f2)
                    rst = [n1]
                    while S[l1+l2:].startswith(str(n1 + n2)):
                        rst.append(n2)
                        tmp = n1
                        n1 = n2
                        n2 = tmp + n1
                        l1 = l1 + l2
                        l2 = len(str(n2))
                    if l1 + l2 >= l:
                        rst.append(n2)
                        for k in rst:
                            if k > 2 ** 31 - 1:
                                return []
                        return rst
        return []


if __name__ == "__main__":
    sol = Solution()
    S = "123456579"
    S = "123"
    S = "11235813"
    S = "112358130"
    S = "012358"
    S = "1101111"
    S = "17522"
    S = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    print(sol.splitIntoFibonacci(S))
