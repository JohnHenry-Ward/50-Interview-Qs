def threeSumSol1(nums): # O(n^3)
    result = [];

    if (len(nums) < 3):
        return result;

    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if (nums[i] + nums[j] + nums[k] == 0):
                    triplet = [nums[i], nums[j], nums[k]];
                    triplet.sort();
                    if triplet not in result:
                        result.append(triplet);

    return result;

    
def threeSumSol2(nums): # O(n^2)
    result = [];
    
    if (len(nums) < 3):
        return result;
    
    nums.sort(); # nums must be sorted for this to work
    
    for i in range(len(nums)-2):
        if (i == 0 or (i > 0 and nums[i] != nums[i-1])): # make sure i is 0 or that i is greater than 0 and the previous nums[i] is not the same value to avoid duplicates
            low = i+1;
            high = len(nums)-1;
            target = 0 - nums[i];
            while (low < high):
                if (nums[low] + nums[high] == target): # if the current values of nums[low] and nums[high] sum to the target, add to result
                    result.append([nums[low], nums[high], nums[i]]);
                    while (low < high and nums[low] == nums[low+1]): # get low to the last value that is the same, to avoid duplicates
                        low+=1;
                    while (low < high and nums[high] == nums[high-1]): # get high to the last value that is the same, to avoid duplicates
                        high-=1;
                    low+=1; # get a new low value
                    high-=1; # get a new high value
                elif (nums[low] + nums[high] < target): # the target is larger than the sum, so the low value needs to be larger
                    low+=1;
                else: # the target is smaller, so the high value needs to be smaller
                    high-=1;
            
    
    return result;

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4];
    print(threeSumSol1(nums));
    print(threeSumSol2(nums));