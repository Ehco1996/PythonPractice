'''
Python版
链表的实现
'''


class Node(object):
    def __init__(self, element=-1):
        self.element = element
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.head.next = None

    # O（1)
    def is_empty(self):
        return self.head is None

    def length(self):
        index = 0
        node = self.head
        while node is not None:
            index += 1
            node = node.next
        return index

    def find(self, element):
        node = self.head
        while node is not None:
            if node.element == element:
                break
            node = node.next
        return node

    def _node_at_index(self, index):
        i = 0
        node = self.head
        while node is not None:
            if i == index:
                return node
            node = node.next
            i += 1
        return None

    def element_at_index(self, index):
        node = self._node_at_index(index)
        return node.element

    # O(n)
    def insert_before_index(self, position, element):
        if position > 0:
            # 找到插入位置的node
            node = self._node_at_index(position - 1)
            new_node = Node(element)
            node.next = new_node
            # 连接上断开的链表
            new_node.next = self._node_at_index(position)
        else:
            new_node = Node(element)
            new_node.next = self.head
            self.head = new_node

    def insert_after_index(self, position, element):
        node = self._node_at_index(position)
        new_node = Node(element)
        new_node.next = node.next
        node.next = new_node

    def first_object(self):
        return self._node_at_index(0)

    def last_object(self):
        return self._node_at_index(self.length() - 1)

    # O(n)
    def append(self, node):
        if self.head is None:
            self.head.next = node
        else:
            last_node = self.last_object()
            last_node.next = node


def log_linkedList(LinkedList):
    for i in range(LinkedList.length()):
        print(LinkedList.element_at_index(i))


def test():
    link = LinkedList()
    link.append(Node(1))
    link.append(Node(2))
    log_linkedList(link)


if __name__ == '__main__':
    test()
