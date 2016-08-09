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

newlist=LinkList()
newlist.head=Node(1)
a=Node(2)
b=Node(3)
newlist.head.next=a
a.next=b
newlist.show()


        
