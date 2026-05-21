class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = defaultdict(list)
        for idx, t in enumerate(time):
            mod[t % 60].append(idx)
        # {
        #     30: [0, 2]
        #     20: [1]
        #     40: [3, 4]
        # }
        cnt = 0
        for i in range(31):
            n = len(mod[i])
            if i in [0, 30]:
                cnt += n * (n - 1) // 2
            elif 60 - i in mod:
                cnt += n * len(mod[60 - i])

        return cnt

# Test case
# only 1,