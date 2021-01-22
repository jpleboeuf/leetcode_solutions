from __future__ import annotations
from typing import Type, TypeVar
from typing import List


ListNodeType = TypeVar('ListNodeType', bound='ListNode')
# Definition for singly-linked list.
class ListNode:
    
    def __init__(self, val:int=0, next:ListNode=None):
        self.val = val
        self.next = next

    def __str__(self):
        ln = self
        s = ""
        s += "["
        s += str(ln.val)
        while ln.next is not None:
            if ln.next is ln:
                s += "… "  # Circular List detected!
                break
            s += "→ "
            ln = ln.next
            s += str(ln.val)
        s += "]"
        return s

@classmethod
def from_list(cls:Type[ListNodeType], l:List=[]) -> ListNodeType:
    # pylint: disable=not-callable
    if len(l) > 0:
        ln0 = cls(l[0])
        ln_prev = ln0
        for le in l[1:]:
            ln = cls(le)
            ln_prev.next = ln
            ln_prev = ln
        cnstrct = ln0
    else:
        cnstrct = cls()
    return cnstrct
ListNode.from_list = from_list


def add_two_numbers(ln1:ListNode, ln2:ListNode) -> ListNode:
    ln_cur = lnr = ListNode()
    carry = 0
    while ln1 or ln2 or carry:
        dv1 = dv2 = 0
        if ln1:
            dv1 = ln1.val
            ln1 = ln1.next
        if ln2:
            dv2 = ln2.val
            ln2 = ln2.next
        carry, dv = divmod(dv1 + dv2 + carry, 10)
        ln_cur.next = ListNode(dv)
        ln_cur = ln_cur.next
    return lnr.next


class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        return add_two_numbers(l1, l2)


def main():

    solution = Solution()

    for l1, l2 in [
                ([2, 4, 3], [5, 6, 4]),                 # Example 1
                ([0], [0]),                             # Example 2
                ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),  # Example 3
                ([0, 1], [0, 1, 2]),                    # Supplementary test case 1
                ([], [0, 1]),                           # Supplementary test case 2
                ([9, 9], [1]),                          # Supplementary test case 3
            ]:
        ln1 = ListNode.from_list(l1)
        ln2 = ListNode.from_list(l2)
        print(f"ln1={ln1}, ln2={ln2} ⇒ solution={solution.addTwoNumbers(ln1, ln2)}")

if __name__ == '__main__':
    main()
