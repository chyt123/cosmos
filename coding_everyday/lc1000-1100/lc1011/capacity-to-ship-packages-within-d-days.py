class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        n = len(weights)
        r = l * ceil(n / days)

        if days >= n:
            return l

        # upper_bound = max_weight * ceil(n / days)

        while l < r:
            print(l, r)
            mid = (l + r) // 2

            day_num = 1
            cur_weight = 0
            flag = True
            for j in weights:
                if cur_weight + j <= mid:
                    cur_weight += j
                else:
                    day_num += 1
                    cur_weight = j

                if day_num > days:
                    flag = False
                    break

            if flag:
                r = mid
            else:
                l = mid + 1
        return r

