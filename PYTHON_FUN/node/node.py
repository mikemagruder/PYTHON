class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def print_values(self):
        runner = self.head
        while(runner != None):
            print(runner.val)
            runner = runner.next
        return self

class SLNode:
    def __init__(self, val):
        self.val = val
        self.next = None


myList = SList()
myList.add_to_front("linked lists").add_to_front("Are").add_to_back("fun?").print_values()

mySecondList = SList()
mySecondList.add_to_front("jumped").add_to_front("brown fox").add_to_front("The").add_to_back("over").add_to_back("the moon").print_values()