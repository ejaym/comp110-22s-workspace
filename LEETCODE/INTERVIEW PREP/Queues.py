"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    
    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    
    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def del_first(self):
        current = self.head
        if current is None:
            return None
        value = current.value
        if current.next is not None:
            self.head = current.next
        else:
            self.head = None
        return value


class Queue:
    def __init__(self, head=None):
        self.head = LinkedList(Element(head))

    def enqueue(self, new_element):  # should be giving it to the end of the linked list,,, shouldn't return anything,,,, 
        self.head.append(Element(new_element))

    def peek(self):  # should just be looking at the value of the element first in the queue, but do not remove it from the queue yet,,, return the value DO NOT REMOVE IT THOUGH
        return self.head.head.value if self.head else None

    def dequeue(self):  # should be taking out from the front of the liniked list,,, should return the value of the dequeued item
        return self.head.del_first()


# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())