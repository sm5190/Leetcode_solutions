# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # 1) Move prev to the node just before 'left'
        for _ in range(left - 1):
            prev = prev.next  # safe because 1 ≤ left ≤ right ≤ n

        # 2) Reverse the sublist by head-insertion
        curr = prev.next                   # first node of the sublist
        for _ in range(right - left):
            nxt = curr.next                # node to move to front
            curr.next = nxt.next           # detach nxt
            nxt.next = prev.next           # link nxt in front of sublist
            prev.next = nxt                # advance front

        return dummy.next
