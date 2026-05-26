class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []

        for i in queries:
            m = 0
            n = 0
            flag = True
            while m < len(i) and n < len(pattern):
                if i[m] == pattern[n]:
                    m += 1
                    n += 1
                elif 'A' <= i[m] <= 'Z':
                    flag = False
                    break
                else:
                    m += 1

            # check pattern finished
            if n != len(pattern):
                flag = False

            # check i tail
            while m < len(i):
                if 'A' <= i[m] <= 'Z':
                    flag = False
                m += 1

            ans.append(flag)

        return ans
