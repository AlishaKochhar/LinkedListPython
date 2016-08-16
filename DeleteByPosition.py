class Node :
    def __init__(self,value) :
        self.value=value
        self.next=None

class LinkList :
    def __init__(self) :
        self.head=None

    def show(self) :
        temp=self.head
        while(temp) :
            print(temp.value)
            temp=temp.next

    def beg(self,data) :
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def delete_key(self,pos) :
        if self.head==None :
            return
        temp=self.head
        if pos==0 :
            self.head=temp.next
            temp=None
            return

        for i in range(pos-1) : #pos=index here
            temp=temp.next
            if temp is None :
                break

        if temp is None :
            return
        if temp.next is None :
            return

        next=temp.next.next
        temp.next=None
        temp.next=next


newlist=LinkList()
newlist.beg(7)
newlist.beg(6)
newlist.beg(5)
newlist.beg(4)
newlist.beg(3)
newlist.beg(2)
newlist.beg(1)
newlist.delete_key(2)
newlist.delete_key(4)

newlist.show()



