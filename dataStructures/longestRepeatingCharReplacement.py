def longestRepeatingCharReplacementSol1(s, k):
    maxLength = 0; # track the current max substring
    mostFreq = 0;  # track the count of the char that appears the most in the current substring [i, j]
    i = 0;        # the start of the substring
    j = 0;        # the end of the substring (inclusive)
    d = {};       # dictionary to look up current count of each character in substring
        
    while j < len(s): # walk through s
        c = s[j];
        
        # update c in d
        if c in d:
            d[c] += 1;
        else:
            d[c] = 1;
            
        mostFreq = max(mostFreq, d[c]); # mostFreq is either itself or we've now update d[c] to be appearing more often in d
        countOfOtherChars = (j - i + 1) - mostFreq; # count of other characters in substring that are not d[c]
        
        # if we've broken the rule of the substring
        if countOfOtherChars > k:
            d[s[i]] -=1; # decrement the count
            i+=1;        # move the start substring by 1
        
        maxLength = max(maxLength, j - i + 1); # update the length
        
        j+=1; # move to next in s
            
    
    return maxLength;

if __name__ == '__main__':
    s = 'ABAB';
    k = 2;
    print(longestRepeatingCharReplacementSol1(s, k));