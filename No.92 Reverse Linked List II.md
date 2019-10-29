### 这个题写了两遍感觉都错了，问题如下
* 第一，出了循环之后，pre在最后一个该被反转的位置，cur在不用反转的地方，写错了
```java
   start.next.next = cur;
   start.next = pre;
```
* 第二，这样写，有可能next本身会被赋值为null，然后继续调用`next = next.next`引起报错
```java
   next = next != null ? next.next : null;
```
```java
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m == n) {return head;}
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode start = dummy;
        int len = n - m + 1;
        
        while (m > 1) {
            start = start.next;
            --m;
        }
        
        ListNode pre = start;
        ListNode cur = pre.next;
        ListNode next = cur.next;
        
        while (len > 0) {
            cur.next = pre;
            pre = cur;
            cur = next;
            next = next != null ? next.next : null;
            --len;
        }
        start.next.next = cur;
        start.next = pre;
        
        return dummy.next;
    }
}
```
