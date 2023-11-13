class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    # TO INSERT NODE AT THE BEGINING
    def insert_node_at_begining(self,data):
        node= Node(data, self.head)
        self.head = node

    # TO PRINT lINKED lIST
    def print(self):
        if self.head is None:
            print("linkedlist is empty")
        itr = self.head
        listr = ''
        while itr:

            listr +=  str(itr.data)
            if itr.next:
                listr +="-->"
            itr = itr.next
        print(listr)

    # to insert node at the end
    def insert_node_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
        itr=self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    # to get the length of the linked list
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count

    # to insert node by index
    def insert_by_index(self,data,index):
        if index<0 or self.get_length()<=index:
            print("Invalid index")
        if index == 0:
            self.insert_node_at_beging(data)
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1

    # to remove node by index
    def remove_by_index(self,index):
        itr=self.head
        count=0
        if index==0:
            self.head=self.head.next
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count+=1
    # insert node by value after a node
    def insert_after_value(self,data_after_to_insert,data_to_insert):
        count = 0
        itr = self.head
        while itr:
            if data_after_to_insert == itr.data:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        else:
            print("Data not found")
    # to remove a node by value
    def remove_by_value(self,data_after_to_remove):
        count=0
        itr = self.head
        while itr:
            if data_after_to_remove == itr.data:
                itr.next = itr.next.next
                break
            itr=itr.next
            count+=1
        else:
            print("Data not found")






lnk_llist = Linkedlist()
lnk_llist.insert_node_at_begining(5)
lnk_llist.insert_node_at_begining(89)
lnk_llist.insert_node_at_end(100)
lnk_llist.insert_node_at_begining(50)
lnk_llist.print()
lnk_llist.insert_by_index(500,2)
lnk_llist.print()
lnk_llist.remove_by_index(1)
lnk_llist.print()
lnk_llist.insert_after_value(89,400)
lnk_llist.print()
lnk_llist.remove_by_value(400)
lnk_llist.print()
print(lnk_llist.get_length())