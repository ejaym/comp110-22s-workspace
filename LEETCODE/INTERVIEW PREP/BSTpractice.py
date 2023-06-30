class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val, current=None):
        if current is None:
            current = self.root

        if (current.value > new_val and current.left is not None):
            return self.insert(new_val, current.left)
        elif (current.value < new_val and current.right is not None):
            return self.insert(new_val, current.right)
        elif (current.value > new_val and current.left is None):
            newinsertnode = Node(new_val)
            current.left = newinsertnode
        elif (current.value < new_val and current.right is None):
            newinsertnode = Node(new_val)
            current.right = newinsertnode

    def search(self, find_val, current=None):
        if current is None:
            current = self.root
        if (current.value > find_val and current.left is not None):
            return self.search(find_val, current.left)
        elif (current.value < find_val and current.right is not None):
            return self.search(find_val, current.right)
        elif (current.value == find_val):
            return True
        return False
    

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

