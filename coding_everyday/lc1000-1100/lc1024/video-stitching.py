class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        sorted_clips = sorted(clips, key=lambda x: (x[0], -x[1]))

        # print(sorted_clips)
        rec = [999] * 101

        visited = set()
        for i in range(len(sorted_clips)):
            s, e = sorted_clips[i]
            if s in visited:
                continue
            visited.add(s)

            if i == 0:
                for j in range(s, e + 1):
                    rec[j] = 1
            else:
                for j in range(s + 1, e + 1):
                    rec[j] = min(rec[j], rec[s] + 1)

        # print(rec)
        return -1 if rec[time] == 999 or rec[0] == 999 else rec[time]
# [3,3,2,3,2,2,1,1,1,1]
# [1,1,1,1,1,1,1,2,2,2,2,