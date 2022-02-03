def maxSubArraySol1(nums):
        currMax = float('-inf');
        runMax = 0;
        for i in range(len(nums)):
            runMax += nums[i];
            if (runMax > currMax):
                currMax = runMax;
            if (runMax < 0):
                runMax = 0;
            
        return currMax;

if __name__ == '__main__':
    nums = [8, -19, 5, -4, 20];
    print(maxSubArraySol1(nums));