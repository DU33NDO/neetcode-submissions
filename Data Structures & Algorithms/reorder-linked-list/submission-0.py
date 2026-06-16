# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        slow, fast = head, head 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
        middle = slow 
        left, right = head, middle.next
        middle.next = None

        prev, curr = None, right
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        right = prev 
        curr = head

        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1
            left, right = tmp1, tmp2