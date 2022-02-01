def isAnagramSol1(s, t): # O(n)
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    myDict = dict();
    
    # put all chars in s into dict, values represent count
    for c in s: # O(n)
        if (c not in myDict):
            myDict[c] = 1;
        else:
            myDict[c] = myDict[c]+1;
            
    # check dict for chars in t, if they exist, decrement the count, if they don't return false
    for c in t: # O(m)
        if (c not in myDict):
            return False;
        else:
            myDict[c] = myDict[c]-1;
    
    # make sure all keys (counts) are 0
    for v in myDict: # O(n)
        if myDict[v] != 0:
            return False;
    
    return True;

if __name__ == '__main__':
    s = 'anagram';
    t = 'nagaarm';
    print(isAnagramSol1(s, t));