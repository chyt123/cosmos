class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for cur in range(n, 0, -1):
            bi = bin(cur)[2:]
            if bi not in s:
                return False

        return True