class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;

    def print(self):
        curr = self;
        while curr:
            print(curr.data);
            curr = curr.next;

class LinkedList:
    def __init__(self):
        self.head = None;

    def push(self, data):
        newNode = Node(data);
        newNode.next = self.head;
        self.head = newNode;
        return newNode;

    def printList(self):
        curr = self.head;
        while curr:
            print(curr.data);
            curr = curr.next;