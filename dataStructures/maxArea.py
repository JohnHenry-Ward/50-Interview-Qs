def maxAreaSol1(height):
    maxWater = 0;
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            w = j - i;
            h = min(height[i], height[j]);
            maxWater = max(maxWater, w * h);
            
    return maxWater;


def maxAreaSol2(height):
    i = 0;
    j = len(height)-1;
    maxWater = 0;
    while i < j:
        w = j - i;
        h = min(height[i], height[j]);
        maxWater = max(maxWater, w * h);
        if height[i] < height[j]:
            i+=1;
        else:
            j-=1;
        
    return maxWater;

if __name__ == '__main__':
    height = [2,3,4,5,18,17,6];
    print(maxAreaSol1(height)); 
    print(maxAreaSol2(height)); 