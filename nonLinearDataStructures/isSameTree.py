from BinaryTree import BinaryTree;
from BinaryTree import TreeNode;

def isSameTreeSol1(p, q):    
    if p == None and q == None: # CASE 1: both p and q are None
        return True;
    
    if p == None or q == None: # CASE 2: one of p or q is None
        return False;
    
    if p.data != q.data: # CASE 3: both p and q have values
        return False;
    
    return isSameTreeSol1(p.left, q.left) and isSameTreeSol1(p.right, q.right);

if __name__ == '__main__':
    BT1 = BinaryTree();
    node1 = TreeNode(1);
    node2 = TreeNode(2);
    node3 = TreeNode(3);
    node1.left = node2;
    node1.right = node3;
    BT1.root = node1;

    BT2 = BinaryTree();
    node4 = TreeNode(1);
    node5 = TreeNode(2);
    node6 = TreeNode(3);
    node4.left = node5;
    node4.right = node6;
    BT2.root = node4;

    print(isSameTreeSol1(BT1.root, BT2.root));