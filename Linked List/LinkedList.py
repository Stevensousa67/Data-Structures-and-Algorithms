class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)  # Create new node
        if self.head is None:   # Check if LL is empty
            self.head = new_node    # Set LL's head to new node
            self.tail = new_node    # Set LL's tail to new node
        else:
            self.tail.next = new_node   # Point LL's tail.next to new node
            self.tail = new_node        # Set LL's tail to new node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())

