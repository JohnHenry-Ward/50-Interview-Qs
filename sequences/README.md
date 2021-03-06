### [Two Sum](https://leetcode.com/problems/two-sum/)
First solution: start at index i=0 and j=i+1, check if i+j=target. Once it does, return. Runtime: O(n^2), first loop complexity is O(n), second loop complexity is n(n-1)/2 ie. times (n-1) + (n-2) + ... + 1, which simplifies to O(n).

Second solution: add nums to dictionary for O(1) lookup. Walk through nums and calculate what second value needs to be and check if it exists. O(n) time complexity because of dictionary hashing

Third solution: rather than store the number as the value in the dictionary, store the index to make sure the numbers are not the same. Runtime: O(n)

### [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
First solution: start at index i=0 and j=i+1, check if they ever match. Runtime: o(n^2)

Second solution: check if num is in dictionary, if no, add it, if yes, we have a duplicate. Runtime: O(n)

Bonus solution: could sort, then see if any nums match those next to it. Runtime: O(nlogn)

### [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/)
First solution: check every possibly pairing to find the max profit. Runtime: O(n^2)

Second Solution: track the min value and continue to compare that to rest of prices, the min value will always be the best possible day to buy stock. Runtime: O(n)

### [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
First solution: use a dictionary, keys are chars in s, values are count of those characters, then walk through t and check if it exists in dictionary, decrementing count if it does. Finally, make sure all counts are 0. Runtime: O(mn), n = length of s, m = length of t

### [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/submissions/)
First solution: use a stack to track the brackets. If the current bracket is an open one, push on to stack. If it is a closing one, make sure that a) the stack is non empty, b) the top of the stack (that we have popped) is a closing bracket, and c) the two brackets go together (by comparing the indexes). Once we walk through s, make sure that the stack is empty. Runtime: O(n) Memory: O(n) all of s could be pushed into the stack

### [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/submissions/)
First solution: walk through nums, each time calculating the product by walking through nums. Runtime: O(n^2)

Second solution: calculate the sum to the left of a number n, and to the right of n. Then multiply each of those together to find the product of all nums except n. Runtime: O(n+n+n) = O(n) Memory: O(2n) = O(n) because of tracking left and right products (using external arrays)

Might be good to re-visit this one

### [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/submissions/)
First solution: track the currMax and keep a runMax. Runmax tracks the running total as long as it is above 0, If runMax < 0, reset to 0. If runMax > currMax, update currMax to runMax. This is Kadane's algorithm (I got about 80% of it)

Might be good to re-visit this one

### [3 Sum](https://leetcode.com/problems/3sum/submissions/)
First solution: brute force check all possible triplets. Runtime: O(n^3)

Second solution: fix a value (i) and then have a low and high pointer mover towards each other. Nums must be sorted. Runtime: O(n^2)

Might be good to re-visit this one

### [Merge Intervals](https://leetcode.com/problems/merge-intervals/submissions/)
First solution: sort intervals by starting value, walk through intervals, add intervals that don't overlap, update most recently added interval that does overlap. Runtime: O(nlogn) bc of sorting

Easy to understand solution, difficult to come up with

### [Group Anagrams](https://leetcode.com/problems/group-anagrams/submissions/)
First solution: store the anagrams in a dictionary with the values being where they are stored in the results array. If it already exists in dictrionary, append to results, other wise, add to dictionary then add to results. Runtime: O(nlogn)

### [Maximum Product Subarray]()
### [Search in Rotated Sorted Array]()