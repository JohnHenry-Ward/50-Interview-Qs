from BinaryTree import BinaryTree, TreeNode;

def levelOrderTraversalSol1(root):
    return traverse(root, [], 0);

def traverse(node, result, level):
    if node == None: # if the node is empty, go back
        return;
    
    if len(result) <= level: # if we are at a level we haven't been to before
        result.append([int(node.data)]);
    else:
        result[level].append(int(node.data)); # we have already been at this level
        
    traverse(node.left, result, level+1);
    traverse(node.right, result, level+1);
    
    return result;

if __name__ == '__main__':
    BT = BinaryTree();
    root = TreeNode(3);
    node2 = TreeNode(9);
    node3 = TreeNode(20);
    node4 = TreeNode(15);
    node5 = TreeNode(7);
    root.left = node2;
    root.right = node3;
    node3.left = node4;
    node3.right = node5;

    print(levelOrderTraversalSol1(root));