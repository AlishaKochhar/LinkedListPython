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

    def position(self,given,data) :
        if given is None :
            print("Empty list")
            return
        new_node=Node(data)
        new_node.next=given.next
        given.next=new_node

    def end(self,data) :
        new_node=Node(data)
        if self.head is None :
            self.head=new_node
            return
        last=self.head
        while(last.next) :
            last=last.next
        last.next=new_node
        

newlist=LinkList()
newlist.head=Node(1)
a=Node(2)
b=Node(4)
newlist.head.next=a
a.next=b
c=newlist.beg(0)
d=newlist.position(a,3)
e=newlist.end(5)
newlist.show()


        
