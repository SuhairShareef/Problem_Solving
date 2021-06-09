class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    def __init__(self, m: int = 10, maxLoadFactor: int = 0.75):
        self.table = [None] * m
        self.m = m
        self.maxLoadFactor = maxLoadFactor
        self.size = 0
        
    def hash(self, key):                 
        return key % self.m

     
    def put(self, key, value):
        if not self.calcLoadFactor():
            print("Adding more will exceed load factor!")
            return
            
        self.size += 1
        index = self.hash(key)
        newNode = Node(key, value)
        
        if self.table[index] is None:
            self.table[index] = newNode
        
        else:
            current = self.table[index]
            
            while current is not None:
                if current.next == None:
                    current.next = newNode
                    break
                current = current.next
                
                
    def get(self, key):
        index = self.hash(key)
        current = self.table[index]
        
        while current is not None and current.key != key:
		        current = current.next

        if current is None:
            return None
        return current.value
        
        
    def delete(self, key):
        index = self.hash(key)
        current = self.table[index]
        prev = None

        while current is not None and current.key != key:
            prev = current
            current = current.next

        if current is None:
            return None
            
        else:
            self.size -= 1
            result = current.value

            if prev is None:
                current = None
                
            else:
                prev.next = prev.next.next

            return result
    
    
    def calcLoadFactor(self):
        loadFactor = self.size / self.m
        
        if loadFactor > self.maxLoadFactor:
            return False
        return True
    
    def print(self):
        for i in range(self.m):
            print("Index: " + str(i))
            
            if self.table[i] is None:
                print(None)
            else:
                current = self.table[i]
                while current is not None:
                    print(current.key, current.value)
                    current = current.next
        
        
ht = HashTable(10, 0.50)
ht.put(10, 20)
ht.put(0, 0)
ht.put(1, 2)
ht.put(3, 3)
ht.put(13, 4)
ht.put(6, 5)

ht.print()
ht.delete(0)
ht.print()
print(ht.get(6))