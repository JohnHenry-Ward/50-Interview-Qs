def productExceptSelfSol1(nums):
    result = [];
    currIndex = 0;
    while (currIndex < len(nums)): # O(n)
        product = 1;
        for nIndex in range(len(nums)): # O(n)
            if (currIndex != nIndex):
                product *= nums[nIndex];
        result.append(product);
        currIndex+=1;

    return result;

def productExceptSelfSol2(nums):
    left = [1]*len(nums);
    right = [1]*len(nums);
    left.append(1);
    
    result = [];
    
    # Calculate left product
    for l in range(1, len(nums)):
        left[l] = left[l-1] * nums[l-1];
    
    # Calculate right product
    for r in range(len(nums)-2, -1, -1):
        right[r] = right[r+1] * nums[r+1];
        
    # Calculate final product
    for n in range(len(nums)):
        result.append(left[n] * right[n]);
        
    return result;

if __name__ == '__main__':
    nums = [1, 2, 3, 4];
    print(productExceptSelfSol1(nums));
    print(productExceptSelfSol2(nums));