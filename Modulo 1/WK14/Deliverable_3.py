#Class to generate nodes to use for the Binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #Node function to print the binary tree 
    def node_print_tree(self, level=0):
        if self.right:
            self.right.node_print_tree(level + 1)
    
        print(f'Level {level} Node {str(self.data)}')

        if self.left:
            self.left.node_print_tree(level + 1)

#Class to build the binary tree
class BinaryTree:
    def __init__(self):
        self.root = None
    
    #Function to print the binary tree from root and call function on Node
    def print_binary_tree(self):
        if self.root:
            self.root.node_print_tree()
        else:
            print(f'The binary tree is empty')

#Testing enviroment
tree = BinaryTree()

node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')

tree.root = node_a
node_a.left = node_b
node_a.right = node_c
node_b.left = node_d
node_c.right = node_e


tree.print_binary_tree()
