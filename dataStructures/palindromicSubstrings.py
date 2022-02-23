def palindromicSubstringsSol1(s):
    result = 0;
    i = j = 0;
    
    while i < len(s):
        j = i;
        while j < len(s):
            if isPalindrome(s, i, j):
                result += 1;
            j+=1;
        i+=1;
    
    return result;

def palindromicSubstringsSol2(s):
    result = 0;
    i = j = 0;
    d = { };
    
    while i < len(s):
        j = i;
        while j < len(s):
            if s[i:j+1] in d:
                result +=1;
            elif isPalindrome(s, i, j):
                d[s[i:j+1]] = 1;
                result += 1;
            j+=1;
        i+=1;
    
    return result;

def isPalindrome(s, i, j):
    while i <= j:
        if s[i] != s[j]:
            return False;
        i+=1;
        j-=1;
    return True;

if __name__ == '__main__':
    s = 'aaa';
    print(palindromicSubstringsSol1(s));
    print(palindromicSubstringsSol2(s));