from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        l = len(formula)
        stack = [Counter()]
        i = 0
        while i < l:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                start = i
                while i < l and formula[i].isnumeric():
                    i += 1
                multi = int(formula[start:i] or 1)
                for name, num in top.items():
                    stack[-1][name] += multi * num
            else:
                start = i
                i += 1
                while i < l and formula[i].islower():
                    i += 1
                name = formula[start:i]
                start = i
                while i < l and formula[i].isnumeric():
                    i += 1
                num = int(formula[start:i] or 1)
                stack[-1][name] += num

        ans = ''
        for name, num in sorted(stack[0].items()):
            ans += name
            ans += '' if num == 1 else str(num)
        return ans


if __name__ == "__main__":
    sol = Solution()
    formula = "K4(ON(SO3)2)2"
    formula = "Mg(OH)2"
    formula = "H2O"
    formula = "Be32"
    print(sol.countOfAtoms(formula))
