from LinkedList import LinkedList;

def detectACycleSol1(head):
    if head == None: # LinkedList of length 0
        return False;
    
    slow = head;
    fast = head.next;
    
    while fast != None: # while we havent hit the end of the list
        if slow == fast: # if the two pointers collide
            return True;
        else:
            slow = slow.next; # move to next
            fast = fast.next  # move to next
            if fast == None:  # if it's the end
                return False;
            else:
                fast = fast.next; # otherwise, move to next (so fast has now moved 2 nodes)
            
    return False;

def detectACycleSol2(head):
    if head == None:
        return False;

    slow = head;
    fast = head.next;

    while fast != None and fast.next != None:
        if slow == fast:
            return True;
        slow = slow.next;
        fast = fast.next.next;

    return False;

if __name__ == '__main__':
    LL = LinkedList();
    temp = LL.push(-4);
    LL.push(0);
    temp2 = LL.push(2);
    LL.push(3);
    temp.next = temp2;
    print(detectACycleSol1(LL.head));
    print(detectACycleSol2(LL.head));