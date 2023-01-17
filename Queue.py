class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        if self.isEmpty():
            return 'Queue is empty!'
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def __len__(self):
        if self.isEmpty():
            return 0
        else:
            temp = self.linkedlist.head
            counter = 0
            while temp:
                temp = temp.next
                counter += 1
            return counter

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.linkedlist.head = node
            self.linkedlist.tail = node
        else:
            self.linkedlist.tail.next = node
            self.linkedlist.tail = node

    def peek(self):
        if self.isEmpty():
            return 'Queue is empty!'
        else:
            return self.linkedlist.head.value

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty!'
        temp = self.linkedlist.head
        self.linkedlist.head = self.linkedlist.head.next
        return temp

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None
        return 'Queue was deleted!'