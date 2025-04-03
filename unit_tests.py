import unittest
from doubly_linked_list import DoublyLinkedList


class TestListImplementations(unittest.TestCase):
    def _test_implementation(self, list_class):
        # Test empty list
        lst = list_class()
        self.assertEqual(lst.length(), 0)
        
        # Test append
        lst.append('a')
        lst.append('b')
        self.assertEqual(lst.length(), 2)
        
        # Test get
        self.assertEqual(lst.get(0), 'a')
        self.assertEqual(lst.get(1), 'b')
        
        # Test insert
        lst.insert('x', 1)
        self.assertEqual(lst.get(1), 'x')
        self.assertEqual(lst.length(), 3)
        
        # Test delete
        deleted = lst.delete(0)
        self.assertEqual(deleted, 'a')
        self.assertEqual(lst.length(), 2)
        
        # Test deleteAll
        lst.append('x')
        lst.append('y')
        lst.deleteAll('x')
        self.assertEqual(lst.length(), 2)
        self.assertEqual(lst.get(0), 'b')
        
        # Test clone
        cloned = lst.clone()
        self.assertEqual(cloned.length(), lst.length())
        cloned.append('z')
        self.assertNotEqual(cloned.length(), lst.length())
        
        # Test reverse
        lst.clear()
        lst.append('1')
        lst.append('2')
        lst.append('3')
        lst.reverse()
        self.assertEqual(lst.get(0), '3')
        self.assertEqual(lst.get(1), '2')
        self.assertEqual(lst.get(2), '1')
        
        # Test findFirst/findLast
        lst.append('2')
        self.assertEqual(lst.findFirst('2'), 1)
        self.assertEqual(lst.findLast('2'), 3)
        
        # Test extend
        other = list_class()
        other.append('a')
        other.append('b')
        lst.extend(other)
        self.assertEqual(lst.length(), 6)
        self.assertEqual(lst.get(4), 'a')
        
        # Test clear
        lst.clear()
        self.assertEqual(lst.length(), 0)
        
        # Test exceptions
        with self.assertRaises(IndexError):
            lst.get(0)
        with self.assertRaises(ValueError):
            lst.append('ab')
    
    def test_doubly_linked_list(self):
        self._test_implementation(DoublyLinkedList)

if __name__ == '__main__':
    unittest.main()
