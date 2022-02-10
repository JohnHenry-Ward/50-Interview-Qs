from LinkedList import LinkedList;

def reverseListSol1(head):
    prev = None;
    curr = head;
    nxt = None;
    
    while (curr != None):
        nxt = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nxt;
        
    return prev;

if __name__ == '__main__':
    ll = LinkedList();
    ll.push(5);
    ll.push(4);
    ll.push(3);
    ll.push(2);
    ll.push(1);
    ll.printList();
    curr = reverseListSol1(ll.head);
    while curr:
        print(curr.data);
        curr = curr.next;