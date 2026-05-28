class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sort by diff desc
        costs = sorted(costs, key=lambda x: [-abs(x[0] - x[1])])

        # go by lower price
        cnt_a, cnt_b = 0, 0
        choices = []
        for i in range(len(costs)):
            cost_a, cost_b = costs[i]
            if cost_a >= cost_b:
                cnt_b +=1
                choices.append('b')
            else:
                cnt_a += 1
                choices.append('a')

        # adjust from least diff
        adjust = (cnt_a - cnt_b) // 2  # -: b->a, +: a-> b

        for i in range(len(choices) - 1, -1 , -1):
            if adjust == 0:
                break
            if adjust < 0 and choices[i] == 'b':
                choices[i] = 'a'
                adjust += 1
            elif adjust > 0 and choices[i] == 'a':
                choices[i] = 'b'
                adjust -= 1

        ans = 0
        for i in range(len(costs)):
            cost_a, cost_b = costs[i]
            ans += cost_a if choices[i] == 'a' else cost_b

        return ans





# [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
#     511       394       259       45       722        108
#      a         b         b         b(a)     b          b(a)