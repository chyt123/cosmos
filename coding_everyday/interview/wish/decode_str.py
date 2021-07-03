#coding=utf-8
import sys

def myDecode(s):
    num_mem = ['']
    ch_mem = ['']
    for i in s:
        if i.isalpha():
            ch_mem[-1] += i
        elif i.isnumeric():
            num_mem[-1] += i
        elif i == '[':
            ch_mem.append('')
            num_mem.append('')
        else:
            cur_str = ch_mem.pop()
            cur_num = int(num_mem.pop(-2))
            ch_mem[-1] += cur_str * cur_num
        print(i, ch_mem, num_mem)
    return ch_mem[-1]

# num_mem = [2]
# ch_mem = [[abcdcsasasa..weererui], [er]]
# abc2[dc13[sa]we]2[er]ui
s = 'abc2[dc13[sa]we]2[er]ui'
print(myDecode(s))