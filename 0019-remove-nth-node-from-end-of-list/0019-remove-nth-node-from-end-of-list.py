# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        curr=head
        while curr:
            length+=1
            curr=curr.next
        
        print(length)

        node_to_remove=length-n

        if node_to_remove==0:
            return head.next
        print(node_to_remove)
        prev=ListNode(-1)
        curr=head
        for i in range(length):
            if i==node_to_remove:
                curr_next=curr.next
                prev.next=curr_next
                break
            prev=curr
            if curr.next:
                curr=curr.next


        return head



