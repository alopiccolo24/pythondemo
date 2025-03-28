from node import node

class LinkedListNode:
    def__init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node=Node(data)
        if self.is_empty():
            self.head=new_node
            return

        current=self.head
        while current.next:
            current=current.next
        current.next=newNode

    def prepend(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert(self, index, data)
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(data)
            return

        new_node=Node(data)
        current=self.head
        prev=None
        count=0

        while current and count < index:
            prev=current
            current= current.nextcount+= 1

        if count == index:
            if prev:
                prev.next=new_node
                new_node.next=current
            else:
                self.head=new_node
                new_node.next= current

        else:
            raise IndexError("Index out of range")

    def delete(self, data):
        current= self.head
        prev=None

        while current:
            if current.data== data:
                if prev:
                    prev.next=current.next
                else:
                    self.head=current.next
                return
            prev=current
            current=current.next

    def display(self)
        current=self.head
        elements= []
        while current:
            elements.append(str(current.data))
            current=current.next
        print ("->".join(elements))


    def__str__(self):
        current=self.head
        elements[]
        while current:
            elements.append(str(current.data))
            current=current.next
        print("->".join(elements))

