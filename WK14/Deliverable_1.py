class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return f'{self.data} Node'


class Stack:
    head: Node

    def __init__(self):
        self.head = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_node):
        new_node.next = self.head
        print(f'Adding {new_node} to the stack')
        self.head = new_node
        

    def pop(self):
        if self.head.next is None:
            raise Exception('Stack is empty')
        
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        return popped_node

stack = Stack()

stack.push(Node('First'))
stack.push(Node('Second'))
stack.push(Node('Third'))

print('Stack Full')
stack.print_structure()

print('Last in first out')
popped = stack.pop()

stack.print_structure()
