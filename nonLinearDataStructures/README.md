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

### [Non Overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
First solution: Greedy approach, sort the intervals by the end value. Track the largest ending value we've seen, that is what we want to get rid of. Runtime: O(nlogn) for sorting

### [Construct Binary Tree from Preoder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/)
First solution: use preorder to get the root, use inorder to get the subtrees around the root. recursivly build tree. Would be good to come back to this one to get solution on own. Runtime: O(n^2) (could be O(n) if we use a hash table to look up the index).

### [Top K Frequent Elements]()
### [Clone Graph]()
### [Course Schedule]()
### [Serialize and Deserialize Binary Tree]()
### [Binary Tree Maximum Path Sum]()