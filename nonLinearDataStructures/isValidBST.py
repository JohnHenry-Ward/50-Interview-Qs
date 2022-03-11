from BinaryTree import TreeNode;

def isValidBSTSol1(root):
    return isValidBSTHelper(root, float('-inf'), float('inf'));

def isValidBSTHelper(node, lowerLimit, upperLimit):
    if node is None:
        return True;
    
    if node.data <= lowerLimit or node.data >= upperLimit:
        return False;
    
    return isValidBSTHelper(node.left, lowerLimit, node.data) and isValidBSTHelper(node.right, node.data, upperLimit);

if __name__ == '__main__':
    root = TreeNode(5);
    node1 = TreeNode(1);
    node2 = TreeNode(7);
    node3 = TreeNode(3);
    node4 = TreeNode(9);
    node5 = TreeNode(8);
    node6 = TreeNode(10);
    root.left = node1;
    root.right = node2;
    node2.left = node3;
    node2.right = node4;
    node4.left = node5;
    node4.right = node6;
    print(isValidBSTSol1(root));