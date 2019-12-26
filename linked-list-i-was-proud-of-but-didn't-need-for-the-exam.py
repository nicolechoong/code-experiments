class LinkedList:
   def __init__(self):
       self.length = 0
       self.head = None

   def insert(self, data, pos=None):
       newNode = Node(data)
       node = self.head

       if node is not None:
           if pos == 0:
               self.head, newNode.pointer = newNode, node
               return

           elif pos == None:
               pos = self.length

           for i in range(0,pos-1):
               if node.pointer == None:
                   break
               node = node.pointer
           node.pointer, newNode.pointer = newNode, node.pointer

       else:
           self.head = newNode

       self.length += 1

   def delete(self, item):
       node = self.head

       if node.data == item:
           self.head = node.pointer

       else:
           while node.pointer is not None:
               if node.pointer.data == item:
                   node.pointer = node.pointer.pointer
                   break
               node = node.pointer

       self.length -= 1

   def search(self, item):
      node = self.head

      while node.pointer is not None:
          if node.pointer.data == item:
              return True
          node = node.pointer

      return False

# For debugging purposes :)

   def __str__(self):
       output = "[ "
       node = self.head

       while node is not None:
           output += str(node) + " "
           node = node.pointer
       output += "]"
       return output
