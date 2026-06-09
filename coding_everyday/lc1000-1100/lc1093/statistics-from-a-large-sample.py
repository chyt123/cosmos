class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        n = len(count)
        for i in range(n):
            if count[i] != 0:
                minimum = i
                break

        for i in range(n - 1, -1, -1):
            if count[i] != 0:
                maximum = i
                break
        
        total = 0
        cnt = 0
        occ = 0
        mode = -1
        for i in range(n):
            if count[i] > 0:
                total += i * count[i]
                cnt += count[i]
            if count[i] > occ:
                occ = count[i]
                mode = i
        mean = total / cnt

        mid_cnt = cnt // 2 + 1 if cnt % 2 == 1 else cnt // 2
        cur = 0
        i = 0
        while cur < mid_cnt:
            cur += count[i]
            i += 1
        if cur > mid_cnt:
            median = i - 1
        elif cur == mid_cnt and cnt % 2 == 1:
            median = i - 1
        else:
            cur = i - 1
            while not count[i]:
                i += 1
            median = (cur + i) / 2
        return [minimum, maximum, mean, median, mode]

# [1 1 1 1]
