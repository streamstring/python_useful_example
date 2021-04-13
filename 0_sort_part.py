# 插入排序 直接插入排序
def insert_sort(a):
    b = 0
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            continue
        b = a[i]
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j] = a[j-1]
                a[j-1] = b
            else:
                continue
    return a


# 插入排序 希尔插入排序 1959
def hill_insert_sort(a, n):
    b = 0
    print(n)
    for i in range(0, n):
        for ii in range(i+n, len(a), n):
            if a[ii] >= a[ii-n]:
                continue
            b = a[ii]
            for jj in range(ii, i, -n):
                if a[jj-n] > a[jj]:
                    a[jj] = a[jj-n]
                    a[jj-n] = b
                else:
                    continue
        print(a)
    return a


# 插入排序 希尔排序 希尔插入排序
def hill_sort(a, steps=(5, 3, 1)):
    for x in steps:
        a = hill_insert_sort(a, x)
    return a


# 交换排序 上升法冒泡排序
def bubble_sort(aa):
    a = list(aa)
    temp = 0
    for i in range(0, len(a)-1):
        # 上升法
        flag = 0
        for j in range(len(a)-1, i, -1):
            if a[j] >= a[j-1]:
                continue
            else:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
                flag = 1
        if not flag:
            # 假如没有交换 则代表有序 直接返回
            break
    return a


# 交换排序 快速排序 Hoare 霍尔 1960
def hoare_partition(a, s, e):
    ttemp = a[s]
    i, j = s, e
    while i < j:
        while i < j and a[j] >= ttemp:
            j -= 1
        if i < j:
            a[i] = a[j]
            i += 1
        while i < j and a[i] <= ttemp:
            i += 1
        if i < j:
            a[j] = a[i]
            j -= 1
    a[i] = ttemp
    return i


def exchange_sort(a, s, e):

    pass


# 堆排序
def heap_sort(hlist):
    pass


if __name__ == '__main__':
    aa = [5, 1, 2, 3, 4, 100, 999, 100, 9, 7, 4, 2]
    # print(insert_sort(aa))
    # hill_sort(aa)
    # bubble_sort(aa)
    hoare_partition(aa, 0, len(aa)-1)
    print(aa)
