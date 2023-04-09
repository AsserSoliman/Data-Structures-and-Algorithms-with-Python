class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        """Constructor"""
        self.head = None

    def __str__(self):
        """returns string for print function"""
        out = ""
        temp = self.head
        if temp:
            while temp:
                out += f'{temp.data}-->'
                temp = temp.next
        else:
            print('Linked List in Empty')

        return out

    def insert_front(self, value):
        """ inserts element at front of linked list"""
        t = Node(value)
        t.next = self.head
        self.head = t

    def insert_back(self, value):
        """ inserts element at back of linked list"""
        t = Node(value)
        temp = self.head
        if self.head:
            while temp.next != None:
                temp = temp.next
            temp.next = t
        else:
            self.head = t

    def insert_index(self,value,index):
        """ add node at specific index in linked list with data equal to value"""
        if index >= self.size() or index < 0:
            print("invalid index")
            return
        else:
            temp = Node(value)
            count = 0
            prev = None
            current = self.head

            while count != index:
                count += 1
                prev = current
                current = current.next

            prev.next = temp
            temp.next = current

    def remove_front(self):
        """ remove element from front of list"""
        if self.head:
            self.head = self.head.next

    def remove_back(self):
        """ remove element from back of list"""
        if self.head:
            if self.head.next:
                prev = None
                current = self.head
                while current.next:
                    prev = current
                    current = current.next
                prev.next = None
            else:
                self.head = None
    
    def remove_index(self,index):
        """ Remove node at specific index in linked list """
        if index >= self.size() or index < 0:
            print("invalid index")
            return
        else:
            count = 0
            prev = None
            current = self.head

            while count != index:
                count += 1
                prev = current
                current = current.next

            prev.next = current.next

    def search(self, value):
        """ searches for element in linked list and returns True if found otherwise False """
        temp = self.head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False

    def delete(self,value):
        """ delete element that's data equals to value"""
        temp = self.head
        if value == temp.data:
            self.head = self.head.next
        else:
            previous = self.head
            temp = temp.next
            while temp:
                if temp.data == value:
                    previous.next = temp.next
                    return
                previous = temp
                temp = temp.next

    def reverse (self):
        """Reverse elements of linked list"""
        if  self.head.next == None:
            return
        else:
            prev = None
            current = self.head
            following = current.next
            while current:
                current.next = prev
                prev = current
                current = following
                if following:
                    following = following.next
            self.head = prev
            return

    def new_reversed_list(self):
        """returns a reversed linked list """
        temp1 = LinkedList()
        temp2 = self.head
        while temp2:
            temp1.insert_front(temp2.data)
            temp2 = temp2.next
        return temp1

    def append_list(self,l):
        """ Take a lined list as input and return a list that consists of elements of object and input linked list"""
        temp = LinkedList()
        temp1 = self.head
        temp2 = l.head
        while temp1:
            temp.insert_back(temp1.data)
            temp1 = temp1.next
        while temp2:
            temp.insert_back(temp2.data)
            temp2 = temp2.next
        return temp

    def size(self):
        """return no of elements in linked list """
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

