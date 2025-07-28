# https://leetcode.com/problems/two-sum

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        
        while l1 or l2 or carry:
            listVal1 = l1.val if l1 else 0
            listVal2 = l2.val if l2 else 0

            carry, sumVal = divmod(listVal1 + listVal2 + carry, 10)
            current.next = ListNode(sumVal)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return(dummyHead.next)
