class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def in_order_traversal(self):
        elements = []
        self._in_order_recursive(self.root, elements)
        return elements

    def _in_order_recursive(self, node, elements):
        if node:
            self._in_order_recursive(node.left, elements)
            elements.append(node.value)
            self._in_order_recursive(node.right, elements)

# Dizi ve ağaç oluşturma
dizi = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
bst = BinarySearchTree()
for eleman in dizi:
    bst.insert(eleman)

# In-order sıralı çıktı
print("In-order Traversal:", bst.in_order_traversal())