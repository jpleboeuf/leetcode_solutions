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

def to_number(self:ListNode) -> int:
    ln = self
    val_s = ""
    val_s += str(ln.val)
    while ln.next is not None:
        ln = ln.next
        val_s += str(ln.val)
    val = int(val_s[::-1])
    return val
ListNode.to_number = to_number


def add_two_numbers(ln1:ListNode, ln2:ListNode) -> ListNode:
    val1 = ln1.to_number()
    val2 = ln2.to_number()
    val = val1 + val2
    val_lst = [d for d in str(val)[::-1]]
    return ListNode.from_list(val_lst)


class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        return add_two_numbers(l1, l2)


def main():

    solution = Solution()

    for l1, l2 in [
                ([2, 4, 3], [5, 6, 4]),                 # Example 1
                ([0], [0]),                             # Example 2
                ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]),  # Example 3
            ]:
        ln1 = ListNode.from_list(l1)
        ln2 = ListNode.from_list(l2)
        print(f"ln1={ln1}, ln2={ln2} ⇒ solution={solution.addTwoNumbers(ln1, ln2)}")

if __name__ == '__main__':
    main()
