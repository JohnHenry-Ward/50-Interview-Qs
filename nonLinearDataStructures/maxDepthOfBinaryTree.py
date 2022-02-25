from BinaryTree import BinaryTree;
from BinaryTree import TreeNode;

def maxDepthOfBinaryTreeSol1(root):
    return traverse(root, 0);

def traverse(node, depth):
    if node != None:
        depth+=1;
        return max(traverse(node.left, depth), traverse(node.right, depth));
    else:
        return depth;

if __name__ == '__main__':
    BT = BinaryTree();
    head = TreeNode(3);
    node1 = TreeNode(9);
    node2 = TreeNode(20);
    node3 = TreeNode(15);
    node4 = TreeNode(7);
    head.left = node1;
    head.right = node2;
    node2.left = node3;
    node2.right = node4;
    BT.inOrder(head);
    print(maxDepthOfBinaryTreeSol1(head));


