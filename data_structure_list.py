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
        self._length = 0

    def is_empty(self):
        return self._anynode is None

    # 添加一个元素到末尾
    def append(self, elem):
        if self._anynode is None:
            p = Lnode2(elem)
            p.next_ = p
            p.prev = p
            self._anynode = p
            self._length += 1
            return
        p = self._anynode
        q = Lnode2(elem)
        q.next_ = p
        q.prev = p.prev
        p.prev.next_ = q
        p.prev = q
        self._length += 1
        return

    # 添加一个元素到头前
    def preappend(self, elem):
        if self._anynode is None:
            p = Lnode2(elem)
            p.next_ = p
            p.prev = p
            self._anynode = p
            self._length += 1
            return
        p = self._anynode
        q = Lnode2(elem)
        q.next_ = p
        q.prev = p.prev
        p.prev.next_ = q
        p.prev = q
        self._anynode = q
        self._length += 1
        return

    # 链表的长度
    def length(self):
        return self._length

    # 插入到位置i
    def insert(self, elem, i):
        pass

    # 打印全部
    def printall(self):
        p = self._anynode
        q = self._anynode
        while p is not None:
            print(p.elem, end=', ')
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

    def get_i(self, i=0):
        if i >= self._length or self._anynode is None:
            return None
        p, n = self._anynode, 0
        while n < i+1:
            if n == i:
                return p
            n += 1
            p = p.next_

    def sort_helper(self, left, right):
        head = self._anynode
        if head is None:
            return
        leftnode, rightnode = self.get_i(left), self.get_i(right)
        x = leftnode.elem
        while left < right:
            while left < right and rightnode.elem >= x:
                rightnode = rightnode.prev
                right -= 1
            if left < right:
                leftnode.elem = rightnode.elem
                leftnode = leftnode.next_
                left += 1
            while left < right and leftnode.elem <= x:
                leftnode = leftnode.next_
                left += 1
            if left < right:
                rightnode.elem = leftnode.elem
                rightnode = rightnode.prev
                right -= 1
        leftnode.elem = x
        return left

    # 快速排序
    def quick_sort(self, left, right):
        if left >= right:
            return
        mid = self.sort_helper(left, right)
        self.quick_sort(left, mid-1)
        self.quick_sort(mid+1, right)


# 基于list的栈
# 入栈 出栈 空栈
class Mstack:
    def __init__(self):
        self._elem = []

    def push(self, elem):
        self._elem.append(elem)

    def pop(self):
        if not self._elem:
            raise Exception("stack is empty")
        return self._elem.pop()

    def is_empty(self):
        return not self._elem


# 基于链表的队列
# 入队 出队 队空
class Lnode:
    def __init__(self, elem=None, next_=None):
        self.elem = elem
        self.next_ = next_


class Mqueue:
    def __init__(self):
        self._head = None
        self._rear = None

    def enqueue(self, elem):
        if not self._head:
            node = Lnode(elem)
            self._head = node
            self._rear = node
            return
        node = Lnode(elem)
        self._rear.next_ = node
        self._rear = node

    def dequeue(self):
        if not self._head:
            raise Exception('queue is empty')
        ee = self._head.elem
        self._head = self._head.next_
        return ee

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next_ is not None:
                print(', ', end='')
            p = p.next_


def main():
    # llist = Llist2()
    # for i in range(5):
    # llist.preappend(i)
    # llist.printall()
    # print("\n")
    # llist.quick_sort(0, llist.length()-1)
    # llist.printall()
    mqueue = Mqueue()
    for i in range(5):
        print(i)
        mqueue.enqueue(i)
    for j in range(5):
        print(mqueue.dequeue())
    mqueue.printall()


if __name__ == '__main__':
    main()
