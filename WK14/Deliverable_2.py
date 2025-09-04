# Class to create node objects to be used on double ended queue.
class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None, tail=None):
        self.data = data
        self.next = next
        self.tail = tail
    
    def __str__(self):
        return f'{self.data} Node'

#Class to create Double Ended Queue 
class DoubleEndedQueue:
    head: Node

    def __init__(self):
        self.head = None
        self.tail = None

    # Function to print status of the Double Ended Queue
    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    # Function to add items from the right side of the queue
    def push_right(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        
        print(f'Adding {new_node} to the right')
        
    # Function to pop items from the right side of the queue
    def pop_right(self):
        if self.head is None:
            raise Exception('Queue empty')
        
        if self.head == self.tail:
            popped = self.head
            self.head = None
            self.tail = None
            print(f'The queue is now empty')
            return popped
        
        current = self.head
        while current.next != self.tail:
            current = current.next
        
        popped_node = self.tail
        self.tail = current
        self.tail.next = None
        print(f'Removing {popped_node}')
        return popped_node

    #Function to add items to the left side of the queue 
    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        print(f'Adding {new_node} to the left')

    #Function to remove items to the left side of the queue 
    def pop_left(self):
        if self.head.next is None:
            raise Exception('Queue is empty')
        
        popped_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        popped_node.next = None
        print(f'Removing {popped_node}')
        return popped_node


#Testing Enviorment 
queue = DoubleEndedQueue()
#Texting Right features pushing and popping
queue.push_right(Node('First'))
queue.push_right(Node('Second'))
print('Queue Full')
queue.print_structure()
queue.pop_right()
queue.print_structure()

print('-----------')

#Testing Left feature pushing and popping
queue.push_left(Node('Third'))
print('Queue Full')
queue.print_structure()
queue.pop_left()

queue.print_structure()
