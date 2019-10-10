### EMMMM,这道题其实和之前这种取链表里的第k个一样的，用两个指针
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int n) {
    if (head == null || head.next == null || n == 0) {
         return head;
    }
    ListNode fast = head;
    ListNode slow = head;
    ListNode newHead;
    for (int i = 0; i < n; i++) {
        if (fast.next == null) {
            n = n % (i+1);
            i = -1;
            fast = head;
        } else {
            fast = fast.next;
        }
    }
    while (fast.next != null) {
        fast = fast.next;
        slow = slow.next;
    }
    fast.next = head;
    newHead = slow.next;
    slow.next = null;
    return newHead;
}
}
```
