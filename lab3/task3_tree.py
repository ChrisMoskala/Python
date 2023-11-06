import unittest


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def __str__(self):
        if self.left:
            self.left.__str__()
        print(self.data),
        if self.right:
            self.right.__str__()

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    @property
    def min_value(self):
        if self.left is None:
            return self.data
        return self.left.min_value


root = Node(19)
root.insert(15)
root.insert(35)
root.insert(12)
root.insert(19)
root.insert(31)
root.insert(42)
# print(min(root.inorderTraversal(root)))
# root.__str__()
min_value = root.min_value
print("Minimum value of the tree:", min_value)


class Testowa(unittest.TestCase):
    def testowanie(self):
        korzen = Node(19)
        korzen.insert(15)
        korzen.insert(35)
        print(korzen.inorderTraversal(korzen))
        self.assertEqual(korzen.inorderTraversal(korzen), [15, 19, 35], "doesn't work")


if __name__ == "__main__":
    unittest.main()
