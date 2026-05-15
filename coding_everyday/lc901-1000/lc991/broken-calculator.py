class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        s = startValue
        if s > target:
            return s - target

        log2ts = ceil(log2(target / s))
        cnt = log2ts if log2ts >= 0 else 0

        tmp_cnt = 0
        while True:
            diff = s * 2 ** cnt - target
            bin_diff = str(bin(diff))[2:]
            if len(bin_diff) <= cnt + 1:
                break
            s -= 1
            tmp_cnt += 1

        for c in bin_diff:
            if c == '1':
                cnt += 1

        return cnt + tmp_cnt