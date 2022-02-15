import math;

def minInRotatedArraySol1(nums):
    if len(nums) == 1:
        return nums[0];
    
    left = 0;
    right = len(nums) - 1;
    
    if nums[right] > nums[0]: # array was never rotated
        return nums[0];
    
    while left < right:
        mid = math.floor(left + (right - left)/2);
        
        if nums[mid] < nums[mid-1]: # mid is the min
            return nums[mid];
        if nums[mid] > nums[mid+1]: # mid is the max, which is next to the min
            return nums[mid+1];
        
        if nums[mid] > nums[0]: # min is to the right
            left = mid+1;
        else:
            right = mid-1; # min is to the left




if __name__ == '__main__':
    nums = [5,6,7,8,9,2,3];
    print(minInRotatedArraySol1(nums));