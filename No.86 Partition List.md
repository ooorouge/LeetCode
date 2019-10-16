### 把链表分成两个部分，大于x的在前面，剩下的按照原来的顺序排列
* 重新开两个新的链表，然后返回新链表的头
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
    public ListNode partition(ListNode head, int x) {
        ListNode dummy = new ListNode(-1);
        ListNode dummy2 = new ListNode(-1);
        ListNode cur = dummy;
        ListNode cur2 = dummy2;
        
        while (head != null) {
            if (head.val < x) {
                cur.next = new ListNode(head.val);
                cur = cur.next;
            } else {
                cur2.next = new ListNode(head.val);
                cur2 = cur2.next;
            }
            head = head.next != null ? head.next : null;
        }
        cur.next = dummy2.next;
        return dummy.next;
    }
}
```
