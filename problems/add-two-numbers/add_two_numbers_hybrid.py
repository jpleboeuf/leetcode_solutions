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

@classmethod
def from_int(cls:Type[ListNodeType], n:int=0) -> ListNodeType:
    # pylint: disable=not-callable
    div, mod = divmod(n, 10)
    ln_unit = cls(mod)
    ln_prev = ln_unit
    while div != 0:
        div, mod = divmod(div, 10)
        ln = cls(mod)
        ln_prev.next = ln
        ln_prev = ln
    cnstrct = ln_unit
    return cnstrct
ListNode.from_int = from_int

def to_int(self:ListNode) -> int:
    return self.val + (10 * to_int(self.next) if self.next else 0)
ListNode.to_int = to_int


def add_two_numbers(ln1:ListNode, ln2:ListNode) -> ListNode:
    return ListNode.from_int(ln1.to_int() + ln2.to_int())


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
