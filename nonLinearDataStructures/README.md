### [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/)
First solution: Traverse tree, keeping track of the depth, and returning the depth once we hit null. Return the max of traversing left and right subtrees. Runtime: O(n)

### [Invert/Flip Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
First solution: Invert (swap children) each subtree of root, left and right child. Recursivly do this for each child.

### [Same Tree](https://leetcode.com/problems/same-tree/)
First solution: Check if current node in p and q are non none, if so, check if they are equal, if so, continue with left and right child recursivly. Runtime: O(n)

### [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
First solution: Use a helper function that tracks the level we are at, if it's a new level, append to result, if it's not append to specific index in result. Runtime: O(n)

### [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
First solution: Keep track of an upper and lower limit that represents the value 2 values that a node has to be between. (would be smart to come back to this one to get a better understanding)

### [Non Overlapping Intervals]()
### [Construct Binary Tree from Preoder and Inorder Traversal]()
### [Top K Frequent Elements]()
### [Clone Graph]()
### [Course Schedule]()
### [Serialize and Deserialize Binary Tree]()
### [Binary Tree Maximum Path Sum]()