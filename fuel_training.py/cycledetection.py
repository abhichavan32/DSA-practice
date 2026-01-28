class node:
    def __init__(self,data):
        self.data=data
        self.next=next

def rmovecycle(head):
    slow=fast=head

    while fast and fast.next:
        slow =slow.next
        fast=fast.next.next

        if slow == fast:
            break
    else:
        return False
    
    slow=head
    while slow.next != fast.next:
        slow=slow.next
        fast=fast.next.next

    fast.next=None
    return True



