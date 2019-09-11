### No.24 Swap Nodes in Pairs
* 注意一下比较常规的写法，然后画图分析思路就好了
```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
        1-> 2-> 3-> 4
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        while (head == null || head.next == null) {return head;}
        ListNode start = new ListNode(0);
        start.next = head;
        ListNode begin = start;
        
        while (begin.next !=null && begin.next.next != null) {
            ListNode reserve = begin.next.next;
            begin.next.next = reserve.next;
            reserve.next = begin.next;
            begin.next = reserve;
            begin = begin.next.next;
        }
        return start.next;
    }
}
```
