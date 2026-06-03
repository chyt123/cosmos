class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                maxx = 0
                max_idx = -1
                for j in range(i + 1, n):
                    if arr[j] < arr[i] and arr[j] > maxx:
                        maxx = arr[j]
                        max_idx = j
                arr[i], arr[max_idx] = arr[max_idx], arr[i]
                return arr
        return arr
# 12543
