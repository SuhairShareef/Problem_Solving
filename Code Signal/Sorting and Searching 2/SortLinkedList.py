class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None


def mergeSort(head: Node):
    if head is None or head.next is None:
        return head
    
    left = head
    right = getMid(head)
    
    list1 = mergeSort(left)
    list2 = mergeSort(right)
    
    return merge(list1, list2)
    

# Getting mid element
def getMid(head: Node) -> Node:
    slow = fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    mid = slow.next
    slow.next = None
    
    return mid
    
    
# Merge lists
def merge(list1, list2):
    if list1 is None and list2 is None:
        return None
        
    elif list1 is None:
        return list2
        
    elif list2 is None:
        return list1
    
    node = None
    if list1.data < list2.data:
        node = list1
        node.next = merge(list1.next, list2)
    else:
        node = list2
        node.next = merge(list1, list2.next)

    return node

def printList(node):
    while (node != None):
        print(node.data, end = " ")
        node = node.next

def test():
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)
    head1.next.next.next = Node(0)
    head1.next.next.next.next = Node(2)

    printList(mergeSort(head1))

test()