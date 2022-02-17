def lengthOfLongestSubStringSol1(s):
    if s == '':
        return 0;
    
    currMax = 0;
    possMax = [];
    pointer = 0;
    d = {};
    
    while pointer < len(s):
        for index in range(pointer, len(s)):
            c = s[index];
            if c not in d:
                currMax +=1;
                d[c] = c;
            else:
                d.clear();
                possMax.append(currMax);
                d[c] = c;
                currMax = 1;
        possMax.append(currMax);
        pointer +=1;
        d.clear();
        currMax = 0;
        
    return max(possMax);

def lengthOfLongestSubStringSol2(s):
    currMax = 0;
    d = {};
    i = 0;
    
    for j in range(len(s)):
        if s[j] in d: # if we have seen s[j] before
            if i < d[s[j]]: # if s[j] is in the current sequence
                i = d[s[j]]; # we need to move i up to the start of a new non repeating sequence, meaning that we move it right after we saw s[j] the previous time
        
        currMax = max(currMax, j-i+1); # currMax gets max of itself or of the current sequence s[i:j]
        d[s[j]] = j+1; # update d[s[j]] to be the most recent time we have seen s[j]
        
    return currMax;


if __name__ == '__main__':
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABC";
    print(lengthOfLongestSubStringSol1(s));
    print(lengthOfLongestSubStringSol2(s));