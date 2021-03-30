# 双链表
# 节点类


class Lnode2:
    def __init__(self, elem, next_=None, prev=None):
        self.elem = elem
        self.next_ = next_
        self.prev = prev


# 双链表
# 寻找前面的元素比较困难
class Llist2:
    def __init__(self):
        self._anynode = None

    def is_empty(self):
        return self._anynode is None

    # 添加一个元素到末尾
    def append(self, elem):
        if self._anynode is None:
            p = Lnode2(elem)
            p.next_ = p
            p.prev = p
            self._anynode = p
            return
        p = self._anynode
        q = Lnode2(elem)
        q.next_ = p
        q.prev = p.prev
        p.prev.next_ = q
        p.prev = q
        return

    # 添加一个元素到头前
    def preappend(self, elem):
        if self._anynode is None:
            p = Lnode2(elem)
            p.next_ = p
            p.prev = p
            self._anynode = p
            return
        p = self._anynode
        q = Lnode2(elem)
        q.next_ = p
        q.prev = p.prev
        p.prev.next_ = q
        p.prev = q
        self._anynode = q
        return

    # 链表的长度
    def length(self):
        pass

    # 插入到位置i
    def insert(self, elem, i):
        pass

    # 打印全部
    def printall(self):
        p = self._anynode
        q = self._anynode
        while p is not None:
            print(p.elem)
            p = p.next_
            if p == q:
                break

    # 遍历元素 生成器迭代器
    def get_elements(self):
        pass

    # 逆置
    def reverse(self):
        pass

    # 插入排序
    def mysort(self):
        nsort = self._anynode.next_
        while nsort is not self._anynode:
            x = nsort.elem
            p = nsort.prev
            while p is not self._anynode.prev and p.elem > x:
                p.next_.elem = p.elem
                p.elem = x
                p = p.prev
            nsort = nsort.next_

    # 快速排序
    def _sort_helper(self, leftnode, rightnode):
        if self._anynode is None:
            return
        x = leftnode.elem
        while leftnode != rightnode:
            while rightnode is not self._anynode.prev and rightnode.elem >= x:
                rightnode = rightnode.prev
            if leftnode != rightnode:
                leftnode.elem = rightnode.elem
                leftnode = leftnode.next_
            while leftnode is not self._anynode.prev and leftnode.elem <= x:
                leftnode = leftnode.next_
            if leftnode != rightnode:
                rightnode.elem = leftnode.elem
                rightnode = rightnode.prev
        leftnode.elem = x
        return leftnode

    def quick_sort(self):
        if self._anynode is None:
            return


def main():
    llist = Llist2()
    for i in range(10):
        llist.preappend(i)
    llist.printall()
    llist.mysort()
    print("sorted")
    llist.printall()


if __name__ == '__main__':
    main()
