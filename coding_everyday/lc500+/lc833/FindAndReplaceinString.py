from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        order = {i: idx for idx, i in enumerate(indexes)}
        bias = 0
        for num in sorted(order.keys()):
            idx = order[num]
            if S[num+bias:].startswith(sources[idx]):
                S = S[:num+bias] + targets[idx] + S[num+bias+len(sources[idx]):]
                bias += len(targets[idx]) - len(sources[idx])
        return S


if __name__ == "__main__":
    sol = Solution()
    # S = "abcd"
    # indexes = [0, 2]
    # sources = ["a", "cd"]
    # targets = ["eee", "ffff"]
    # S = "abcd"
    # indexes = [0, 2]
    # sources = ["ab", "ec"]
    # targets = ["eee", "ffff"]
    S = "vmokgggqzp"
    indexes = [3, 5, 1]
    sources = ["kg", "ggq", "mo"]
    targets = ["s", "so", "bfr"]
    print(sol.findReplaceString(S, indexes, sources, targets))
