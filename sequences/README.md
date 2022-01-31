### [x] [Two Sum](https://leetcode.com/problems/two-sum/)
First solution: start at index i=0 and j=i+1, check if i+j=target. Once it does, return. Runtime: O(n^2), first loop complexity is O(n), second loop complexity is n(n-1)/2 ie. times (n-1) + (n-2) + ... + 1, which simplifies to O(n).

Second solution: add nums to dictionary for O(1) lookup. Walk through nums and calculate what second value needs to be and check if it exists. O(n) time complexity because of dictionary hashing

### [ ] [Contains Duplicate]()
### [ ] [Best Time to Buy and Sell Stock]()
### [ ] [Valid Anagram]()
### [ ] [Valid Parenthese]()
### [ ] [Product of Array Except Self]()
### [ ] [Maximum Subarray]()
### [ ] [3 Sum]()
### [ ] [Merge Intervals]()
### [ ] [Group Anagrams]()
### [ ] [Maximum Product Subarray]()
### [ ] [Search in Rotated Sorted Array]()