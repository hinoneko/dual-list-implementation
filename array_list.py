class ArrayList:
    def __init__(self):
        self.elements = []
    
    def length(self) -> int:
        return len(self.elements)
    
    def append(self, element: str) -> None:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        self.elements.append(element)
    
    def insert(self, element: str, index: int) -> None:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        if index < 0 or index > len(self.elements):
            raise IndexError("Index out of range")
        self.elements.insert(index, element)
    
    def delete(self, index: int) -> str:
        if index < 0 or index >= len(self.elements):
            raise IndexError("Index out of range")
        return self.elements.pop(index)
    
    def deleteAll(self, element: str) -> None:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        self.elements = [e for e in self.elements if e != element]
    
    def get(self, index: int) -> str:
        if index < 0 or index >= len(self.elements):
            raise IndexError("Index out of range")
        return self.elements[index]
    
    def clone(self) -> 'ArrayList':
        new_list = ArrayList()
        new_list.elements = self.elements.copy()
        return new_list
    
    def reverse(self) -> None:
        self.elements.reverse()
    
    def findFirst(self, element: str) -> int:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        try:
            return self.elements.index(element)
        except ValueError:
            return -1
    
    def findLast(self, element: str) -> int:
        if len(element) != 1:
            raise ValueError("Element must be a single character")
        for i in range(len(self.elements)-1, -1, -1):
            if self.elements[i] == element:
                return i
        return -1
    
    def clear(self) -> None:
        self.elements = []
    
    def extend(self, elements: 'ArrayList') -> None:
        self.elements.extend(elements.elements)
    
    def __str__(self):
        return str(self.elements)
    