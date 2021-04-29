from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        i = (start + end) // 2
        while not (arr[i-1] < arr[i] > arr[i+1]):
            print(start, i, end)
            pre = arr[i-1]
            nex = arr[i+1]
            if pre < nex:  # up
                start = i
                i = (i + end) // 2
            else:
                end = i
                i = (start + i) // 2
        return i


if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 0]
    arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    arr = [0, 2, 1, 0]
    arr = [0, 10, 5, 2]
    arr = [3, 4, 5, 1]
    arr = [40,48,61,75,100,99,98,39,30,10]
    arr = [18,29,38,59,98,100,99,98,90]
    print(sol.peakIndexInMountainArray(arr))
