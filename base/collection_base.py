# encoding: utf-8
# ---------------------------------------- #
# Question 1 计算列表中各元素出现的次数
# ---------------------------------------- #

# Solution 1 普通方法
list_example = ['a', 'b', 'b', 'b', 'c']
dict_result = {}
for x in list_example:
    if x not in dict_result:
        dict_result[x] = 1
    else:
        dict_result[x] += 1
        print(dict_result)

# Solution 2 defaultdict函数
# 使用collection模块的公共函数defaultdict函数 缩减代码量
# defaultdict函数接受函数作为参数 例如int函数或者lambda: 0
# defaultdict函数返回一个可迭代对象 操作类似于字典
from collections import defaultdict
dict_result_v2 = defaultdict(lambda: 0)
for x in list_example:
    dict_result_v2[x] += 1

print(dict_result_v2)
print(dict(dict_result_v2))
for x, y in dict_result_v2.items():
    print(x, y)

# Solution 3 列表函数count
dict_result_v3 = {x: list_example.count(x) for x in list_example}
print(dict_result_v3)

# Solution 4 Counter计数器函数
# 使用collections模块的Counter计数器函数
# Counter函数返回可迭代对象 操作类似于字典
# 但有类似于列表的合并操作 + 共有项计算相加
# 也有类似于集合的交&（共有项取计数小者） 并|（共有项取计数大者）差-（出现在第一个Counter但不出现在第二个Counter）
from collections import Counter
dict_result_v4 = Counter(list_example)
print(dict(dict_result_v4))

list_example_v2 = ['b', 'b', 'c', 'd']
dict_result_v4_2 = Counter(list_example_v2)
print(dict_result_v4 + dict_result_v4_2)
print(dict_result_v4 - dict_result_v4_2)
print(dict_result_v4 & dict_result_v4_2)
print(dict_result_v4 | dict_result_v4_2)