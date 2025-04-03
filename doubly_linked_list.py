class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def length(self) -> int:
        return self.size
    
    def append(self, element: str) -> None:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def insert(self, element: str, index: int) -> None:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            new_node = Node(element)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        elif index == self.size:
            self.append(element)
            return
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node = Node(element)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
        self.size += 1
    
    def delete(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.size - 1:
            data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1
        return data
    
    def get(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def deleteAll(self, element: str) -> None:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        
        current = self.head
        while current:
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.size -= 1
            current = current.next
    
    def clone(self) -> 'DoublyLinkedList':
        new_list = DoublyLinkedList()
        current = self.head
        while current:
            new_list.append(current.data)
            current = current.next
        return new_list
    
    def reverse(self) -> None:
        current = self.head
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp
        temp = self.head
        self.head = self.tail
        self.tail = temp
    
    def findFirst(self, element: str) -> int:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        
        current = self.head
        index = 0
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1
    
    def findLast(self, element: str) -> int:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        
        current = self.tail
        index = self.size - 1
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1
    
    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def extend(self, elements: 'DoublyLinkedList') -> None:
        current = elements.head
        while current:
            self.append(current.data)
            current = current.next
            
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return str(elements)
