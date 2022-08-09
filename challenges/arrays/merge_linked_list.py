"""Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.
"""
import sys

class SinglyLinkedListNode():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

def mergeLists(head1, head2):
    sys.setrecursionlimit(2000)
    return _mergeLists(head1, head2)

def _mergeLists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    if head1.data < head2.data:
        merge = head1
        merge.next = _mergeLists(head1.next, head2)
    else:
        merge = head2
        merge.next = _mergeLists(head1, head2.next)
    
    return merge

if __name__ == '__main__':
    SG = SinglyLinkedList()
    for i in range(4):
        SG.push(i)