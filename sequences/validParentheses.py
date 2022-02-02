def isValidSol1(s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []; # push (append) and pop only
        opening = ['(', '{', '['];
        closing = [')', '}', ']'];
        
        for bracket in s: # O(n)
            if bracket in opening: # O(1)
                stack.append(bracket);
            else:
                if (len(stack) == 0):
                    return False;
                else:
                    top = stack.pop();
                    if (top not in opening): # O(1)
                        return False;
                    elif (opening.index(top) != closing.index(bracket)):
                        return False;
                
        return len(stack) == 0;

if __name__ == '__main__':
    s = '()[]{}';
    print(isValidSol1(s));