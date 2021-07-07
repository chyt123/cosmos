# csv

# name,foo,bar
# test,foo1,bar1

# input:
'''
def read_line(s):
    # return s.split(',')
    rtn = ['']
    flag = False
    for i in s:
        if i == ',' and not flag:
            rtn.append('')
        elif i == ' ' and not flag:
            continue
        elif i == '"':
            flag = not flag
        else:
            rtn[-1] += i  # -1: last element,
    return rtn


# '123,"3,545",abc',
# rtn = ['123', '3,545', 'abc']


test_cases = [
    '',  # ['']
    ',',  # ['', '']
    '123,'  # ['123', '']
    ',345',  # ['', '345']
    '123,"3,545",abc',
    '123,"3,545",abc , def',
    'test,foo1,bar1,abc,def',
]
for i in test_cases:
    print(read_line(i))
'''
import collections

'''
# abccccd
# abc4d

def compress_str(s):
    if not s:
        return ''
    rtn = ''
    cur = s[0]
    cnt = 1
    for i in range(1, len(s)):
        if s[i] != cur:  # new char
            rtn += cur
            rtn += '' if cnt == 1 else str(cnt)  # ? :
            cur = s[i]
            cnt = 1
        else:
            cnt += 1
    rtn += cur
    rtn += '' if cnt == 1 else str(cnt)  # ? :
    return rtn


test_cases = [
    '',
    'a',
    'abcd',
    'aaabbbbcddd',
    'aaabbbbbbbbbbbbbcddd',
]
'''

'''
# evaluate
# '123+2*5/3-5/3',

# rst = 124.666667
# cur = '-1.66667'
# post = '3'
# symbol = '/'

# 1-3
# rst = -2
# cur = '-3'

def evaluate(s):
    rst = 0
    cur = ''
    post = ''
    symbol = ''
    for i in s:
        if i.isnumeric():
            if symbol:  # we are doing * /
                post += i
            else:  #
                cur += i
        else:
            if symbol:
                # in py3, 5 / 3 = 1.6667
                cur = str(float(cur) * float(post)) if symbol == '*' else str(float(cur) / float(post))
                symbol = ''
                post = ''
            if i in ['+', '-']:
                rst += float(cur)
                cur = i
            elif i in ['*', '/']:
                symbol = i

    if symbol:
        cur = str(float(cur) * float(post)) if symbol == '*' else str(float(cur) / float(post))
    rst += float(cur)

    return rst


test_cases = [
    '5/3',  # 1.66667
    '10+8'
    '1+2*5/3-5/3',
]


# ((1+2)*3/(4-5)+6)*7
# rst = 0
# p = []
# token = [['-21']]
'''

# uuid
# frequency: 100/ms
# 10 machines , 00000~09999, 10000~19999, ...
# request: type(1, 2, 3) + timestamp(ms since 1970-1-1) + md5_hash(username, header, cookie) + 00000


def bfs(edges, start, end):
    graph = collections.defaultdict()
    father_node = []
    q = collections.deque()
    q.append(start)
    visited = set()
    for i, j in edges:
        graph[i] = j
        graph[j] = i
    while q:
        cur = q.popleft()
        if cur not in visited:
            visited.add(cur)
            for son in graph[cur]:
                q.append(son)


edges = [[0,1], [1,2], [1,3], [0,2], [3,4]]
print(bfs(edges, 0, 4))