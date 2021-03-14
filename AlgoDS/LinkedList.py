class Node:
    # Function to init the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to init the linkedlist object
    def __init__(self):
        self.head = None


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

#code execution starts here
if __name__=='__main__':
    #start with the empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # link first node to second
    llist.head.next = second;

    # link second node to third
    second.next = third;

    llist.printList()



