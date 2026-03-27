from collections import Counter


class Solution(object):
    def customSortString(self, S, T):
        non_ex = ans = ""
        for ch in T:
            if ch not in S:
                non_ex += ch

        counter = Counter(T)

        for ch in S:
            ans += ch * counter[ch]

        return ans + non_ex


if __name__ == "__main__":
    sol = Solution()
    S = "cba"
    T = "abaasdbcacd"
    print sol.customSortString(S, T)

