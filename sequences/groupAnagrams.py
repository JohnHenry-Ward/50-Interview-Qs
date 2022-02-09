def mergeAnagramsSol1(strs):
    result = [];
    resultIndex = 0;
    d = {}; # keys are the anagrams, values are their index in result
    
    for s in strs:
        currAnagram = ''.join(sorted(s)); 
        if currAnagram in d: # if we've already seen the anagram
            result[d[currAnagram]].append(s); # append it to the already existing list of these same anagrams
        else:
            d[currAnagram] = resultIndex; # add anagram to dict
            result.append([]); # make space for a new list
            result[resultIndex].append(s); # add s to the new list
            resultIndex+=1; # update where we are in result
        
    return result;

if __name__ == '__main__':
    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'];
    print(mergeAnagramsSol1(strs));