class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


def printList(node):
    while (node != None):
        print(node.data, end = " ")
        node = node.next
 
 
def merge(list1: Node, list2: Node) -> Node:
    if list1 is None:
        return list2
    
    if list2 is None:
        return list1
        
    if (list1.data < list2.data):
        list1.next = merge(list1.next, list2)
        return list1
     
    else:
        list2.next = merge(list1, list2.next)
        return list2


def main():
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)
 
    # 1.3.5 LinkedList created
    head2 = Node(0)
    head2.next = Node(2)
    head2.next.next = Node(4)
        
    printList(head1)
    print()
    printList(head2)
    print()

    # 0.2.4 LinkedList created
    mergedhead = merge(head1, head2)
    printList(mergedhead)


main()