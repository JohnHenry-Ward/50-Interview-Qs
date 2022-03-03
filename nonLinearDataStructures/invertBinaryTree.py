from BinaryTree import BinaryTree;
from BinaryTree import TreeNode;

def invertBinaryTreeSol1(root):
    if root == None:
        return;
    
    temp = root.left;
    root.left = root.right;
    root.right = temp;
    
    invertBinaryTreeSol1(root.left);
    invertBinaryTreeSol1(root.right);
    
    return root;

if __name__ == '__main__':
    BT = BinaryTree();
    root = TreeNode(4);
    node2 = TreeNode(2);
    node3 = TreeNode(7);
    node4 = TreeNode(1);
    node5 = TreeNode(3);
    node6 = TreeNode(6);
    node7 = TreeNode(9);
    root.left = node2;
    root.right = node3;
    node2.left = node4;
    node2.right = node5;
    node3.left = node6;
    node3.right = node7;
    BT.inOrder(root);
    newRoot = invertBinaryTreeSol1(root);
    print('----');
    BT.inOrder(root);