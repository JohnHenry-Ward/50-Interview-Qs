def containsDuplicateSol1(nums): # O(n^2)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
        
    return False

def containsDuplicateSol2(nums): # O(n)
    myDict = dict();
    for num in nums:
        if num in myDict:
            return True;
        myDict[num] = num;
    
    return False;

if __name__ == '__main__':
    nums = [1, 2, 3, 1];
    print(containsDuplicateSol1(nums));
    print(containsDuplicateSol2(nums));