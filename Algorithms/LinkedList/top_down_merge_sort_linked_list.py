from typing import Optional

from lctest import ListNode


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_mid(head):
            """
                get mid and also split the linked list
            """
            slow = ListNode(next=head)
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow.next
            slow.next = None

            return mid

        def merge(list1, list2):
            head = ListNode()

            if not list1:
                return list2
            elif not list2:
                return list1
            elif list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
            head.next = merge(list1, list2)
            return head

        if not head or not head.next:
            return head

        mid = get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
