# 给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等
def find_wap_values(array1, array2):
    """
    :type array1: List[int]
    :type array2: List[int]
    :rtype: List[int]
    """
    diff = sum(array1) - sum(array2)
    if diff & 1:
        return []
    diff >>= 1
    if len(array1) > len(array2):
        temp = set(array1)
        for y in array2:
            if y + diff in temp:
                return [y + diff, y]
    else:
        temp = set(array2)
        for x in array1:
            if x - diff in temp:
                return [x, x - diff]
    return []


# 给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形，
# 其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)
# 不要求这些单词在清单里连续出现，但要求所有行等长，所有列等高
def max_rectangle(words):
    init = {len(x): list() for x in words}
    for w in words:
        init.get(len(w)).append(w)
    init_sorted_len = sorted(init.keys(), reverse=True)
    for i in range(len(init_sorted_len)-1):
        long = init_sorted_len[i]
        for j in range(i+1, len(init_sorted_len)):
            high = init_sorted_len[j]


# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2
# 请你找出并返回这两个正序数组的 中位数
def find_kth_from_twolist(a, b, k):
    la, lb = len(a), len(b)
    i, j, count = -1, -1, 0
    ans = None
    while count < k:
        if i+1 < la and j+1 < lb and a[i+1] <= b[j+1]:
            i = i+1
            count = count+1
            ans = a[i]
        elif i+1 < la and j+1 < lb and b[j+1] < a[i+1]:
            j = j+1
            count = count+1
            ans = b[j]
        elif i+1 >= la and j+1 < lb:
            j = j+1
            count = count+1
            ans = b[j]
        elif j+1 >= lb and i+1 < la:
            i = i+1
            count = count+1
            ans = a[i]
    return ans



def main():
    a = ["this", "real", "hard", "trh", "hea", "iar", "sld"]
    max_rectangle(a)

    aa = [0, 0]
    bb = [0, 0]

    print(find_kth_from_twolist(aa, bb, 2))


if __name__ == '__main__':
    main()
