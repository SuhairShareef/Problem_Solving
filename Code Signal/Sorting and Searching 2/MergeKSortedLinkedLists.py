class Node:
    def __init__(self, data): 
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
    
    result = None
    
    if list1.data <= list2.data:
        result = list1
        result.next = merge(list1.next, list2)
    else:
        result = list2
        result.next = merge(list1, list2.next)
    
    return result



def mergeLists(arr):
        if len(arr) == 0:
            return []
        
        if len(arr) == 1:
            return arr[0]
        
        k = len(arr) - 1
        
        while(k != 0):
            i = 0
            j = k
            
            while(i < j):
                arr[i] = merge(arr[i], arr[j])

                i += 1
                j -= 1
                
            if i >= j:
                k = j
        
        return arr[0]



def test():
    lists = [0,0,0]
    # List 1
    lists[0] = Node(1)
    lists[0].next = Node(3)
    lists[0].next.next = Node(5)
    lists[0].next.next.next = Node(7)

    # List 2
    lists[1] = Node(2)
    lists[1].next = Node(4)
    lists[1].next.next = Node(6)
    lists[1].next.next.next = Node(8)

    # List 3
    lists[2] = Node(0)
    lists[2].next = Node(9)
    lists[2].next.next = Node(10)
    lists[2].next.next.next = Node(11)

    head = mergeLists(lists)
    printList(head)

test()