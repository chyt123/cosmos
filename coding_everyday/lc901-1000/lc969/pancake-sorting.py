class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def pancake(arr, k):
            return arr[:k + 1][::-1] + arr[k + 1:]

        n = len(arr)
        ans = []
        for cnt in range(n):
            k = 0
            max_num = arr[0]
            for i in range(n - cnt):
                if arr[i] > max_num:
                    max_num = arr[i]
                    k = i
            # print(k, max_num)
            arr = pancake(arr, k)
            # print(arr)
            arr = pancake(arr, n - cnt - 1)
            # print(arr)
            ans.append(k + 1)
            ans.append(n - cnt)

        return ans
