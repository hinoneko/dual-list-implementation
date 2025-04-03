from array_list import ArrayList


def demonstrate_list_operations(list_impl):
    print(f"Demonstrating {list_impl.__class__.__name__}")
    print("Initial list:", list_impl)
    
    # Append
    list_impl.append('a')
    list_impl.append('b')
    list_impl.append('c')
    print("After append a, b, c:", list_impl)
    
    # Insert
    list_impl.insert('x', 1)
    print("After insert x at position 1:", list_impl)
    
    # Get
    print("Element at position 2:", list_impl.get(2))
    
    # Delete
    deleted = list_impl.delete(0)
    print(f"Deleted element at position 0: {deleted}, list now:", list_impl)
    
    # DeleteAll
    list_impl.append('b')
    print("Before deleteAll b:", list_impl)
    list_impl.deleteAll('b')
    print("After deleteAll b:", list_impl)
    
    # Clone
    cloned = list_impl.clone()
    print("Cloned list:", cloned)
    
    # Reverse
    list_impl.reverse()
    print("After reverse:", list_impl)
    
    # FindFirst/FindLast
    list_impl.append('a')
    list_impl.append('x')
    list_impl.append('a')
    print("List with multiple 'a':", list_impl)
    print("First 'a' at:", list_impl.findFirst('a'))
    print("Last 'a' at:", list_impl.findLast('a'))
    
    # Extend
    other_list = list_impl.clone()
    list_impl.extend(other_list)
    print("After extend with clone:", list_impl)
    
    # Length
    print("Current length:", list_impl.length())
    
    # Clear
    list_impl.clear()
    print("After clear:", list_impl)

    # Length after clear
    print("Length after clear:", list_impl.length())

if __name__ == "__main__":
    print("=== Array List Implementation ===")
    demonstrate_list_operations(ArrayList())
