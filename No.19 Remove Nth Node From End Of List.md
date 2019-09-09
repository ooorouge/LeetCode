### Remove Nth Node Of List
* 主要的问题就是这个start从什么地方开始，作为一个比较好的办法就是下面代码的前三行的写法，可以绕开一些由于删除第一个节点带来的问题
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode start = new ListNode(0);
        start.next = head;
        ListNode slow = start, fast = start;
        
        for(int i=1; i<=n+1; i++)   {
            fast = fast.next;
        }
        while(fast != null) {
            slow = slow.next;
            fast = fast.next;
        }
        slow.next = slow.next.next;
        return start.next;
    }
}
```
