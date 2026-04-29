class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        dir = True
        counting = False
        ans = 1
        cnt = 0
        for i in range(1, n):
            if not counting:
                if arr[i] == arr[i - 1]:
                    continue
                dir = True if arr[i] < arr[i - 1] else False
                counting = True
                cnt = 2
            else:
                if dir and arr[i] > arr[i - 1] or not dir and arr[i] < arr[i - 1]:
                    cnt += 1
                    dir = not dir
                else:
                    ans = max(ans, cnt)
                    if arr[i] == arr[i - 1]:
                        counting = False
                    else:
                        dir = True if arr[i] < arr[i - 1] else False
                        cnt = 2

        return max(ans, cnt)
