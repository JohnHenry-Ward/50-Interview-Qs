def nonOverlappingInveralsSol1(intervals):
    # we want to keep the intervals that are the smallest (ie the ones with the smaller of the end times)
    
    counter = 0;
    largestEnd = float('-inf');
    intervals = sorted(intervals, key=lambda x: x[1]); # sort the intervals by the end
    
    for i in intervals:
        if i[0] >= largestEnd: # if the current start (i[0]) is larger than the largest end we've seen, then that means we will see a larger end (i[1])
            largestEnd = i[1];
        else:                  # the current start (i[0]) is smaller than the largest end we've seen, meaning that this interval is overlapping something
            counter += 1;
            
    return counter;

if __name__ == '__main__':
    intervals = [[1,2], [2,3], [1,3], [3,4]];
    print(nonOverlappingInveralsSol1(intervals));