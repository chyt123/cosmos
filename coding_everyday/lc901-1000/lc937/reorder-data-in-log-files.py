class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for l in logs:
            first = l.split(' ')[1]
            if first.isnumeric():
                digit_logs.append(l)
            else:
                s = l.split(' ')
                letter_logs.append((l, s[0], s[1:]))

        return [i[0] for i in sorted(letter_logs, key=lambda x : (x[2], x[1]))] + digit_logs