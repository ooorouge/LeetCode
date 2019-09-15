### No.25 Reverse Nodes in K-Group
* 第一个考点应该是反转链表的写法
* 第二个就是反转链表函数返回值的定位，和主函数定位的衔接都需要思考的比较清楚
```java
public ListNode reverse(ListNode begin, ListNode end) {
        ListNode cur = begin.next;
        ListNode prev = cur;
        ListNode next = cur;
        ListNode first = cur;
        while (cur != end) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next; 
        }
        begin.next = prev;
        first.next = cur;
        return first;
    }
```
* 主函数
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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode begin;
        if (head==null || head.next ==null || k==1) return head;
        ListNode dummyhead = new ListNode(-1);
        dummyhead.next = head;
        begin = dummyhead;
        int i=0;
        while (head != null){
    	    i++;
    	    if (i%k == 0){
    		    begin = reverse(begin, head.next);
    		    head = begin.next;
    	    } else {
    		    head = head.next;
    	    }
        }
        return dummyhead.next;
    }
    // begin -> 12345 -> end
    //              ^head
    // begin -> 54321 -> end
    // head = being.next;
    public ListNode reverse(ListNode begin, ListNode end) {
        ListNode cur = begin.next;
        ListNode prev = cur;
        ListNode next = cur;
        ListNode first = cur;
        while (cur != end) {
            next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next; 
        }
        begin.next = prev;
        first.next = cur;
        return first;
    }
}
```
