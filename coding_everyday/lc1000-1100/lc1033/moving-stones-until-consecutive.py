class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        s = a + b + c
        a, c = min(a, b, c), max(a, b, c)
        b = s - a - c

        intervala, intervalb = b - a - 1, c - b - 1

        if intervala == intervalb == 0:
            return [0, 0]
        return [1 if intervala <= 1 or intervalb <= 1 else 2, intervala + intervalb]


# o . o . o

# o o . . o

# o o o

# o . . . o . . . o