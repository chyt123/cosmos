class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()

        def dfs(path: str, s: str) -> None:
            if path:
                ans.add(path)    
            for i in range(len(s)):
                dfs(path + s[i], s[:i] + s[i + 1:])

        dfs('', tiles)
        return len(ans)

