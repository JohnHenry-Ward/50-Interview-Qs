def twoSumSol1(nums, target): # O(n^2)
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    rList = [-1]*2;
    
    for i in range(0, len(nums)): # O(n)
        for j in range(i+1, len(nums)): # O(n)
            if (nums[i] + nums[j] == target):
                rList[0] = i;
                rList[1] = j;
                return rList;

def twoSumSol2(nums, target): # O(n)
    rList = [-1]*2;

    myDict = dict();
    for num in nums: # O(n)
        myDict[num] = num;
                
    for iIndex in range(len(nums)): # O(n)
        j = target - nums[iIndex];
        if (j in myDict): # O(1), uses the dicts hashing
            if (nums.index(j) != iIndex): # THIS IS NOT CONSTANT TIME
                rList[0] = iIndex;
                rList[1] = nums.index(j); # O(n) but only runs once
                return rList;

def twoSumSol3(nums, target): # O(n)
    myDict = dict();
    for n in range(len(nums)):
        myDict[nums[n]] = n;
    
    for n in range(len(nums)):
        val = target - nums[n];
        if val in myDict and n != myDict[val]:
            return [n, myDict[val]];

if __name__ == '__main__':
    nums = [2, 7, 11, 15];
    target = 9;
    print(twoSumSol1(nums, target));
    print(twoSumSol2(nums, target));