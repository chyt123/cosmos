class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [chr(ord('a') + i) for i in range(26)]

        def find(x):
            return x if parent[ord(x) - ord('a')] == x else find(parent[ord(x) - ord('a')])

        for e in equations:
            if e[1] == '=':
                parent[ord(find(e[0])) - ord('a')] = find(e[3])

        # print(parent)
        for e in equations:
            if e[1] == '!' and find(e[0]) == find(e[3]):
                return False

        return True