class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = ['']
        d = {}
        stack = []

        def getval(x):
            return d.get(x, x)

        def calc(tokens):
            if tokens[0] == 'let':
                for i in range(1, len(tokens)-1, 2):
                    if tokens[i+1]:
                        d[tokens[i]] = getval(tokens[i+1])
                return getval(tokens[-1])

            elif tokens[0] in ['add', 'mult']:
                x, y = map(getval, tokens[1:])
                x = int(x)
                y = int(y)
                return str(x + y if tokens[0] == 'add' else x * y)

        for c in expression:
            if c == '(':
                if tokens[0] == 'let':
                    calc(tokens)
                stack.append((tokens, dict(d)))
                tokens = ['']
            elif c == ')':
                val = calc(tokens)
                (tokens, d) = stack.pop()
                tokens[-1] += val
            elif c == ' ':
                tokens.append('')
            else:
                tokens[-1] += c
        return int(tokens[0])


if __name__ == "__main__":
    sol = Solution()
    expression = '(add 1 2)'
    expression = '(mult 3 (add 2 3))'
    expression = '(let x 2 (mult x (let x 3 y 4 (add x y))))'
    expression = '(let x 3 x 2 x)'
    expression = '(let x 1 y 2 x (add x y) (add x y))'
    expression = '(let x 2 (add (let x 3 (let x 4 x)) x))'
    expression = '(let a1 3 b2 (add a1 1) b2)'
    expression = "(let x -2 y x y)"
    expression = "(let x (add 12 -7) (mult x x))"
    expression = "(let a -122 b 0 (add (add 1 -4) (mult a 66)))"
    expression = "(let var 78 b 77 (let c 33 (add c (mult var 66))))"
    expression = "(let x -5 xy -7 (let x 4 (add x xy)))"
    print(sol.evaluate(expression))

