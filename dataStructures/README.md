### [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/submissions/)
First solution: 3 pointers, prev, curr, and nxt. Walk done LL until curr is null, return curr (which is the new head). Runtime: O(n)

### [Detect Cycle in a Linked List](https://leetcode.com/problems/linked-list-cycle/submissions/)
First solution: 2 pointers, one fast and one slow, move slow one node at a time, move fast 2 nodes at a time. If they ever equal, we have a cycle, if fast is ever None, we don't have a cycle. Runtime: O(n)

Second soltuion: same as first, just cleaner

### [Container with Most Water](https://leetcode.com/problems/container-with-most-water/submissions/)
First solution: check every possible combo with two pointers. Runtime: O(n^2)

Second solution: have one pointer on the very left and one on the very right. Track maxArea, move the smaller pointer closer to center until they meet. Runtime: O(n)

### [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/)
First solution: sudo binary search. Find the middle element and see if it is larger than the first element. If so, the min is to the right, otherwise it's to the left. Divide array in half and continue. Runtime: O(logn)

### [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/)
First solution: check all possible using hash table. Runtime: O(n^2)

Second solution: use a dictionary to track when we last saw a character, and use 2 pointers, i and j, to track the current subsequence. Runtime: O(n)

### [Longest Substring without Repeating Characters]()
### [Minimum Window Substring]()
### [Number of Islands]()
### [Remove nth Node from End of List]()
### [Palindromic Substrings]()
### [Pacific Atlantic Water Flow]()
