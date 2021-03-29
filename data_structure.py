# 链表
# 节点类


class Lnode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class Llist:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

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

    def length(self):
        p, ll = self._head, 0
        while p is not None:
            ll += 1
            p = p.next_
        return ll

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

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next_ is not None:
                print(', ', end='')
            p = p.next_


def main():
    llist = Llist()
    for i in range(10):
        llist.append(i)
    llist.insert(100, 11)
    llist.printall()


if __name__ == '__main__':
    main()
