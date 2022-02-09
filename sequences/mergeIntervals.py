def mergeIntervalsSol1(intervals):
    result = [];
    intervals.sort(); # sort the intervals by the start value of each interval
    result.append(intervals[0]); # add the first interval
    
    for curr in intervals[1:]: # for each interval, starting at the second one
        if (result[-1][1] >= curr[0]): # if there is overlap (result[-1] will always be the most recent interval added)
            result[-1][1] = max(result[-1][1], curr[1]); # update the most recent interval to end at the larger value
        else:
            result.append(curr); # add the new interval that hasn't yet overlapped
            
    return result;

if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]];
    print(mergeIntervalsSol1(intervals));