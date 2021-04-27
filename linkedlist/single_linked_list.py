class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    
    def addData(self,data):
        
        node = Node(data)

        if self.head is None:
            self.head = node

        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = node


    def showData(self):

        if self.head is None:
            print("Linked List is Blank")
        
        else:
            current = self.head
            while(current):
                print(current.data,end=" ")
                current = current.next


    def addAtBeginning(self,data):
        node = Node(data)

        if self.head is None:
            self.head = node

        else:
            toBehold = self.head
            self.head = node
            self.head.next = toBehold           
 


linkedlist = Linkedlist()







def mainFunction():
    print("\n \nChoose any of below")
    print("1 - Add Data To a list ")
    print("2 - Show Data of a list ")
    print("3 - Remove Data of a list")
    print("4 - Insert at begining")
    option = int(input("Please choose your option : "))
    print("\n")
    
    if option == 1:
        data = input("Enter your Data : ")
        linkedlist.addData(data)

    elif option == 2:
        linkedlist.showData()

    elif option == 4:
        data = input("Enter data : ")
        linkedlist.addAtBeginning(data)


while(True):
    mainFunction()

