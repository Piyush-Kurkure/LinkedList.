class Node:
   def __init__(self):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None

   def push(self,data):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node
"""
   def print_from_last(self,n):
      temp = self.head
      while temp!=n:
         temp = temp.next

      while temp is not None:
         temp = temp.next
         print(temp.data)
"""
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)
llist.push(40)

llist.print_from_last(3)