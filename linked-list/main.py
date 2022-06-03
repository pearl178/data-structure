class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
a.next = b
b.next = c
c.next = d

# A → B → C → D


def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next


## Recursion
def printLinkedList_(head):
    if head is None:
        return           #Base
    print(head.val)
    printLinkedList_(head.next)


printLinkedList(a)
