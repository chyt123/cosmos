import math
from typing import List
from collections import deque, defaultdict, OrderedDict


class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        sorted2 = sorted(nums2)
        assigned = {
            b: [] for b in nums2
        }
        wait = []
        pt = 0
        while nums1:
            cur = nums1.pop(0)
            if cur > sorted2[pt]:
                assigned[sorted2[pt]].append(cur)
                pt += 1
            else:
                wait.append(cur)
        ans = [assigned[b].pop() if assigned[b] else wait.pop() for b in nums2]
        return ans
        # ans = [-1] * len(nums1)
        # wait = []
        # nums1.sort()
        # shadow_nums2 = OrderedDict()
        # for idx, i in enumerate(nums2):
        #     if i in shadow_nums2:
        #         shadow_nums2[i].append(idx)
        #     else:
        #         shadow_nums2[i] = [idx]
        # shadow_nums2 = sorted(shadow_nums2.items(), key=lambda t: t[0])
        #
        # while nums1:
        #     cur = nums1.pop(0)
        #     if cur > shadow_nums2[0][0]:
        #         idx = shadow_nums2[0][1].pop()
        #         ans[idx] = cur
        #         if not shadow_nums2[0][1]:
        #             shadow_nums2.pop(0)
        #     else:
        #         wait.append(cur)
        # for idx, i in enumerate(ans):
        #     if i == -1:
        #         ans[idx] = wait.pop()
        # return ans


if __name__ == "__main__":
    sol = Solution()
    nums1 = [2, 7, 11, 15]
    nums2 = [1, 10, 4, 11]
    nums1 = [2, 0, 4, 1, 2]
    nums2 = [1, 3, 0, 0, 2]
    nums1 = [12, 24, 8, 32]
    nums2 = [13, 25, 32, 11]
    print(sol.advantageCount(nums1, nums2))
