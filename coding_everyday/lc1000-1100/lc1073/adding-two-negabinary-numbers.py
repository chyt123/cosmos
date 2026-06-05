class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sum_base10 = 0
        m = len(arr1)
        n = len(arr2)
        for i in range(m):
            sum_base10 += arr1[m - 1 - i] * (-2)**i
        
        for i in range(n):
            sum_base10 += arr2[n - 1 - i] * (-2)**i
        

        ans = []
        while sum_base10 != 0:
            mod = sum_base10 % (-2)
            sum_base10 = sum_base10 // (-2)
            if mod == -1:
                mod = 1
                sum_base10 += 1
            ans.append(mod)

        ans.reverse()
        return ans if ans else [0]
# 11
# -5..1
# 3 ..1
# -1 ..1
# 1 ..1
# 0 ..1

