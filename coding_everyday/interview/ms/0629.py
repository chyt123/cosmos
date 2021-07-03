# [1, 2, 3, 5, 7, 2]
# sort, max num

# [12, 34, 56]

# [1111, 1112, 1113, 56]
from functools import cmp_to_key


def comp_merged_str(s1, s2):
    if s1 + s2 > s2 + s1:
        return 1
    elif s1 + s2 == s2 + s1:
        return 0
    else:
        return -1


def merge_nums(nums):
    if not nums:
        return ''
    zero_flag = True
    str_nums = []
    for i in nums:
        if i > 0:
            zero_flag = False
        str_nums.append(str(i))
    str_nums = sorted(str_nums, key=cmp_to_key(comp_merged_str), reverse=True)
    return ''.join(str_nums) if not zero_flag else '0'


test_cases = [
    # (input, expected_out)
    ([12, 34, 56], '563412'),
    ([1111, 1112, 1113, 535, 0, 56], '565351113111211110'),
    ([56, 5, 53], '56553'),
    ([111111111111111111111111111111111111111111111, 8], '8111111111111111111111111111111111111111111111'),
    ([0, 2, 0], '200'),
    ([0, 0, 0, 0, 0, 0], '0'),
    ([], '')
    # ([23, 45, -4], None),
    # ([1.23, 4], None),
    # (['a'], None)
]

for input_num, expected_output in test_cases:
    assert merge_nums(input_num) == expected_output

a = [[1, 5], [2, 4], [1, 4]]
a = sorted(a, key=lambda x: (x[1], -x[0]))
print(a)
