class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        current = self.root
        traversal = ""
        traversal = self.preorder_print(current, traversal)
        print(traversal)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        current = start
        if (current.value == find_val):
            return True
        elif (current.value != find_val and current.left is not None):
            return self.preorder_search(current.left,find_val)
        elif (current.value != find_val and current.right is not None):
            return self.preorder_search(current.right, find_val)
        else:
            return False

    def preorder_print(self, start, traversal): 
        """Helper method - use this to create a 
        recursive print solution."""
        if start is None:
            return traversal
        traversal += str(start.value)
        if (start.left):
            traversal += '-'
            traversal = self.preorder_print(start.left, traversal)
        if (start.right):
            traversal += '-'
            traversal = self.preorder_print(start.right, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())