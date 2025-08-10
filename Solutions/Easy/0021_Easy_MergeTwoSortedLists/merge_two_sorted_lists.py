# https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        list3 = dummy
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next
        list3.next = list1 if list1 else list2
        return dummy.next