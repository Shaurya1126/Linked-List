class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class linked_list:
    def __init__(self):
        self.head = None

    def add_at_begin(self,data):
        node = Node(data,self.head)
        self.head = node

    def display(self):
        if self.head ==None:
            print("The linked list is empty")
            return
        i = self.head
        while i != None:
            print(i.data)
            i = i.next

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return
 
        i = self.head
        while i.next != None:
            i = i.next
        node = Node(data,None)
        i.next = node

    def get_length(self):
        if self.head != None:
            x=1
            i= self.head
            while i.next != None:
                x=x+1
                i=i.next
            print("The total number of elements is: ",x)
        else:
            print("There are no elements in the linked list")

    def insert_at(self,index,data):
        i = self.head
        count = 0

        while i != None:
            if count == index-1:
                node = Node(data,i.next)
                i.next = node
                break

            i = i.next
            count += 1
    """def remove(self,data):
        i=self.head 
        num=1
        while i != None: 
            if num == data:
                node= Node(data, i.next)
                node=node.next 
                break 
            i= i.next """
    
    def delete(self,value):
         i = self.head
         if i != None:
           if i.data == value:
             self.head = i.next
             return

           while i != None:
            if i.data == value:
              break
            prev = i
            i = i.next

           prev.next = i.next


    def search(self,find):
        i= self.head
        count=1
        while i != None: 
            if find == i.data: 
                return count
            i=i.next
            count +=1
        return False

    def insert_values(self, lst): 
        for i in lst:
            self.insert_at_end(i)
    def min(self):
        i= self.head
        x=i.data 
        while i != None: 
            if x>i.data: 
                x=i.data
            i=i.next
        return x 
    def max(self): 
        i= self.head
        x= i.data 
        while i != None: 
            if x<i.data:
                x=i.data
            i=i.next 
        return x 





#i.next.next

l = linked_list()
l.add_at_begin(1)
l.add_at_begin(2)
l.add_at_begin(3)
l.insert_at_end(4)
l.insert_at_end(5)
l.insert_at(2,10)
l.delete(3)
l.get_length()
l.insert_values([800,801,802])
l.display()
print("The smallest element is: ", l.min())
print("The largest element is: ", l.max())
print("The element is present at", l.search(50))