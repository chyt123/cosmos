from typing import List
from collections import deque, OrderedDict
import heapq


class Solution:
    def print_structure(self, paths: List[str]) -> None:
        sys = dict()
        for i in paths:
            q = deque(i.split('/')[1:])
            root = sys
            while q:
                cur = q.popleft()
                if cur not in root:
                    root[cur] = dict()
                root = root[cur]

        def print_helper(parent, r, lv):
            if not r:
                return
            pre = '    ' * lv
            print('{}-- {}'.format(pre, r))
            for s in sorted(parent[r]):
                print_helper(parent[r], s, lv + 1)

        for i in sorted(sys):
            print_helper(sys, i, 0)


if __name__ == "__main__":
    sol = Solution()
    paths = [
        "/app/components/zeader",
        "/app/components/header",
        "/app/services",
        "/app/tests/components/header",
        "/images/image.png",
        "/tsconfig.json",
        "/index.html",
    ]
    print(sol.print_structure(paths))
'''
-- app
    -- components
        -- header
        -- zeader
    -- services
    -- tests
        -- components
            -- header
-- images
    -- image.png
-- index.html
-- tsconfig.json
'''
