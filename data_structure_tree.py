

# 优先队列 堆实现
# 建堆 插入数据 获取顶部元素
class MFqueue:
    def __init__(self, llist):
        self._elist = list(llist)
        print(self._elist)
        if llist:
            self.buildheap()
            print(self._elist)

    def is_empty(self):
        return not self._elist

    # 两个子堆上添加一个元素 两个子树是堆
    def shifdown(self, elem, begin, end):
        elist, i, j = self._elist, begin, 2*begin+1
        while j < end:
            if j+1 < end and elist[j+1] < elist[j]:
                j += 1
            if elem < elist[j]:
                break
            elist[i] = elist[j]
            i, j = j, 2*j+1
        elist[i] = elem

    def dequeue(self):
        if not self._elist:
            raise Exception('empty')
        elist = self._elist
        e0 = elist[0]
        e = elist.pop()
        if len(elist) > 0:
            self.shifdown(e, 0, len(elist))
        return e0

    # 上推 下标从0开始
    def enqueue(self, elem):
        last = len(self._elist)
        elist, i, j = self._elist, last, (last-1)//2
        self._elist.append(None)
        while i > 0 and elem < elist[j]:
            elist[i] = elist[j]
            i, j = j, (j-1)//2
        elist[i] = elem

    # 从len(list)//2
    def buildheap(self):
        elist = self._elist
        end = len(self._elist)
        for i in range(end//2, -1, -1):
            self.shifdown(elist[i], i, end)


class Binarytree:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right

    # 递归 先根序
    def dlr_get(self):
        pass


def main():
    a = MFqueue([6, 5, 4, 3, 2, 1])
    a.enqueue(100)
    while not a.is_empty():
        print(a.dequeue())


if __name__ == '__main__':
    main()
