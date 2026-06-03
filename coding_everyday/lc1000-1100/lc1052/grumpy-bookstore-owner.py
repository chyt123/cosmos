class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers) # 8
        satisfied = sum(customers[:minutes]) # 2

        for i in range(minutes, n):
            satisfied += customers[i] if not grumpy[i] else 0

        maxx = satisfied # 10

        for i in range(1, n - minutes + 1):
            left = i - 1
            tail = i + minutes - 1
            if grumpy[tail]:
                satisfied += customers[tail]
            if grumpy[left]:
                satisfied -= customers[left]
            maxx = max(maxx, satisfied)
        
        return maxx
