from typing import List
from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = Counter()
        for i in cpdomains:
            cnt_addr = i.split(' ')
            cnt = int(cnt_addr[0])
            addr = cnt_addr[1]
            while addr:
                ans[addr] += cnt
                idx = addr.find('.')
                if idx < 0:
                    break
                addr = addr[addr.find('.')+1:]
        return ['{} {}'.format(v, k) for k, v in ans.items()]


if __name__ == "__main__":
    sol = Solution()
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(sol.subdomainVisits(cpdomains))
