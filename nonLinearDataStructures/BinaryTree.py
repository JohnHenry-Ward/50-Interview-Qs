class TreeNode:
    def __init__(self, data):
        self.data  = data;
        self.left  = None;
        self.right = None;
    
class BinaryTree:
    def __init__(self):
        self.root = None;

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left);
            print(node.data);
            self.inOrder(node.right);