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

    def deleten(self,val) :
        temp=self.head
        if(temp is not None) :
            if(temp.value==val) :
                self.head=temp.next
                temp=None
                return
            while(temp is not None) :
                if (temp.value==val) :
                    break
                prev=temp
                temp=temp.next

            if(temp==None) :
                return

            prev.next=temp.next
            temp=None





newlist=LinkList()
newlist.beg(1)
newlist.beg(2)
newlist.beg(3)
newlist.beg(4)
newlist.deleten(3)
newlist.show()
