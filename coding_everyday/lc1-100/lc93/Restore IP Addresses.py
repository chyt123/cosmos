import bisect
from typing import List
from collections import defaultdict
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def is_valid(self, num: str):
        if num.startswith('0') and num != '0':
            return False
        if not 0 <= int(num) <= 255:
            return False
        return True

    def is_valid_ip(self, ip):
        nums = ip.split('.')
        if len(nums) != 4:
            return False
        for i in nums:
            if not self.is_valid(i):
                return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) > 12 or len(s) < 4:
            return []
        ans = set()

        def bt(lv, pt, cur):
            if len(cur) > len(s) + 3:
                return
            if pt == 3 or lv == len(s) - 1:
                cand = cur + s[lv:]
                if self.is_valid_ip(cand) and cand not in ans:
                    ans.add(cand)
                return
            cur += s[lv]
            cur += '.'
            bt(lv + 1, pt + 1, cur)
            cur = cur[:-1]
            bt(lv + 1, pt, cur)

        bt(0, 0, '')
        return list(ans)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "1111",
        "25525511135",
        "0000",
        "010010",
        "101023",
        "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
    ]
    for i in test_cases:
        result = sol.restoreIpAddresses(i)
        print(result)
