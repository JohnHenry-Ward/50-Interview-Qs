from LinkedList import LinkedList;

def removeNthNodeSol1(head, n):
    curr = head;
    count = 0;
    while curr != None:
        count += 1;
        curr = curr.next;
        
    nodeToRemove = count - n;
    curr = head;
    prev = None;
    count = 0;
    while curr != None:
        if count == nodeToRemove:
            if prev != None:
                prev.next = curr.next;
                return head;
            else:
                return curr.next;
        else:
            prev = curr;
            curr = curr.next;
            count += 1;


def removeNthNodeSol2(head, n):
    slow = fast = head;
    prev = None;
    for x in range(n):
        fast = fast.next;
    
    while fast != None:
        prev = slow;
        slow = slow.next;
        fast = fast.next;
            
    if prev == None:
        return head.next;
    else:
        prev.next = slow.next;
        return head;

if __name__ == '__main__':
    LL1 = LinkedList();
    LL1.push(5);
    LL1.push(4);
    LL1.push(3);
    LL1.push(2);
    LL1.push(1);
    LL2 = LinkedList();
    LL2.push(5);
    LL2.push(4);
    LL2.push(3);
    LL2.push(2);
    LL2.push(1);
    
    removeNthNodeSol1(LL1.head, 2).print();
    removeNthNodeSol2(LL2.head, 2).print();