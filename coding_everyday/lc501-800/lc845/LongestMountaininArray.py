from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        l = len(arr)
        if l < 3:
            return 0
        up = True
        ans = 0
        cnt = 0
        for i in range(0, l - 1):
            print(arr[i], '-------')
            if up:
                if arr[i] == arr[i + 1]:
                    cnt = 0
                    continue
                if arr[i] < arr[i + 1]:
                    cnt += 1
                if arr[i] > arr[i + 1] and cnt >= 1:
                    cnt += 1
                    up = False
                    if i != l - 2:
                        continue
                    else:
                        return max(ans, cnt + 1)
            else:
                if arr[i] > arr[i + 1]:
                    cnt += 1
                if arr[i] <= arr[i + 1] or i == l - 2:
                    cnt += 1
                    up = True
                    ans = max(ans, cnt)
                    cnt = 0 if arr[i] == arr[i + 1] else 1
            print('    ', cnt)
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 1, 4, 7, 3, 2, 5]
    arr = [2, 2, 2]
    arr = [0,1,2,3,4,5,4,3,2,1,0]
    arr = [0, 1, 0]
    arr = [875, 884, 239, 731, 723, 685]
    print(sol.longestMountain(arr))
    arr = [0,0,1,0,0,1,1,1,1,1]
    arr = [0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1]
