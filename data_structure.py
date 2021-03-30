# 链表
# 节点类


class Lnode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


# 单链表
# 寻找前面的元素比较困难
class Llist:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    # 添加一个元素到末尾
    def append(self, elem):
        if self._head is None:
            self._head = Lnode(elem)
            return
        p = self._head
        while p.next_ is not None:
            p = p.next_
        p.next_ = Lnode(elem)

    def preappend(self, elem):
        self._head = Lnode(elem, self._head)

    # 链表的长度
    def length(self):
        p, ll = self._head, 0
        while p is not None:
            ll += 1
            p = p.next_
        return ll

    # 插入到位置i
    def insert(self, elem, i):
        if i == 0 and self._head is not None:
            self._head = Lnode(elem, self._head)
            return
        p, n = self._head, 0
        q = None
        while p is not None:
            if n == i:
                q.next_ = Lnode(elem, p)
                return
            q = p
            p = p.next_
            n += 1
        if i == n:
            q.next_ = Lnode(elem, p)
            return
        else:
            raise IndexError("错误位置")

    # 打印全部
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next_ is not None:
                print(', ', end='')
            p = p.next_

    # 遍历元素 生成器迭代器
    def get_elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next_

    # 逆置
    def reverse(self):
        # p遍历原链表
        # q构造新链表
        p, q, temp = self._head, None, None
        while p is not None:
            temp = p
            p = p.next_
            temp.next_ = q
            q = temp
        self._head = q

    # 插入排序
    def mysort(self):
        if self._head is None:
            return
        nsort = self._head.next_
        while nsort is not None:
            x = nsort.elem
            p = self._head
            while p is not nsort and p.elem <= x:
                p = p.next_
            while p is not nsort:
                y = p.elem
                p.elem = x
                x = y
                p = p.next_
            nsort.elem = x
            nsort = nsort.next_




def main():
    llist = Llist()
    for i in range(10):
        llist.append(i)
    llist.insert(100, 10)
    llist.printall()
    llist.reverse()
    llist.printall()


if __name__ == '__main__':
    main()
