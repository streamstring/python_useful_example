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
def bubble_sort(a):
    for i in range(0, len(a)-1):
        for j in range(len(a)-1, i, -1):
            if a[j-1] > a[j]:
                b = a[j]
                a[j] = a[j-1]
                a[j-1] = b
            else:
                continue
        print(a)
    return a


# 交换排序 快速排序 Hoare 霍尔 1960


if __name__ == '__main__':
    aa = [5, 1, 2, 3, 4, 100, 999, 100, 9, 7, 4, 2]
    # print(insert_sort(aa))
    print(aa)
    # hill_sort(aa)
    bubble_sort(aa)
