class ArrayQueue:
    """
    Queue implementations using array
    Ex: [0,0,0,21,0,1]
        front is the first element in the array
        rear is the last element
    """

    def __init__(self) -> None:
        self.queue = []
        self.size = 0

    def push(self, val: int) -> None:
        self.queue.append(val)
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            print("Queue is empty")
            return -10000000
        self.size -= 1
        return self.queue.pop(0)

    def getRear(self) -> int:
        if self.size == 0:
            print("Queue is empty")
            return -10000000
        return self.queue[-1]

    def getFront(self) -> int:
        if self.size == 0:
            print("Queue is empty")
            return -10000000
        return self.queue[0]

    def isEmpty(self) -> bool:
        return self.size == 0

    def __repr__(self) -> str:
        if self.size == 0:
            print("Queue is empty")
        return self.queue


class Node:
    """
    Node Class
    """

    def __init__(self, val: int = None) -> None:
        self.val = val
        self.next = None


class LLQueue:
    """
    Queue implementations using linked list
    Ex: 0->0->0->21->0->1->None
        front is the first element in the list
        rear is the last element
    """

    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0

    def push(self, val: int) -> None:
        newNode = Node(val)
        if self.size == 0:
            self.front = self.rear = newNode

        else:
            self.rear.next = newNode
            self.rear = newNode

        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            print("Queue is empty")
            return -10000000

        val = self.front.val
        self.front = self.front.next

        if self.size == 1:
            self.rear = None
        self.size -= 1
        return val

    def getRear(self) -> int:
        if self.rear is not None:
            return self.rear.val

        print("Queue is empty")
        return -10000000

    def getFront(self) -> int:
        if self.front is not None:
            return self.front.val

        print("Queue is empty")
        return -10000000

    def isEmpty(self) -> bool:
        return self.size == 0

    def __repr__(self) -> str:
        currentNode = self.front
        result = "["
        while currentNode is not None:
            result += str(currentNode.val) + ", "
            currentNode = currentNode.next

        result += "]"
        if result == "[]":
            return "Queue is empty"
        return result

def test():
    print("Array queue:")
    queue = ArrayQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    print(queue.__repr__())

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.__repr__())

    print("\nLinked list queue:")
    queue = LLQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    print(queue.__repr__())

    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.__repr__())


test()