def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    rList = [-1]*2;
    
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                rList[0] = i;
                rList[1] = j;
                return rList;

if __name__ == '__main__':
    nums = [2, 7, 11, 15];
    target = 9;
    print(twoSum(nums, target));