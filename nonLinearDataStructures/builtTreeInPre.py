from BinaryTree import BinaryTree, TreeNode;

def buildTreeSol1(preorder, inorder):
    # preorder gives us the root of a subtree 
        # inorder gives us the left and right subtrees around the root
        
    if not preorder or not inorder:
        return None;

    if len(preorder) == 1:
        return TreeNode(preorder[0]);
    
    root = TreeNode(preorder[0]);
    rootIndex = inorder.index(preorder[0]);

    # left and right subtrees should always have the same values in them
    root.left  = buildTreeSol1(preorder[1:rootIndex + 1], inorder[:rootIndex]);
    root.right = buildTreeSol1(preorder[rootIndex + 1:], inorder[rootIndex + 1:]);
    
    return root;

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7];
    inorder =  [9, 3, 15, 20, 7];

    BT = BinaryTree();
    root = buildTreeSol1(preorder, inorder);
    BT.inOrder(root);